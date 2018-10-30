__author__ = 'vden'

import pytest



count_table_points_index_gist = 0

class Table_points_index_gistHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        if self.db.initdb.check_tablename(tablename='table_points_index_gist'+self.db.app.mbt_conn.test_uuid) :
            print(("table '%s' already created") % 'table_points_index_gist')
        else:
            print(("table '%s' no created") % 'table_points_index_gist')

            list_sql_char = []

            list_sql_char.append("begin;")

            list_sql_char.append(("""
                     CREATE TABLE table_points_index_gist_{test_uuid}
                     (id         serial NOT NULL 
                                 CONSTRAINT table_points_index_gist_{test_uuid}_pkey
                                 PRIMARY KEY ,
                     p_point point NOT NULL )
                     ;""") .format(test_uuid=self.db.app.mbt_conn.test_uuid)
                                 )

            #list_sql_char.append(("""
                #CREATE  INDEX  fibonacci_number_{test_uuid}_column_fib_number ON fibonacci_number_{test_uuid}(fib_number)
                #;""") .format(test_uuid=self.db.app.mbt_conn.test_uuid))

            list_sql_char.append('commit;')

            with pytest.allure.step('DDL=%s' % list_sql_char):
                list_row = self.db.cur_e.execute_ddl(list_sql_char=list_sql_char)

