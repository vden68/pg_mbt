__author__ = 'vden'

from fixture.fixdb.connect import ConnectHelper
from fixture.fixdb.initdb import InitdbHelper
from fixture.fixdb.cursor_execute import CursorExecuteHelper
from fixture.fixdb.basic_tables.table_fibonacci_number import Table_fibonacci_numberHelper
from fixture.fixdb.basic_tables.sql_ddl import Sql_ddlHelper



class Dbfixture:

    def __init__(self, app):
        self.app = app

        self.conn = ConnectHelper(self)
        self.initdb = InitdbHelper(self)
        self.cur_e = CursorExecuteHelper(self)

        #basic tables
        self.table_fibonacci_number=Table_fibonacci_numberHelper(self)
        self.sql_ddl=Sql_ddlHelper(self)



        self.initdb.create_db()
        self.table_fibonacci_number.create_table()




    def destroy(self):
        self.conn.all_close_conn()



