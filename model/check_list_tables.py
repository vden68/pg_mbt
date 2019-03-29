__author__ = 'vden'

class Check_list_tables:

    def __init__(self, table_name=None, count_rows=None, table_md5=None):
        self.table_name = table_name
        self.count_rows = count_rows
        self.table_md5 = table_md5


    def __repr__(self):
        return "%s,%s,%s" % (self.table_name, self.count_rows, self.table_md5)

    def __eq__(self, other):
        return (self.table_name==other.table_name and self.count_rows==other.count_rows and
                self.table_md5==other.table_md5)
