__author__ = 'vden'

import time
import random

from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

list_table_fibonacci_number = []
count_table_fibonacci_number = 0

class Table_fibonacci_numberHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        if self.db.initdb.check_tablename(tablename='fibonacci_number'):
            print(("table '%s' already created") % 'fibonacci_number')
        else:
            print(("table '%s' no created") % 'fibonacci_number')

            conn = self.db.conn.db_write()

            sql_char = """
                  create table fibonacci_number
                    (
                       id         serial not null
                         constraint fibonacci_number_pkey
                         primary key,
                        fib_number bigint,
                        test_start_timestamp timestamp                        
                     );

                    create unique index fibonacci_number_id_uindex
                       on fibonacci_number (id);
                       
                    create index fibonacci_number_test_start_timestamp_index
                        on fibonacci_number (test_start_timestamp desc); 
                        
                    commit ;
                       """


            #print('sql_char=', sql_char)
            cursor = self.db.cur_e.cursor_execute(conn=conn, sql_char=sql_char)

            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()


    def insert(self, fib_number=None, commit=True):
        global list_table_fibonacci_number
        global count_table_fibonacci_number

        list_sql_char=[]

        list_sql_char.append(("""
                          insert into fibonacci_number
                             (fib_number, test_start_timestamp) VALUES 
                             (%s, '%s') RETURNING id
                          ; 
                               """) %(fib_number, self.db.app.mbt_conn.test_start_timestamp)
                             )

        if commit:
            list_sql_char.append('commit;')

            list_row = self.db.cur_e.execute_insert(list_sql_char=list_sql_char)

            for row in list_row:
                list_table_fibonacci_number.append(Table_fibonacci_number(id=row, fib_number=fib_number,
                                                                      test_start_timestamp=self.db.app.mbt_conn.test_start_timestamp))
            if len(list_table_fibonacci_number)>10:
                r_list= random.choice(list_table_fibonacci_number)
                list_table_fibonacci_number.remove(r_list)

            count_table_fibonacci_number+=1





    def get_list(self):
        global list_table_fibonacci_number
        return list_table_fibonacci_number


    def check_count(self):
        global count_table_fibonacci_number

        c_count = False
        x=1
        for x in range(10):
            sql_char = ("""
                        select
                          count (id)
                        from
                          fibonacci_number
                        where
                           test_start_timestamp = '%s'                    ;
                        """) % (self.db.app.mbt_conn.test_start_timestamp)

            # print('sql_char=', sql_char)

            list_count = self.db.cur_e.execute_select(sql_char=sql_char)
            for row in list_count:
                (count,) = row
                print("count_table=", count)

            if count==count_table_fibonacci_number:
                c_count = True
            else:
                c_count = False
                break

        return c_count
