__author__ = 'vden'

class Mbt_conn:

    def __init__(self, superuser=None, superuser_password=None, user=None, password=None, database=None,
                 test_start_timestamp=None, test_uuid=None, cycle_factor=None):
        self.superuser = superuser
        self.superuser_password = superuser_password
        self.user = user
        self.password = password
        self.database = database
        self.test_start_timestamp = test_start_timestamp
        self.test_uuid = test_uuid
        self.cycle_factor = cycle_factor


    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.superuser, self.superuser_password, self.user, self.password, self.database,
                                      self.test_start_timestamp, self.test_start_timestamp, self.test_uuid,self. cycle_factor)
