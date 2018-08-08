__author__ = 'vden'

import psycopg2
import random
import time



class ConnectHelper():


    def __init__(self, db):
        self.db = db


    def connection(self, host=None, port=None, dbname=None, user=None, password=None):
        conn = None

        conn_string = "host="+host+" port="+port+" dbname="+dbname+" user="+user+" password="+password
        #print("Connecting to database\n	->%s" % (conn_string))


        try:
            conn = psycopg2.connect(conn_string)
        except :
            if conn:
                conn.close()
            conn = None
            print("I am unable to connect to the database ->%s %s %s %s" % (host, dbname, user, password))


        return conn

    def db_superuser(self):
        conn = None
        x = 0
        while (conn is None) :
            if x>0:
                time.sleep(1)
            db_host=random.choice(self.db.app.mbt_hosts_write)
            conn=self.connection(host=db_host.host, port=db_host.port, dbname="postgres",
                                 user=self.db.app.mbt_conn.superuser, password=self.db.app.mbt_conn.superuser_password)
            #print(db_host, x)

            x=x+1
            if x>60:
                print('Could not connect to conn.db_postgres')
                exit(1)

        return conn



    def db_write(self):
        conn = None
        x = 0
        while (conn is None):
            if x > 0:
                time.sleep(1)
            db_host = random.choice(self.db.app.mbt_hosts_write)
            conn = self.connection(host=db_host.host, port=db_host.port, dbname=self.db.app.mbt_conn.database,
                                   user=self.db.app.mbt_conn.user, password=self.db.app.mbt_conn.password)
            #print(db_host, x)

            x = x + 1
            if x > 60:
                print('Could not connect to conn.db_postgres')
                exit(1)

        return conn


    def db_read(self):
        conn = None
        x = 0
        while (conn is None):
            if x > 0:
                print("x=", x)
                time.sleep(1)
            db_host = random.choice(self.db.app.mbt_hosts_read)
            conn = self.connection(host=db_host.host, port=db_host.port, dbname=self.db.app.mbt_conn.database,
                                   user=self.db.app.mbt_conn.user, password=self.db.app.mbt_conn.password)
            #print(db_host, x)

            x = x + 1
            if x > 60:
                print('Could not connect to conn.db_postgres')
                exit(1)

        return conn






