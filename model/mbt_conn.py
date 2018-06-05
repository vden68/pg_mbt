__author__ = 'vden'

class Mbt_conn:

    def __init__(self, superuser=None, superuser_password=None, user=None, password=None, database=None):
        self.superuser = superuser
        self.superuser_password = superuser_password
        self.user = user
        self.password = password
        self.database = database


    def __repr__(self):
        return "%s,%s,%s,%s,%s" % (self.superuser, self.superuser_password, self.user, self.password, self.database)
