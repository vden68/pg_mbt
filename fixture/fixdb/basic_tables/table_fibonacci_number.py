__author__ = 'vden'



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