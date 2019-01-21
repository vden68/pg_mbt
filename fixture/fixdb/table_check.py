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
        #self.checking_completion_of_all_locks(table_name=table_name)

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

    def checking_completion_of_all_locks(self, table_name=None):

        list_sql_char = []

        list_sql_char.append("BEGIN;")

        sql_char = ("""SELECT
                                count(c.relname)
                             FROM
                               pg_locks AS l
                               LEFT JOIN pg_class AS c ON l.relation = c.oid
                             WHERE
                               relname='{s_table_name}'
                             ;
                            """).format(s_table_name=table_name)
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
                    else:
                        break

                    if count2 > 1:
                        time.sleep(1)

                    if count2 > 120:
                        break

                    count2 += 1
                    print('selected_node=', selected_node, "count_lock=", count_lock)


    def check_extension_pg(self, sql_char=None, extension_pg_name=None):
        extension_pg=False
        #sql_char = "SELECT extname FROM pg_extension;"
        #extension_pg_name = 'pg_pathman'

        for x in range(10):

            if x > 1:
                time.sleep(2)

            list_extension_pg_pathman_node_id = []
            for selected_node in self.db.app.mbt_hosts_read:

                with pytest.allure.step('get the number of rows  SQL=%s' % sql_char):
                    list_extension = self.db.cur_e.execute_select(sql_char=sql_char, selected_node=selected_node)

                    if list_extension is not None:
                        for row in list_extension:
                            (extname,) = row
                            if extname== extension_pg_name:
                                break
                        print("node_id=", selected_node.node_id, "extname=", extname)
                        list_extension_pg_pathman_node_id.append(extname)
                    else:
                        print("node_id=", selected_node.node_id, "extname=", None)
                        list_extension_pg_pathman_node_id.append(None)

            print("list_extension_pg_pathman_node_id=", list_extension_pg_pathman_node_id)

            for extension_pg in list_extension_pg_pathman_node_id:
                if not (extension_pg == extension_pg_name or extension_pg is None):
                    break
            else:
                extension_pg = True
                break

        return extension_pg


    def get_number_of_rows_from_table(self, table_name=None):
        count_rows = None
        # global count_table_points_index_gist
        # self.checking_completion_of_all_locks(table_name=table_name)

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

            with pytest.allure.step('get the number of rows  SQL=%s' % sql_char):
                list_count = self.db.cur_e.execute_select(sql_char=sql_char)

                if list_count is not None:
                    for row in list_count:
                        (count_rows,) = row
                    print("count_rows=",  count_rows)
                else:
                    print("count_rows=", None)

            if count_rows is not None:
                break


        return count_rows

    def get_pathman_partition_list(self):
        pass



