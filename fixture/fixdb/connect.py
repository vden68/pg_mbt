# -*- coding: utf-8 -*-
__author__ = 'vden'
import psycopg2
import random
import time



class ConnectHelper():


    def __init__(self, db):
        self.db = db


    def connection(self, host=None, port=None, dbname=None, user=None, password=None):
        conn = None
        #" port="+port+

        conn_string = "host="+host+" port="+port+" dbname="+dbname+" user="+user+" password="+password
        print("Connecting to database\n	->%s" % (conn_string))


        try:
            conn = psycopg2.connect(conn_string)
        except :
            if conn:
                conn.close()
            print("I am unable to connect to the database ->%s %s %s %s" % (host, dbname, user, password))


        return conn

    def db_postgres(self):
        conn = None
        x = 0
        while (conn is None) :
            if x>0:
                time.sleep(5)
            db_host=random.choice(self.db.mbt_hosts_write)
            conn=self.connection(host=db_host.host, port=db_host.port, dbname="postgres", user=db_host.superuser,
                                 password=db_host.superuser_password)
            print(db_host, x)

            x=x+1
            if x>10:
                print('Could not connect to conn.db_postgres')
                exit(1)

        return conn



    def db_write(self):
        conn = None
        x = 0
        while (conn is None):
            if x > 0:
                time.sleep(5)
            db_host = random.choice(self.db.mbt_hosts_write)
            conn = self.connection(host=db_host.host, port=db_host.port, dbname=db_host.database, user=db_host.superuser,
                                   password=db_host.superuser_password)
            print(db_host, x)

            x = x + 1
            if x > 10:
                print('Could not connect to conn.db_postgres')
                exit(1)

        return conn


    def db_read(self):
        pass






