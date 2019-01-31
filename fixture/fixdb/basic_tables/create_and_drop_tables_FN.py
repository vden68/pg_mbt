__author__ = 'vden'

import allure


count_tables_fibonacci_number_empty = 0
list_tables_fibonacci_number_empty = []

class CreateAndDropTablesFnHelper():

    def __init__(self, db):
        self.db = db

    @allure.step('create table "{tablename}" ')
    def create_table(self, tablename=None):
        self.db.fibonacci_number.create_table(table_name=tablename)
        return tablename

    def create_tables_loop(self, list_tables=None):
        for tablename in list_tables:
            self.create_table(tablename)

    @allure.step('creating empty tables in quantities "{number_of_tables}" ')
    def create_tables_empty(self, number_of_tables=None):
        global count_tables_fibonacci_number_empty
        global list_tables_fibonacci_number_empty
        tablename = 'fibonacci_number_empty_' + self.db.app.mbt_conn.test_uuid

        for x in range(number_of_tables):
            list_tables_fibonacci_number_empty.append(tablename+'_'+str(x))
            count_tables_fibonacci_number_empty+=1

        self.create_tables_loop(list_tables=list_tables_fibonacci_number_empty)



