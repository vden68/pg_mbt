__author__ = 'vden'

class Mbt_hosts:

    def __init__(self, host=None, user=None, password=None, database=None, port=None, type=None):
        self.host = host
        self.user= user
        self.password= password
        self.database= database
        self.port= port
        self.type= type


    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.host, self.user, self.password, self.database, self.port, self.type)
