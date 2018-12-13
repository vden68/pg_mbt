__author__ = 'vden'

import pytest


count_table_fibonacci_number = 0
table_fibonacci_number_name = None

class Table_fibonacci_numberHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        tablename='fibonacci_number_'+self.db.app.mbt_conn.test_uuid
        self.db.fibonacci_number.create_table(table_name=tablename)
        return tablename



    @pytest.allure.step('insert in table "fibonacci_number"')
    def insert(self, list_table_fibonacci_numbers=None, commit=True):
        global count_table_fibonacci_number
        global table_fibonacci_number_name
        if table_fibonacci_number_name is None:
            table_fibonacci_number_name = self.create_table()

        tablename = table_fibonacci_number_name
        self.db.fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers,
                                        commit=commit, table_name=tablename)
        if commit==True:
            count_table_fibonacci_number+=len(list_table_fibonacci_numbers)

    @pytest.allure.step('check count')
    def check_count(self):
        global count_table_fibonacci_number
        global table_fibonacci_number_name
        tablename = table_fibonacci_number_name
        c_count = self.db.table_check.check_count(count_rows_table=count_table_fibonacci_number, table_name=tablename)
        return  c_count


    @pytest.allure.step('check records')
    def check_records(self):
        global table_fibonacci_number_name
        tablename = table_fibonacci_number_name
        check_records_c = self.db.fibonacci_number.check_records(table_name=tablename)
        return check_records_c



    @pytest.allure.step('update in table "fibonacci_number"')
    def update_id_random(self, commit=True):
        global count_table_fibonacci_number
        c_limit = count_table_fibonacci_number // 10 + 1

        if c_limit>10000:
            c_limit=10000

        global table_fn_pg_pathman_hash_name
        tablename = table_fibonacci_number_name
        self.db.fibonacci_number.update_id_random(c_limit=c_limit, table_name=tablename, commit=commit)


    def get_count_table_fibonacci_number(self):
        global count_table_fibonacci_number
        return count_table_fibonacci_number

    @pytest.allure.step('delete 10 percent of rows "fibonacci_number"')
    def delete_2_percent_of_rows(self, commit=True):
        global count_table_fibonacci_number
        c_limit = count_table_fibonacci_number // 50 + 1

        global table_fibonacci_number_name
        tablename = table_fibonacci_number_name
        self.db.fibonacci_number.delete_2_percent_of_rows(c_limit=c_limit, table_name=tablename, commit=commit)

        if commit == True:
            count_table_fibonacci_number-=c_limit
