__author__ = 'vden'

import pytest


count_table_fn_pg_pathman_hash = 0
table_fn_pg_pathman_hash_name = None

class TableFNPg_pathmanHashHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        tablename='fn_pg_pathman_hash_'+self.db.app.mbt_conn.test_uuid
        self.db.fibonacci_number.create_table(table_name=tablename)
        list_sql_char=[]
        list_sql_char.append("BEGIN;")
        list_sql_char.append (("SELECT create_hash_partitions('%s', 'id', 30);") %(tablename))
        list_sql_char.append("COMMIT;")
        print("list_sql_char=", list_sql_char)
        self.db.cur_e.execute_ddl(list_sql_char=list_sql_char)
        return tablename



    @pytest.allure.step('insert in table "fn_pg_pathman_hash"')
    def insert(self, list_table_fibonacci_numbers=None, commit=True):
        global count_table_fn_pg_pathman_hash
        global table_fn_pg_pathman_hash_name
        if table_fn_pg_pathman_hash_name is None:
            table_fn_pg_pathman_hash_name = self.create_table()

        tablename = table_fn_pg_pathman_hash_name
        self.db.fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers,
                                        commit=commit, table_name=tablename)
        if commit==True:
            count_table_fn_pg_pathman_hash+=len(list_table_fibonacci_numbers)

    @pytest.allure.step('check count')
    def check_count(self):
        global count_table_fn_pg_pathman_hash
        global table_fn_pg_pathman_hash_name
        tablename = table_fn_pg_pathman_hash_name
        c_count = self.db.table_check.check_count(count_rows_table=count_table_fn_pg_pathman_hash, table_name=tablename)
        return  c_count


    @pytest.allure.step('check records')
    def check_records(self):
        global table_fn_pg_pathman_hash_name
        tablename = table_fn_pg_pathman_hash_name
        check_records_c = self.db.fibonacci_number.check_records(table_name=tablename)
        return check_records_c



    @pytest.allure.step('update in table "fn_pg_pathman_hash"')
    def update_id_random(self, commit=True):
        global count_table_fn_pg_pathman_hash
        c_limit = count_table_fn_pg_pathman_hash // 10 + 1

        if c_limit>10000:
            c_limit=10000

        global table_fn_pg_pathman_hash_name
        tablename = table_fn_pg_pathman_hash_name
        self.db.fibonacci_number.update_id_random(c_limit=c_limit, table_name=tablename, commit=commit)


    def get_count_table_fibonacci_number(self):
        global count_table_fn_pg_pathman_hash
        return count_table_fn_pg_pathman_hash

    @pytest.allure.step('delete 2 percent of rows "fn_pg_pathman_hash"')
    def delete_2_percent_of_rows(self, commit=True):
        global count_table_fn_pg_pathman_hash
        c_limit = count_table_fn_pg_pathman_hash // 50 + 1
        print('count_table_fn_pg_pathman_hash=', count_table_fn_pg_pathman_hash)
        print('c_limit=', c_limit)

        global table_fn_pg_pathman_hash_name
        tablename = table_fn_pg_pathman_hash_name
        self.db.fibonacci_number.delete_2_percent_of_rows(c_limit=c_limit, table_name=tablename, commit=commit)

        if commit == True:
            count_table_fn_pg_pathman_hash -= c_limit
