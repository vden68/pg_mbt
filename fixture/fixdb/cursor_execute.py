__author__ = 'vden'



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

        return cursor



