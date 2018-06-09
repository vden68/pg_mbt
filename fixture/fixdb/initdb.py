__author__ = 'vden'



class InitdbHelper():

    def __init__(self, db):
        self.db = db


    def check_db(self, x_datname, x_rolname):
        conn = self.db.conn.db_superuser()

        sql_char =( """
            select
              db.datname,
              rol.rolname
            from
              pg_database as db ,
              pg_roles as rol
            where
              rol.OID=db.datdba and
              rol.rolname= '%s' and
              db.datname='%s'
            ;
            """)%(x_rolname, x_datname)

        #print('sql_char=', sql_char)

        cursor = self.db.cur_e.cursor_execute(conn=conn, sql_char=sql_char)
        datname, rolname = None, None
        for row in cursor:
            (datname, rolname) = row
            print('datname=', datname)
            print('rolname=', rolname)


        cursor.close()
        conn.close()

        if datname is None and rolname is None:
            return False
        else:
            return True


    def create_db(self, datname=None, rolname=None):
        if datname is None:
            datname=self.db.app.mbt_conn.database
        if rolname is None:
            rolname=self.db.app.mbt_conn.user

        if self.check_db(x_rolname=rolname,x_datname=datname):
            print(("database %s already created") % datname)
        else:
            pass

    def check_tablename(self, tablename=None):
        print('check_tablename')
        conn = self.db.conn.db_read()

        sql_char = ("""
        SELECT
          tablename
        FROM
          pg_tables
        where
          tablename = '%s'
        ;""")%tablename

        print('sql_char=', sql_char)
        cursor = self.db.cur_e.cursor_execute(conn=conn, sql_char=sql_char)
        x_tablename = None
        for row in cursor:
            (x_tablename) = row
            print('tablename=', x_tablename)

        cursor.close()
        conn.close()

        if x_tablename is None :
            return False
        else:
            return True









