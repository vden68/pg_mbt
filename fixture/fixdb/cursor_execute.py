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

        for x in range(10):

            if x > 1:
                time.sleep(2)

            conn = self.db.conn.db_write()
            if conn is None:
                continue

            cursor = conn.cursor()
            list_row = []

            for sql_char in list_sql_char:

                try:
                    cursor.execute(sql_char)
                    if cursor.rowcount > 0:
                        results = cursor.fetchall()
                        # print('results=', results)
                        for row in results:
                            # print('row=', row)
                            (id1,) = row
                            id = int(id1)
                            # print('id=', id)
                            list_row.append(id)
                except:
                    if cursor:
                        cursor.close()
                    print("no execute %s" % (sql_char))
                    cursor = None

                if cursor is None:
                    break

            if cursor is not None:
                break

        else:
            print('Could not connect to conn.db_postgres')
            exit(1)

        if cursor:
            cursor.close()
            cursor=None

        return list_row




    def execute_select(self, sql_char=None, selected_node=None):

        for x in range(10):

            if x > 1:
                time.sleep(2)

            conn = self.db.conn.db_read(selected_node)
            if conn is None:
                continue

            list_row = []
            try:
                cursor = conn.cursor()
                cursor.execute(sql_char)
                if cursor.rowcount > 0:
                    results = cursor.fetchall()
                    #print('results=', results)
                    for row in results:
                        (id) = row
                        #print('id=', id)
                        list_row.append(id)

            except:
                print("no execute %s" % (sql_char))

            finally:
                if cursor is not None:
                    cursor.close()
                cursor=None

            if len(list_row)>0:
                break

        else:
            list_row=None

        return list_row









        """
        check_cursor = None
        x = 0
        while check_cursor is None:
            #if x > 0:
                #time.sleep(5)

            list_row = []
            cursor=None

            try:
                conn = self.db.conn.db_read(selected_node)
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
        """



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







