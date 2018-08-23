__author__ = 'vden'

import psycopg2
import random
import time

conn_node1=None
conn_node2=None
conn_node3=None
conn_node4=None
conn_node5=None

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



    def db_write(self, selected_node=None):

        if selected_node is None:
            selected_node = random.choice(self.db.app.mbt_hosts_write)

        conn=self.get_conn_node(selected_node)

        return conn


    def db_read(self, selected_node=None):
        if selected_node is None:
            selected_node = random.choice(self.db.app.mbt_hosts_read)

        conn=self.get_conn_node(selected_node)

        return conn



    def get_conn_node(self, selected_node):

        global conn_node1
        global conn_node2
        global conn_node3
        global conn_node4
        global conn_node5

        if selected_node.node_id==1:
            if conn_node1 is None:
                conn_node1=self.connection(host=selected_node.host, port=selected_node.port,
                                           dbname=self.db.app.mbt_conn.database, user=self.db.app.mbt_conn.user,
                                           password=self.db.app.mbt_conn.password)
            return conn_node1

        elif selected_node.node_id==2:
            if conn_node2 is None:
                conn_node2 = self.connection(host=selected_node.host, port=selected_node.port,
                                             dbname=self.db.app.mbt_conn.database, user=self.db.app.mbt_conn.user,
                                             password=self.db.app.mbt_conn.password)
            return conn_node2

        elif selected_node.node_id==3:
            if conn_node3 is None:
                conn_node3 = self.connection(host=selected_node.host, port=selected_node.port,
                                             dbname=self.db.app.mbt_conn.database, user=self.db.app.mbt_conn.user,
                                             password=self.db.app.mbt_conn.password)
            return conn_node3

        elif selected_node.node_id==4:
            if conn_node4 is None:
                conn_node4 = self.connection(host=selected_node.host, port=selected_node.port,
                                             dbname=self.db.app.mbt_conn.database, user=self.db.app.mbt_conn.user,
                                             password=self.db.app.mbt_conn.password)
            return conn_node4

        elif selected_node.node_id==5:
            if conn_node5 is None:
                conn_node5 = self.connection(host=selected_node.host, port=selected_node.port,
                                             dbname=self.db.app.mbt_conn.database, user=self.db.app.mbt_conn.user,
                                             password=self.db.app.mbt_conn.password)
            return conn_node5







    def all_close_conn(self):

        global conn_node1
        global conn_node2
        global conn_node3
        global conn_node4
        global conn_node5

        if conn_node1 is not None:
            conn_node1.close()
            conn_node1 = None
            print("conn_node1 close")
        if conn_node2 is not None:
            conn_node2.close()
            conn_node2 = None
            print("conn_node2 close")
        if conn_node3 is not None:
            conn_node3.close()
            conn_node3 = None
            print("conn_node3 close")
        if conn_node4 is not None:
            conn_node4.close()
            conn_node4 = None
            print("conn_node4 close")
        if conn_node5 is not None:
            conn_node5.close()
            conn_node5 = None
            print("conn_node5 close")









