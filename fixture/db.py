__author__ = 'vden'


from fixture.fixdb.connect import ConnectHelper
from fixture.fixdb.initdb import InitdbHelper
from fixture.fixdb.cursor_execute import CursorExecuteHelper
from fixture.fixdb.basic_tables.table_fibonacci_number import Table_fibonacci_numberHelper
from fixture.fixdb.basic_tables.table_points_index_gist import Table_points_index_gistHelper
from fixture.fixdb.basic_tables.sql_ddl import Sql_ddlHelper
from fixture.fixdb.basic_tables.create_and_drop_tables_FN import CreateAndDropTablesFnHelper
from fixture.fixdb.table_check import TableCheckHelper
from fixture.fixdb.table_mbt_random import TableMbtRandomHelper
from fixture.fixdb.common.fibonacci_number import FibonacciNumberHelper
from fixture.fixdb.extension.pg_pathman.table_fn_pg_pathman_hash import TableFNPg_pathmanHashHelper
from fixture.fixdb.extension.pg_pathman.table_fn_pg_pathman_range_id import TableFNPg_pathmanRangeIdHelper
from fixture.fixdb.extension.autonomous_transactions.table_fn_autonomous_transactions_in_one_table import \
    TableFnAutonomousTransactionsInOneTableHelper
from fixture.fixdb.finishing_checks.finishing_checks import FinishingChecklHelper




class Dbfixture:

    def __init__(self, app, generator ):
        self.app = app
        self.generator = generator

        self.conn = ConnectHelper(self)
        self.initdb = InitdbHelper(self)
        self.cur_e = CursorExecuteHelper(self)
        self.table_check = TableCheckHelper(self)
        self.mbt_random = TableMbtRandomHelper(self)

        #basic tables
        self.table_fibonacci_number=Table_fibonacci_numberHelper(self)
        self.table_points_index_gist=Table_points_index_gistHelper(self)
        self.create_and_drop_tables_FN=CreateAndDropTablesFnHelper(self)
        self.sql_ddl=Sql_ddlHelper(self)

        #common
        self.fibonacci_number=FibonacciNumberHelper(self)

        #extension
        self.fn_pg_pathman_hash=TableFNPg_pathmanHashHelper(self)
        self.fn_pg_pathman_range_id=TableFNPg_pathmanRangeIdHelper(self)
        self.fn_autonomous_transactions_in_one_table=TableFnAutonomousTransactionsInOneTableHelper(self)

        #finishing_checks
        self.finishing_checks=FinishingChecklHelper(self)



        self.initdb.create_db()
        #self.table_fibonacci_number.create_table()
        #self.table_points_index_gist.create_table()
        self.mbt_random.create_table()




    def destroy(self):
        self.conn.all_close_conn()



