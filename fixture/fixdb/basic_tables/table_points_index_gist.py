__author__ = 'vden'

import pytest
import time



count_table_points_index_gist = 0

class Table_points_index_gistHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        if self.db.initdb.check_tablename(tablename='points_index_gist_'+self.db.app.mbt_conn.test_uuid) :
            print(("table '%s' already created") % 'points_index_gist')
        else:
            print(("table '%s' no created") % 'points_index_gist')

            list_sql_char = []

            list_sql_char.append("BEGIN")

            list_sql_char.append(("""
                     CREATE TABLE points_index_gist_{test_uuid}
                     (id         serial NOT NULL 
                                 CONSTRAINT points_index_gist_{test_uuid}_pkey
                                 PRIMARY KEY ,
                     p_point point NOT NULL )
                     ;""") .format(test_uuid=self.db.app.mbt_conn.test_uuid)
                                 )

            list_sql_char.append(("""
                CREATE  INDEX  
                     points_index_gist_{test_uuid}_column_p_point 
                  ON 
                     points_index_gist_{test_uuid}  USING GIST(p_point)
                ;""") .format(test_uuid=self.db.app.mbt_conn.test_uuid))

            list_sql_char.append('COMMIT;')

            with pytest.allure.step('DDL=%s' % list_sql_char):
                self.db.cur_e.execute_ddl(list_sql_char=list_sql_char)


    @pytest.allure.step('insert in table "fibonacci_number"')
    def insert(self, list_points=None, commit=True):
        global count_table_points_index_gist

        list_sql_char=[]

        list_sql_char.append("BEGIN;")
        sql_char=(("""INSERT INTO points_index_gist_{test_uuid}
                             (p_point) VALUES""").format(test_uuid=self.db.app.mbt_conn.test_uuid))

        for p in list_points:
            sql_char+=("""
                       ({pl_point}),""").format (pl_point=("'"+str(p.p_point_x)+","+str(p.p_point_y))+"'")
        sql_char=sql_char[:-1]+" RETURNING id ;"

        list_sql_char.append(sql_char)

        if commit==True:
            list_sql_char.append('commit;')

            with pytest.allure.step('insert plus commit  SQL=%s' % list_sql_char):
                list_row = self.db.cur_e.execute_insert(list_sql_char=list_sql_char)

                count_table_points_index_gist+=len(list_points)

        else:

            list_sql_char.append('rollback;')

            with pytest.allure.step('insert plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_insert(list_sql_char=list_sql_char)


    @pytest.allure.step('check count')
    def check_count(self):
        c_count = False
        global count_table_points_index_gist
        self.checking_completion_of_all_locks()

        sql_char = ("""
                                    select
                                      count (id)
                                    from
                                      points_index_gist_{test_uuid}
                                                       ;
                                    """).format(test_uuid=self.db.app.mbt_conn.test_uuid)
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
                        print("count_table_points_index_gist=", count_table_points_index_gist, "node_id=",
                              selected_node.node_id, "count=", count)
                        list_count_node_id.append(count)
                    else:
                        print("node_id=", selected_node.node_id, "count=", None)
                        list_count_node_id.append(None)

            print("list_count_node_id=", list_count_node_id)

            for count_node_id in list_count_node_id:
                if not (count_node_id == count_table_points_index_gist or count_node_id is None):
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

        print('sql_char=' , sql_char)


        for selected_node in self.db.app.mbt_hosts_read:

            count_lock=10
            count2=0
            while count_lock!=0:


                with pytest.allure.step('Checking completion of all locks  SQL=%s' % sql_char):
                    list_count = self.db.cur_e.execute_select_list(list_sql_char=list_sql_char, selected_node=selected_node)

                    if list_count is not None:
                        for row in list_count:
                            (count_lock,) = row

                    if count2>1:
                        time.sleep(1)

                    if count2>40:
                        break

                    count2+=1
                    print('selected_node=', selected_node,  "count_lock=", count_lock)




