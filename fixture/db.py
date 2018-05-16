__author__ = 'vden'

from fixture.fixdb.connect import ConnectHelper



class Dbfixture:

    def __init__(self, mbt_hosts_write, mbt_hosts_read):
        self.mbt_hosts_write = mbt_hosts_write
        self.mbt_hosts_read = mbt_hosts_read

        self.conn = ConnectHelper(self)




    def destroy(self):
        pass
        #self.connection.close()



