__author__ = 'vden'

import time
import pytest

from model.basic_tables.check_table_fibonacci_number import Check_table_fibonacci_number


class FibonacciNumberHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self, table_name=None):

        if self.db.initdb.check_tablename(tablename=table_name) :
            print(("table '%s' already created") % table_name)
        else:
            print(("table '%s' no created") % table_name)

            list_sql_char = []

            list_sql_char.append("BEGIN;")

            list_sql_char.append(("""
                     CREATE TABLE {tablename}
                     (id         serial not null
                                constraint {tablename}_pkey
                                primary key,
                     fib_number bigint not null);
                     """) .format(tablename=table_name)
                                 )

            list_sql_char.append(("""
                CREATE  INDEX  {tablename}_column_fib_number ON {tablename}(fib_number)
                ;""") .format(tablename=table_name))

            list_sql_char.append('COMMIT;')

            with pytest.allure.step('DDL=%s' % list_sql_char):
                self.db.cur_e.execute_ddl(list_sql_char=list_sql_char)


    def insert(self, list_table_fibonacci_numbers=None, commit=True, table_name=None):

        list_sql_char=[]

        list_sql_char.append("BEGIN;")
        sql_char=(("""INSERT INTO {tablename}(fib_number) VALUES""").format(tablename=table_name))

        for fib_n in list_table_fibonacci_numbers:
            sql_char+=("""
                       ({fib_number}),""").format (fib_number=fib_n.fib_number)
        sql_char=sql_char[:-1]+" RETURNING id ;"

        list_sql_char.append(sql_char)

        if commit==True:
            list_sql_char.append('COMMIT;')

            with pytest.allure.step('insert plus commit  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_insert(list_sql_char=list_sql_char)

        else:

            list_sql_char.append('ROLLBACK;')

            with pytest.allure.step('insert plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_insert(list_sql_char=list_sql_char)

    def triple_autonomous_transactions_insert(self, list_table_fibonacci_numbers = None, commit = True,
                                              commit_autonomous_transactions = True, table_name = None ):
        list_sql_char=[]

        list_sql_char.append("BEGIN;")

        sql_char=(("""INSERT INTO {tablename}(fib_number) VALUES""").format(tablename=table_name))
        for fib_n in list_table_fibonacci_numbers:
            sql_char+=("""
                       ({fib_number}),""").format (fib_number=fib_n.fib_number)
        sql_char=sql_char[:-1]+" RETURNING id ;"
        list_sql_char.append(sql_char)

        list_sql_char.append("BEGIN AUTONOMOUS TRANSACTION;")
        list_sql_char.append(sql_char)
        if commit_autonomous_transactions:
            list_sql_char.append('COMMIT AUTONOMOUS TRANSACTION;')
        else:
            list_sql_char.append('ROLLBACK AUTONOMOUS TRANSACTION;')

        list_sql_char.append(sql_char)
        if commit==True:
            list_sql_char.append('COMMIT;')
        else:
            list_sql_char.append('ROLLBACK;')

        with pytest.allure.step('insert SQL=%s' % list_sql_char):
            self.db.cur_e.execute_insert(list_sql_char=list_sql_char)




    @pytest.allure.step('check records')
    def check_records(self, table_name=None):

        sql_char = ("""
        SELECT
           fib_number,
           count(*)
         FROM
           {tablename}
         GROUP BY
           fib_number
         ORDER BY
           fib_number
        ;""").format(tablename=table_name)

        for x in range(10):

            if x > 1:
                time.sleep(2)

            with pytest.allure.step('get row records for verification  SQL=%s' % sql_char):
                list_row = self.db.cur_e.execute_select(sql_char=sql_char)

            list_row_records_for_verification = []
            if list_row is not None:
                for row in list_row:
                    (fib_number, count,) = row
                    list_row_records_for_verification.append(Check_table_fibonacci_number(fib_number=fib_number, count=count))
                break

        for selected_node in self.db.app.mbt_hosts_read:

            with pytest.allure.step('get the number of rows  SQL=%s' % sql_char):
                list_row = self.db.cur_e.execute_select(sql_char=sql_char, selected_node=selected_node)
                list_row2 = []

                if list_row is not None:
                    for row in list_row:
                        (fib_number, count,) = row
                        list_row2.append(Check_table_fibonacci_number(fib_number=fib_number, count=count))

                    assert list_row_records_for_verification==list_row2
                    print("node_id=", selected_node.node_id, True)
                else:
                    print("node_id=", selected_node.node_id, None)

        return True



    @pytest.allure.step('update in table "fibonacci_number"')
    def update_id_random(self, c_limit=1, table_name=None, commit=True):

        list_sql_char = []

        list_sql_char.append("BEGIN;")
        sql_char = (("""WITH sub AS (SELECT id  FROM {tablename}
                                     ORDER BY RANDOM()
                                     LIMIT {m_limit})
                        UPDATE 
                          {tablename} AS f
                        SET 
                          fib_number = (SELECT m.fib_number FROM mbt_random AS m
                        WHERE m.id<> f.id
                        ORDER BY  RANDOM()
                        LIMIT 1)        
                        WHERE 
                          f.id IN (SELECT id  FROM sub)
                         ;""").format(tablename=table_name, m_limit=c_limit))

        list_sql_char.append(sql_char)

        if commit == True:
            list_sql_char.append('COMMIT;')

            with pytest.allure.step('update plus commit  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)

        else:

            list_sql_char.append('ROLLBACK;')

            with pytest.allure.step('update plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)


    @pytest.allure.step('delete 2 percent of rows "fibonacci_number"')
    def delete_2_percent_of_rows(self, c_limit=1, table_name=None, commit=True):

        list_sql_char = []

        list_sql_char.append("BEGIN;")
        sql_char = (("""
        WITH sub AS (SELECT id  FROM {tablename}
                    ORDER BY RANDOM()
                      LIMIT {m_limit})
        DELETE FROM {tablename}
          WHERE
            id IN (SELECT id  FROM sub)
        ;
        """).format(tablename=table_name, m_limit=c_limit))
        print('sql_char=', sql_char)

        list_sql_char.append(sql_char)

        if commit == True:
            list_sql_char.append('COMMIT;')

            with pytest.allure.step('update plus commit  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)
        else:

            list_sql_char.append('ROLLBACK;')

            with pytest.allure.step('update plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)





