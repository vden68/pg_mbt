__author__ = 'vden'

from fixture.fixdb.connect import ConnectHelper
from fixture.fixdb.initdb import InitdbHelper
from fixture.fixdb.cursor_execute import CursorExecuteHelper



class Dbfixture:

    def __init__(self, app):

        self.conn = ConnectHelper(self)
        self.initdb = InitdbHelper(self)
        self.cur_e = CursorExecuteHelper(self)

        self.app = app

        self.initdb.create_db()




    def destroy(self):
        pass
        #self.connection.close()



