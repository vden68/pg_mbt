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

    @allure.step('drop empty tables in quantities ')
    def drop_tables_empty(self):
        global count_tables_fibonacci_number_empty
        global list_tables_fibonacci_number_empty

        self.db.fibonacci_number.drop_tables(list_table_name=list_tables_fibonacci_number_empty)

        count_tables_fibonacci_number_empty=0
        list_tables_fibonacci_number_empty=[]

    @allure.step('drop_tables_empty_one_by_one ')
    def drop_tables_empty_one_by_one(self):
        global count_tables_fibonacci_number_empty
        global list_tables_fibonacci_number_empty

        for name_table in list_tables_fibonacci_number_empty:
            List_name_table=[]
            List_name_table.append(name_table)
            self.db.fibonacci_number.drop_tables(list_table_name=List_name_table)

        count_tables_fibonacci_number_empty = 0
        list_tables_fibonacci_number_empty = []

    def get_count_tables_fibonacci_number_empty(self):
        global count_tables_fibonacci_number_empty

        return count_tables_fibonacci_number_empty

    def get_list_tables_fibonacci_number_empty(self):
        global list_tables_fibonacci_number_empty
        return list_tables_fibonacci_number_empty






