__author__ = 'vden'

from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

list_table_fibonacci_number = []

class Table_fibonacci_numberHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        if self.db.initdb.check_tablename(tablename='fibonacci_number'):
            print(("table '%s' already created") % 'fibonacci_number')
        else:
            print(("table '%s' no created") % 'fibonacci_number')

            conn = self.db.conn.db_read()

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


            print('sql_char=', sql_char)
            cursor = self.db.cur_e.cursor_execute(conn=conn, sql_char=sql_char)

            cursor.close()
            conn.close()


    def insert(self, fib_number=None, commit=True):
        global list_table_fibonacci_number
        print("insert_commit")
        print('fib_number=', fib_number)

        conn = self.db.conn.db_write()

        sql_char = ("""
                          insert into fibonacci_number
                             (fib_number, test_start_timestamp) VALUES 
                             (%s, '%s') RETURNING id
                          ; 
                               """) %(fib_number, self.db.app.mbt_conn.test_start_timestamp)

        print('sql_char=', sql_char)

        cursor = self.db.cur_e.cursor_execute(conn=conn, sql_char=sql_char)
        print('cursor=', cursor)
        for row in cursor:
            (id,)=row
            print(id)

        if commit:
            cursor = self.db.cur_e.cursor_execute(conn=conn, sql_char='commit;')
            list_table_fibonacci_number.append(Table_fibonacci_number(id=id, fib_number=fib_number,
                                               test_start_timestamp=self.db.app.mbt_conn.test_start_timestamp))
        else:
            pass

        cursor.close()
        conn.close()
        print('list_table_fibonacci_number=', list_table_fibonacci_number)


    def get_list_table_fibonacci_number(self):
        global list_table_fibonacci_number
        return list_table_fibonacci_number

