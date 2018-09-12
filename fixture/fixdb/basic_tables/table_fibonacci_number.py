__author__ = 'vden'

import time
import pytest

from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

#list_table_fibonacci_number = []
count_table_fibonacci_number = 0

class Table_fibonacci_numberHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        if self.db.initdb.check_tablename(tablename='fibonacci_number_'+self.db.app.mbt_conn.test_uuid) :
            print(("table '%s' already created") % 'fibonacci_number')
        else:
            print(("table '%s' no created") % 'fibonacci_number')

            list_sql_char = []

            list_sql_char.append("begin;")

            list_sql_char.append(("""
                     create table fibonacci_number_{test_uuid}
                     (id         serial not null
                                constraint fibonacci_number_{test_uuid}_pkey
                                primary key,
                     fib_number bigint);
                     """) .format(test_uuid=self.db.app.mbt_conn.test_uuid)
                                 )

            list_sql_char.append('commit;')

            with pytest.allure.step('DDL=%s' % list_sql_char):
                list_row = self.db.cur_e.execute_ddl(list_sql_char=list_sql_char)


    @pytest.allure.step('insert in table "fibonacci_number"')
    def insert(self, list_table_fibonacci_numbers=None, commit=True):
        global list_table_fibonacci_number
        global count_table_fibonacci_number

        list_sql_char=[]

        list_sql_char.append("begin;")
        sql_char=(("""insert into fibonacci_number_{test_uuid}
                             (fib_number) VALUES""").format(test_uuid=self.db.app.mbt_conn.test_uuid))

        for fib_n in list_table_fibonacci_numbers:
            sql_char+=("""
                       ({fib_number}),""").format (fib_number=fib_n.fib_number)
        sql_char=sql_char[:-1]+" RETURNING id ;"

        list_sql_char.append(sql_char)

        if commit==True:
            list_sql_char.append('commit;')

            with pytest.allure.step('insert plus commit  SQL=%s' % list_sql_char):
                list_row = self.db.cur_e.execute_insert(list_sql_char=list_sql_char)

            count_table_fibonacci_number+=len(list_table_fibonacci_numbers)

        else:

            list_sql_char.append('rollback;')

            with pytest.allure.step('insert plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_insert(list_sql_char=list_sql_char)


    #def get_list(self):
        #global list_table_fibonacci_number
        #return list_table_fibonacci_number


    @pytest.allure.step('check count')
    def check_count(self):
        c_count = False
        global count_table_fibonacci_number

        sql_char = ("""
                                select
                                  count (id)
                                from
                                  fibonacci_number_{test_uuid}
                                                   ;
                                """).format(test_uuid=self.db.app.mbt_conn.test_uuid)
        # print('sql_char=', sql_char)

        for x in range(10):

            if x > 1:
                time.sleep(2)

            list_count_node_id = []
            for selected_node in self.db.app.mbt_hosts_read:

                with pytest.allure.step('get the number of rows  SQL=%s' % sql_char):
                    list_count = self.db.cur_e.execute_select(sql_char=sql_char, selected_node=selected_node)

                    if list_count is not None:
                        for row in list_count:
                            (count,) = row
                        print("count_table_fibonacci_number=", count_table_fibonacci_number ,"node_id=",selected_node.node_id  ,"count=", count)
                        list_count_node_id.append(count)
                    else:
                        print("node_id=", selected_node.node_id, "count=", None)
                        list_count_node_id.append(None)


            print("list_count_node_id=", list_count_node_id)

            for count_node_id in list_count_node_id:
                if not (count_node_id==count_table_fibonacci_number or count_node_id is None):
                    break
            else:
                c_count=True
                break

        return  c_count


    @pytest.allure.step('check records')
    def check_records(self):

        global count_table_fibonacci_number
        if count_table_fibonacci_number<100:
            c_limit=count_table_fibonacci_number//10+2
        elif count_table_fibonacci_number<1000:
            c_limit = count_table_fibonacci_number//10
        elif count_table_fibonacci_number<10000:
            c_limit = count_table_fibonacci_number//20
        elif count_table_fibonacci_number<100000:
            c_limit = count_table_fibonacci_number//40
        else:
            c_limit = 3000




        sql_char = ("""
                                        select
                                          id,
                                          fib_number
                                        from
                                          fibonacci_number_{test_uuid}
                                        ORDER BY RANDOM()
                                        LIMIT {climit}                                                           ;
                                        ;""").format(test_uuid=self.db.app.mbt_conn.test_uuid, climit=c_limit)
        print('sql_char=', sql_char)

        for x in range(10):

            if x > 1:
                time.sleep(2)

            with pytest.allure.step('get row records for verification  SQL=%s' % sql_char):
                list_row = self.db.cur_e.execute_select(sql_char=sql_char)

            list_row_records_for_verification = []
            if list_row is not None:
                for row in list_row:
                    (id, fib_number,) = row
                    list_row_records_for_verification.append(Table_fibonacci_number(id=id, fib_number=fib_number))
                break

        list_row_records_for_verification=sorted(list_row_records_for_verification, key=lambda x: x.id)
        print("list_row_records_for_verification=", list_row_records_for_verification)

        sql_char = ("""select
                          fib.id,
                          fib.fib_number
                        from
                          fibonacci_number_{test_uuid} AS fib
                        ORDER BY fib.id
                        WHERE 
                          fib.id IN (""").format(test_uuid=self.db.app.mbt_conn.test_uuid)









        return True

