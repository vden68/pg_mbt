__author__ = 'vden'

import pytest
import time




class TableMbtRandomHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        if self.db.initdb.check_tablename(tablename='mbt_random') :
            print(("table '%s' already created") % 'mbt_random')
        else:
            print(("table '%s' no created") % 'mbt_random')

            list_sql_char = []

            list_sql_char.append("BEGIN")

            list_sql_char.append("""
                     CREATE TABLE mbt_random
                     (id         serial NOT NULL 
                                 CONSTRAINT mbt_random_pkey
                                 PRIMARY KEY ,
                     fib_number bigint,
                     p_point point NOT NULL )
                     ;""")

            list_sql_char.append('COMMIT;')

            #test_list = self.db.generator.mbt_random.random_generator()
            #print('test_list=', test_list)

            with pytest.allure.step('DDL=%s' % list_sql_char):
                self.db.cur_e.execute_ddl(list_sql_char=list_sql_char)

            self.insert()


    @pytest.allure.step('insert in table "mbt_random"')
    def insert(self ):


        list_mbt_random = self.db.generator.mbt_random.random_generator()
        list_sql_char=[]

        list_sql_char.append("BEGIN;")
        sql_char=("""INSERT INTO mbt_random
                             (fib_number, p_point) VALUES""")

        for l in list_mbt_random:
            sql_char+=("""
                       ({fib_number}, {pl_point}),""").format (fib_number= l.fib_number,
                                                               pl_point=("'"+str(l.p_point_x)+","+str(l.p_point_y))+"'")
        sql_char=sql_char[:-1]+" RETURNING id ;"

        list_sql_char.append(sql_char)

        list_sql_char.append('COMMIT;')

        with pytest.allure.step('insert plus commit  SQL=%s' % list_sql_char):
            self.db.cur_e.execute_insert(list_sql_char=list_sql_char)

        self.db.table_check.checking_completion_of_all_locks(table_name="mbt_random")


    @pytest.allure.step('check count')
    def check_count(self):

        global count_table_points_index_gist
        table_name = ("points_index_gist_{test_uuid}").format(test_uuid=self.db.app.mbt_conn.test_uuid)
        c_count = self.db.table_check.check_count(count_rows_table=count_table_points_index_gist, table_name=table_name)

        return c_count

    @pytest.allure.step('check records')
    def check_records(self):

        sql_char = ("""
            SELECT
                   count(id) AS count_box
            FROM
                 points_index_gist_{test_uuid}
            GROUP BY
                  p_point <@ box '(-100,-100),(-80,100)',
                  p_point <@ box '(-60,-100),(-40,100)',
                  p_point <@ box '(-40,-100),(-20,100)',
                  p_point <@ box '(0,-100),(20,100)',
                  p_point <@ box '(20,-100),(40,100)',
                  p_point <@ box '(60,-100),(80,100)',
                  p_point <@ box '(80,-100),(100,100)'
            ORDER BY
              count_box
            ;
            """).format(test_uuid=self.db.app.mbt_conn.test_uuid)

        for x in range(10):

            if x > 1:
                time.sleep(2)

            with pytest.allure.step('get row records for verification  SQL=%s' % sql_char):
                list_row = self.db.cur_e.execute_select(sql_char=sql_char)

            list_row_records_for_verification = []
            if list_row is not None:
                for row in list_row:
                    (count_box,) = row
                    list_row_records_for_verification.append(count_box)
                break

        # list_row_records_for_verification=sorted(list_row_records_for_verification, key=lambda x: x.id)

        for selected_node in self.db.app.mbt_hosts_read:

            with pytest.allure.step('get the number of rows  SQL=%s' % sql_char):
                list_row = self.db.cur_e.execute_select(sql_char=sql_char, selected_node=selected_node)
                list_row2 = []

                if list_row is not None:
                    for row in list_row:
                        (count_box,) = row
                        list_row2.append(count_box)

                    # print('list_row_records_for_verification=' , list_row_records_for_verification)
                    # print('list_row2=', list_row2)
                    assert list_row_records_for_verification == list_row2
                    print("node_id=", selected_node.node_id, True)
                else:
                    print("node_id=", selected_node.node_id, None)

        return True

    @pytest.allure.step('delete 2 percent of rows "points_index_gist"')
    def delete_2_percent_of_rows(self, commit=True):

        global count_table_points_index_gist
        c_limit = count_table_points_index_gist // 50 + 1

        list_sql_char = []

        list_sql_char.append("BEGIN;")
        sql_char = (("""
        DELETE FROM points_index_gist_{test_uuid}
          WHERE
            id IN (SELECT id  FROM points_index_gist_{test_uuid}
                    ORDER BY RANDOM()
                      LIMIT {m_limit})
        ;
        """).format(test_uuid=self.db.app.mbt_conn.test_uuid, m_limit=c_limit))

        list_sql_char.append(sql_char)

        if commit == True:
            list_sql_char.append('commit;')

            #print("list_sql_char=", list_sql_char)

            with pytest.allure.step('delete plus commit  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)
                count_table_points_index_gist=count_table_points_index_gist-c_limit
                print('c_limit=', c_limit)

        else:

            list_sql_char.append('rollback;')

            with pytest.allure.step('delete plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)


    def get_count_table_points_index_gist(self):
        global count_table_points_index_gist
        return count_table_points_index_gist







