__author__ = 'vden'

class Mbt_hosts:

    def __init__(self, host=None, superuser=None, superuser_password=None, user=None, password=None, database=None,
                 port=None, write=None, read=None):
        self.host = host
        self.superuser = superuser
        self.superuser_password = superuser_password
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.write = write
        self.read = read


    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.host, self.superuser, self.superuser_password, self.user,
                                               self.password, self.database, self.port, self.write, self.read)
