__author__ = 'vden'

class Check_list_tables:

    def __init__(self, table_name=None):
        self.table_name = table_name


    def __repr__(self):
        return "%s" % (self.table_name,)

    def __eq__(self, other):
        return (self.table_name==other.table_name)
