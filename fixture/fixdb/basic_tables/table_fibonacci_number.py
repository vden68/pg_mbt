__author__ = 'vden'

import time
import pytest

from model.basic_tables.table_fibonacci_number import Table_fibonacci_number
from model.basic_tables.check_table_fibonacci_number import Check_table_fibonacci_number

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
        self.checking_completion_of_all_locks()

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
        SELECT
           fib_number,
           count(*)
         FROM
           fibonacci_number_{test_uuid}
         GROUP BY
           fib_number
         ORDER BY
           fib_number
        ;""").format(test_uuid=self.db.app.mbt_conn.test_uuid)

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

        #list_row_records_for_verification=sorted(list_row_records_for_verification, key=lambda x: x.id)


        for selected_node in self.db.app.mbt_hosts_read:

            with pytest.allure.step('get the number of rows  SQL=%s' % sql_char):
                list_row = self.db.cur_e.execute_select(sql_char=sql_char, selected_node=selected_node)
                list_row2 = []

                if list_row is not None:
                    for row in list_row:
                        (fib_number, count,) = row
                        list_row2.append(Check_table_fibonacci_number(fib_number=fib_number, count=count))

                    #print('list_row_records_for_verification=' , list_row_records_for_verification)
                    #print('list_row2=', list_row2)
                    assert list_row_records_for_verification==list_row2
                    print("node_id=", selected_node.node_id, True)
                else:
                    print("node_id=", selected_node.node_id, None)

        return True



    @pytest.allure.step('update in table "fibonacci_number"')
    def update_id_more_than_number(self, number_write=0,number_id=0 , commit=True):

        list_sql_char = []

        list_sql_char.append("BEGIN;")
        sql_char = (("""UPDATE 
                          fibonacci_number_{test_uuid}
                        SET 
                          fib_number = {m_number_write}
                        WHERE 
                          id > {m_number_id} 
                        ;
                          """).format(test_uuid=self.db.app.mbt_conn.test_uuid,
                                      m_number_write=number_write, m_number_id=number_id))

        list_sql_char.append(sql_char)

        if commit == True:
            list_sql_char.append('commit;')

            with pytest.allure.step('update plus commit  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)

        else:

            list_sql_char.append('rollback;')

            with pytest.allure.step('update plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)


    def get_count_table_fibonacci_number(self):
        global count_table_fibonacci_number
        return count_table_fibonacci_number


    def checking_completion_of_all_locks(self):

        list_sql_char = []

        list_sql_char.append("BEGIN;")

        sql_char = ("""SELECT
                            count(c.relname)
                         FROM
                           pg_locks AS l
                           LEFT JOIN pg_class AS c ON l.relation = c.oid
                         WHERE
                           relname='fibonacci_number_{test_uuid}'
                         ;
                        """).format(test_uuid=self.db.app.mbt_conn.test_uuid)
        list_sql_char.append(sql_char)
        list_sql_char.append('commit;')

        print('sql_char=' , sql_char)


        for selected_node in self.db.app.mbt_hosts_read:

            count_lock=10
            count2=0
            while count_lock!=0:


                with pytest.allure.step('Checking completion of all locks  SQL=%s' % sql_char):
                    list_count = self.db.cur_e.execute_select_list(list_sql_char=list_sql_char, selected_node=selected_node)

                    if list_count is not None:
                        for row in list_count:
                            (count_lock,) = row

                    if count2>1:
                        time.sleep(1)

                    if count2>40:
                        break

                    count2+=1
                    print('selected_node=', selected_node,  "count_lock=", count_lock)


    @pytest.allure.step('delete 10 percent of rows "fibonacci_number"')
    def delete_10_percent_of_rows(self, commit=True):

        global count_table_fibonacci_number
        c_limit = count_table_fibonacci_number // 10 + 1

        list_sql_char = []

        list_sql_char.append("BEGIN;")
        sql_char = (("""
        DELETE FROM fibonacci_number_{test_uuid}
          WHERE
            id IN (SELECT id  FROM fibonacci_number_{test_uuid}
                    ORDER BY RANDOM()
                      LIMIT {m_limit})
        ;
        """).format(test_uuid=self.db.app.mbt_conn.test_uuid, m_limit=c_limit))

        list_sql_char.append(sql_char)

        if commit == True:
            list_sql_char.append('commit;')

            with pytest.allure.step('update plus commit  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)
                count_table_fibonacci_number=count_table_fibonacci_number-c_limit
                print('c_limit=', c_limit)

        else:

            list_sql_char.append('rollback;')

            with pytest.allure.step('update plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)





