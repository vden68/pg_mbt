__author__ = 'vden'
import time
import pytest



class CursorExecuteHelper():


    def __init__(self, db):
        self.db = db

    def cursor_execute(self, conn=None, sql_char=None):
        cursor = conn.cursor()
        try:
            cursor.execute(sql_char)
        except :
            if cursor:
                cursor.close()
            print("no execute %s" % (sql_char))
            cursor = None

        return cursor

    def execute_insert(self, list_sql_char=None):
        #list_row=[]
        cursor = None
        x = 0
        while cursor is None:
            if x > 0:
                time.sleep(5)
            conn = self.db.conn.db_write()
            cursor = conn.cursor()
            list_row = []

            for sql_char in list_sql_char:

                try:
                    cursor.execute(sql_char)
                    if cursor.rowcount > 0:
                        results = cursor.fetchall()
                        #print('results=', results)
                        for row in results:
                            #print('row=', row)
                            (id1,) = row
                            id = int(id1)
                            #print('id=', id)
                            list_row.append(id)
                except:
                    if cursor:
                        cursor.close()
                    print("no execute %s" % (sql_char))
                    cursor = None

                if cursor is None:
                    x = x + 1
                    print('x=', x)
                    #if conn is not None:
                        #conn.close()
                    list_row = None

                    if x > 10:
                        print('Could not connect to conn.db_postgres')
                        exit(1)

                    break



            if cursor is not None:
                cursor.close()
            #if conn is not None:
                #conn.close()

        return list_row


    def execute_select(self, sql_char=None):
        check_cursor = None
        x = 0
        while check_cursor is None:
            #if x > 0:
                #time.sleep(5)

            list_row = []

            try:
                conn = self.db.conn.db_read()
                cursor = conn.cursor()
                cursor.execute(sql_char)
                if cursor.rowcount > 0:
                    results = cursor.fetchall()
                    #print('results=', results)
                    for row in results:
                        (id) = row
                        #print('id=', id)
                        list_row.append(id)
                break
            except:
                print("no execute %s" % (sql_char))
                check_cursor = None

            finally:
                if cursor is not None:
                    cursor.close()
                if conn is not None:
                    conn.close()


            if check_cursor is None:
                x = x + 1
                print('x=', x)

                if x > 10:
                    print('Could not connect to conn.db_postgres')
                    exit(1)




        return list_row



    def execute_ddl(self, sql_char=None):
        check_cursor = None
        x = 0
        while check_cursor is None:

            list_row = []

            try:
                conn = self.db.conn.db_read()
                cursor = conn.cursor()
                cursor.execute(sql_char)
                if cursor.rowcount > 0:
                    results = cursor.fetchall()
                    #print('results=', results)
                    for row in results:
                        (id) = row
                        #print('id=', id)
                        list_row.append(id)
                break
            except:
                print("no execute %s" % (sql_char))
                check_cursor = None

            finally:
                if cursor is not None:
                    cursor.close()
                #if conn is not None:
                    #conn.close()


            if check_cursor is None:
                x = x + 1
                print('x=', x)

                if x > 10:
                    print('Could not connect to conn.db_postgres')
                    exit(1)




        return list_row







