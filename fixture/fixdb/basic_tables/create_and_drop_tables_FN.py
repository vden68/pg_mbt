__author__ = 'vden'

import allure


count_table_fibonacci_number = 0
table_fibonacci_number_name = None

class CreateAndDropTablesFnHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        tablename='fibonacci_number_'+self.db.app.mbt_conn.test_uuid
        self.db.fibonacci_number.create_table(table_name=tablename)
        return tablename
