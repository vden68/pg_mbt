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

        global count_table_points_index_gist
        table_name = ("points_index_gist_{test_uuid}").format(test_uuid=self.db.app.mbt_conn.test_uuid)
        c_count = self.db.table_check.check_count(count_rows_table=count_table_points_index_gist, table_name=table_name)

        return c_count



