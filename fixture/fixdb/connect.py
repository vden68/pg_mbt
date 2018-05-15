# -*- coding: utf-8 -*-
__author__ = 'vden'
import psycopg2



class ConnectHelper():


    def __init__(self, db):
        self.db = db


    def connection(self, host=None, port=None, dbname=None, user=None, password=None):
        conn = None

        conn_string = "Проверка"#"host="+host+" host="+port+" dbname="+dbname+" user="+user+" password="+password
        print("Connecting to database\n	->%s" % (conn_string))
        print(self.db.mbt_hosts_write, self.db.mbt_hosts_read)

        """

        try:
            conn = psycopg2.connect(conn_string)
        except :
            if conn:
                conn.rollback()
                conn.close()
            print("I am unable to connect to the database ->%s %s %s %s" % (host, port, dbname, user, password))
        """

        return conn

    def con_db_postgres(app, db):
        db_write = app.mbt_mbt_hosts
        print(db_write)
        conn=db.conn.connection()
        print(conn)


    """

    def tfp_execute(app, str_ex, conn):

        try:
            cur= conn.cursor()
            cur.execute(str_ex)
            print(time.ctime()[11:-5], str_ex)
            #rows = cur.fetchone()
            #for row in rows:
            #    print(row)
            conn.commit()
        except psycopg2.DatabaseError:
            if conn:
                conn.rollback()

            print("Error " )

        return cur
    """







