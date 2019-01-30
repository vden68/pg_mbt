__author__ = 'vden'

import pytest
import time
import allure


table_points_index_gist = None
count_table_points_index_gist = 0

class Table_points_index_gistHelper():

    def __init__(self, db):
        self.db = db

    def create_table(self):

        if self.db.initdb.check_tablename(tablename='points_index_gist_'+self.db.app.mbt_conn.test_uuid) :
            print(("table '%s' already created") % 'points_index_gist')
        else:
            print(("table '%s' no created") % 'points_index_gist')

            list_sql_char = []

            list_sql_char.append("BEGIN")

            list_sql_char.append(("""
                     CREATE TABLE points_index_gist_{test_uuid}
                     (id         serial NOT NULL 
                                 CONSTRAINT points_index_gist_{test_uuid}_pkey
                                 PRIMARY KEY ,
                     p_point point NOT NULL )
                     ;""") .format(test_uuid=self.db.app.mbt_conn.test_uuid)
                                 )

            list_sql_char.append(("""
                CREATE  INDEX  
                     points_index_gist_{test_uuid}_column_p_point 
                  ON 
                     points_index_gist_{test_uuid}  USING GIST(p_point)
                ;""") .format(test_uuid=self.db.app.mbt_conn.test_uuid))

            list_sql_char.append('COMMIT;')

            with pytest.allure.step('DDL=%s' % list_sql_char):
                self.db.cur_e.execute_ddl(list_sql_char=list_sql_char)


    @allure.step('insert in table "points_index_gist"')
    def insert(self, list_points=None, commit=True):
        global count_table_points_index_gist
        global table_points_index_gist
        if table_points_index_gist is None:
            self.create_table()
            table_points_index_gist = True

        list_sql_char=[]

        list_sql_char.append("BEGIN;")
        sql_char=(("""INSERT INTO points_index_gist_{test_uuid}
                             (p_point) VALUES""").format(test_uuid=self.db.app.mbt_conn.test_uuid))

        for p in list_points:
            sql_char+=("""
                       ({pl_point}),""").format (pl_point=("'"+str(p.p_point_x)+","+str(p.p_point_y))+"'")
        sql_char=sql_char[:-1]+" RETURNING id ;"

        list_sql_char.append(sql_char)

        if commit==True:
            list_sql_char.append('commit;')

            with pytest.allure.step('insert plus commit  SQL=%s' % list_sql_char):
                list_row = self.db.cur_e.execute_insert(list_sql_char=list_sql_char)

                count_table_points_index_gist+=len(list_points)

        else:

            list_sql_char.append('rollback;')

            with pytest.allure.step('insert plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_insert(list_sql_char=list_sql_char)

                #self.db.conn.all_close_conn()


    @allure.step('check count')
    def check_count(self):

        global count_table_points_index_gist
        table_name = ("points_index_gist_{test_uuid}").format(test_uuid=self.db.app.mbt_conn.test_uuid)
        c_count = self.db.table_check.check_count(count_rows_table=count_table_points_index_gist, table_name=table_name)

        return c_count

    @allure.step('check records')
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

    @allure.step('delete 2 percent of rows "points_index_gist"')
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


    @allure.step('update in table "points_index_gist"')
    def update_id_random(self, commit=True):

        global count_table_points_index_gist
        c_limit = count_table_points_index_gist // 10 + 1
        if c_limit>50000:
            c_limit=50000

        list_sql_char = []

        list_sql_char.append("BEGIN;")
        sql_char = (("""UPDATE 
                              points_index_gist_{test_uuid} AS f
                            SET 
                              p_point = (SELECT m.p_point FROM mbt_random AS m
                            WHERE m.id<> f.id
                            ORDER BY  RANDOM()
                            LIMIT 1)        
                            WHERE 
                              f.id IN (SELECT id  FROM points_index_gist_{test_uuid}
                                     ORDER BY RANDOM()
                                     LIMIT {m_limit})
                             ;""").format(test_uuid=self.db.app.mbt_conn.test_uuid, m_limit=c_limit))

        list_sql_char.append(sql_char)

        if commit == True:
            list_sql_char.append('COMMIT;')

            with pytest.allure.step('update plus commit  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)

        else:

            list_sql_char.append('ROLLBACK;')

            with pytest.allure.step('update plus rollback  SQL=%s' % list_sql_char):
                self.db.cur_e.execute_update(list_sql_char=list_sql_char)








