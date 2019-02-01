__author__ = 'vden'
import time
import allure



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
                    #cursor.executescript(sql_char)
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
                    self.db.conn.all_close_conn()

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

    allure.step('get row records for verification  SQL="{sql_char}", node="{selected_node}"' )
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
                self.db.conn.all_close_conn()


            if len(list_row)>0:
                break

        else:
            list_row=None

        return list_row


    def execute_ddl(self, list_sql_char=None):

        for x in range(10):

            if x > 1:
                time.sleep(2)

            conn = self.db.conn.db_write()
            if conn is None:
                continue

            cursor = conn.cursor()


            for sql_char in list_sql_char:

                try:
                    cursor.execute(sql_char)
                    #cursor.executescript(sql_char)


                except:
                    if cursor:
                        cursor.close()
                    print("no execute %s" % (sql_char))
                    cursor = None
                    self.db.conn.all_close_conn()

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

        return


    def execute_update(self, list_sql_char=None):

        for x in range(10):

            if x > 1:
                time.sleep(2)

            conn = self.db.conn.db_write()
            if conn is None:
                continue

            cursor = conn.cursor()


            for sql_char in list_sql_char:

                try:
                    #print('sql_char=', sql_char)
                    cursor.execute(sql_char)

                except:
                    if cursor:
                        cursor.close()
                    print("no execute %s" % (sql_char))
                    cursor = None
                    self.db.conn.all_close_conn()

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

        return


    def execute_select_list(self, list_sql_char=None, selected_node=None):

        for x in range(10):

            if x > 1:
                time.sleep(2)

            conn = self.db.conn.db_write(selected_node)
            if conn is None:
                continue

            cursor = conn.cursor()

            list_row = []
            for sql_char in list_sql_char:

                try:
                    cursor.execute(sql_char)
                    if cursor.rowcount > 0:
                        results = cursor.fetchall()
                        #print('results=', results)
                        for row in results:
                            (id) = row
                            #print('id=', id)
                            list_row.append(id)
                except:
                    if cursor:
                        cursor.close()
                    print("no execute %s" % (sql_char))
                    cursor = None
                    self.db.conn.all_close_conn()

                if cursor is None:
                    break

            if cursor is not None:
                break

        else:
            print('Could not connect to conn.db_postgres')
            list_row = None
            #exit(1)

        #if cursor:
            #cursor.close()
            #cursor=None

        return list_row



