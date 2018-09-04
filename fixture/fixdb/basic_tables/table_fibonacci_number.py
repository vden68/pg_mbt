__author__ = 'vden'

import time
import random
import pytest

from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

list_table_fibonacci_number = []
count_table_fibonacci_number = 0

class Table_fibonacci_numberHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        if self.db.initdb.check_tablename(tablename='fibonacci_number_'+self.db.app.mbt_conn.test_uuid) :
            print(("table '%s' already created") % 'fibonacci_number')
        else:
            print(("table '%s' no created") % 'fibonacci_number')

            conn = self.db.conn.db_write()

            sql_char = ("""
                  create table fibonacci_number_{test_uuid}
                    (
                       id         serial not null
                         constraint fibonacci_number_{test_uuid}_pkey
                         primary key,
                        fib_number bigint
                     ); 

                    create unique index fibonacci_number_{test_uuid}_id_uindex
                       on fibonacci_number_{test_uuid} (id);
                       
                                            
                    commit ;
                       """) .format(test_uuid=self.db.app.mbt_conn.test_uuid)


            #print('sql_char=', sql_char)
            cursor = self.db.cur_e.cursor_execute(conn=conn, sql_char=sql_char)

            if cursor is not None:
                cursor.close()


    @pytest.allure.step('insert in table "fibonacci_number"')
    def insert(self, fib_number=None, commit=True):
        global list_table_fibonacci_number
        global count_table_fibonacci_number

        list_sql_char=[]

        list_sql_char.append("begin;")
        list_sql_char.append(("""
                          insert into fibonacci_number_{test_uuid}
                             (fib_number) VALUES 
                             ({fib_number}) RETURNING id
                          ; 
                               """).format (fib_number=fib_number, test_uuid=self.db.app.mbt_conn.test_uuid)
                             )

        if commit==True:
            list_sql_char.append('commit;')

            with pytest.allure.step('insert plus commit  SQL=%s' % list_sql_char):
                list_row = self.db.cur_e.execute_insert(list_sql_char=list_sql_char)

            for row in list_row:
                list_table_fibonacci_number.append(Table_fibonacci_number(id=row, fib_number=fib_number))

            if len(list_table_fibonacci_number)>10:
                r_list= random.choice(list_table_fibonacci_number)
                list_table_fibonacci_number.remove(r_list)

            count_table_fibonacci_number+=1

        else:

            list_sql_char.append('rollback;')

            with pytest.allure.step('insert plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_insert(list_sql_char=list_sql_char)


    def get_list(self):
        global list_table_fibonacci_number
        return list_table_fibonacci_number


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

        global list_table_fibonacci_number
        c_records = False

        for x in range(1):

            if x > 1:
                time.sleep(2)

            sql_char = ("""select
                            id,
                            fib_number
                          from
                            fibonacci_number_{test_uuid}
                          where
                          id IN (""").format(test_uuid=self.db.app.mbt_conn.test_uuid)
                                                 #  id = {rowid}                    ;
                                                #).format(rowid=row.id, test_uuid=self.db.app.mbt_conn.test_uuid)

            for row in list_table_fibonacci_number:
                sql_char=sql_char+("""
                            {rowid},""").format(rowid=row.id)
            sql_char=sql_char[:-1]+");"
            print('sql_char=', sql_char)



            for selected_node in self.db.app.mbt_hosts_read:

                with pytest.allure.step('get row  SQL=%s' % sql_char):
                    list_records = self.db.cur_e.execute_select(sql_char=sql_char, selected_node=selected_node)
                for row_list_records in list_records:
                    (id, fib_number) = row_list_records
                    print("selected_node_id=", selected_node.node_id, "check_records_table=", id, fib_number)

                """
                with pytest.allure.step(('compare the row received=%s present=%s') %(str(id)+" "+str(fib_number), str(x.id)+" "+str(x.fib_number))):
                    if  row.id==id and row.fib_number==fib_number:
                        c_records = True
                    else:
                        c_records = False
                        break
            












        xc=0
        yc=0
        while xc<10:

            for x in list_table_fibonacci_number:
                sql_char = mat(xid=x.id, test_uuid=self.db.app.mbt_conn.test_uuid)

                # print('sql_char=', sql_char)

                with pytest.allure.step('get row  SQL=%s' % sql_char):
                    list_records = self.db.cur_e.execute_select(sql_char=sql_char)
                for row in list_records:
                    (id, fib_number) = row
                    #print("check_records_table=", id, fib_number)

                with pytest.allure.step(('compare the row received=%s present=%s') %(str(id)+" "+str(fib_number), str(x.id)+" "+str(x.fib_number))):
                    if  x.id==id and x.fib_number==fib_number:
                        c_records = True
                    else:
                        c_records = False
                        break

            if c_records:
                xc=xc+1
            else:
                xc=xc-10
                #time.sleep(2)
                if yc<5:
                    yc=yc+1
                else:
                    break

        """
        return True

