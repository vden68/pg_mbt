__author__ = 'vden'

class Check_list_tables:

    def __init__(self, table_name=None, count_rows=None):
        self.table_name = table_name
        self.count_rows = count_rows


    def __repr__(self):
        return "%s,%s" % (self.table_name, self.count_rows)

    def __eq__(self, other):
        return (self.table_name==other.table_name and self.count_rows==other.count_rows)
