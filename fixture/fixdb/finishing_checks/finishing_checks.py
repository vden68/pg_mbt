__author__ = 'vden'


import allure

class FinishingChecklHelper():

    def __init__(self, db):
        self.db = db

    @allure.step('create table {0}')
    def create_table(self, tablename=None, column_names_and_type=None):

        if self.db.initdb.check_tablename(tablename=tablename):
            print(("table '%s' already created") % tablename)
        else:
            print(("table '%s' not created") % tablename)

            conn = self.db.conn.db_write()

            sql_char = ("""
                  create table {tablename_t}
                    (
                       id         serial not null
                                  constraint {tablename_t}_pkey
                                  primary key,""").format(tablename_t=tablename)

            for column_name_and_type in column_names_and_type:
                sql_char +=("""
                        {column_name_c} ,""").format(column_name_c=column_name_and_type)


            sql_char+=("""             
                        test_start_timestamp timestamp                        
                     );

                    create unique index {tablename_t}_id_uindex
                       on {tablename_t} (id);
                       
                    create index {tablename_t}_test_start_timestamp_index
                        on {tablename_t} (test_start_timestamp desc); 
                        
                    commit ;
                       """).format(tablename_t=tablename)


            print('sql_char=', sql_char)


            cursor = self.db.cur_e.cursor_execute(conn=conn, sql_char=sql_char)

            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

