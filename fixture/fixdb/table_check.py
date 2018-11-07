__author__ = 'vden'


import pytest
import time



class TableCheckHelper():


    def __init__(self, db):
        self.db = db

    @pytest.allure.step('check count')
    def check_count(self, count_rows_table=None, table_name=None):
        c_count = False
        #global count_table_points_index_gist
        self.checking_completion_of_all_locks()

        sql_char = ("""
                                        SELECT
                                          count(*)
                                        FROM
                                          {s_table_name}
                                                           ;
                                        """).format(s_table_name=table_name)
        # print('sql_char=', sql_char)

        for x in range(10):

            if x > 1:
                time.sleep(2)

            list_count_node_id = []
            for selected_node in self.db.app.mbt_hosts_read:

                with pytest.allure.step('get the number of rows  SQL=%s' % sql_char):
                    list_count = self.db.cur_e.execute_select(sql_char=sql_char, selected_node=selected_node)

                    if list_count is not None:
                        for row in list_count:
                            (count,) = row
                        print("count_rows_table=", count_rows_table, "node_id=",
                              selected_node.node_id, "count=", count)
                        list_count_node_id.append(count)
                    else:
                        print("node_id=", selected_node.node_id, "count=", None)
                        list_count_node_id.append(None)

            print("list_count_node_id=", list_count_node_id)

            for count_node_id in list_count_node_id:
                if not (count_node_id == count_rows_table or count_node_id is None):
                    break
            else:
                c_count = True
                break

        return c_count

    def checking_completion_of_all_locks(self):

        list_sql_char = []

        list_sql_char.append("BEGIN;")

        sql_char = ("""SELECT
                                count(c.relname)
                             FROM
                               pg_locks AS l
                               LEFT JOIN pg_class AS c ON l.relation = c.oid
                             WHERE
                               relname='points_index_gist_{test_uuid}'
                             ;
                            """).format(test_uuid=self.db.app.mbt_conn.test_uuid)
        list_sql_char.append(sql_char)
        list_sql_char.append('commit;')

        # print('sql_char=' , sql_char)

        for selected_node in self.db.app.mbt_hosts_read:

            count_lock = 10
            count2 = 0
            while count_lock != 0:

                with pytest.allure.step('Checking completion of all locks  SQL=%s' % sql_char):
                    list_count = self.db.cur_e.execute_select_list(list_sql_char=list_sql_char,
                                                                   selected_node=selected_node)

                    if list_count is not None:
                        for row in list_count:
                            (count_lock,) = row

                    if count2 > 1:
                        time.sleep(1)

                    if count2 > 40:
                        break

                    count2 += 1
                    print('selected_node=', selected_node, "count_lock=", count_lock)



