__author__ = 'vden'

import allure
from model.check_list_tables import Check_list_tables

class FinishingChecklHelper():

    def __init__(self, db):
        self.db = db

    @allure.step('get_list_tables {0}')
    def get_list_tables (self, selected_node=None):
        sql_char = """
            SELECT
              tablename
            FROM
              pg_tables
            WHERE
              schemaname='public'
              AND (
                tablename LIKE 'fibonacci_number%'
                OR tablename LIKE 'points_index_gist%'
                OR tablename LIKE 'mbt_random'
                OR tablename LIKE 'fn_autonomous_transactions%'
                OR tablename LIKE 'fn_pg_pathman%'                                
              )
            ORDER BY
              tablename
            ;"""

        list_table=self.db.cur_e.execute_select(sql_char=sql_char, selected_node=selected_node)
        list_tables=[]
        for tablename in list_table:
            (t_name,) = tablename
            list_tables.append(Check_list_tables(table_name=t_name))

        return list_tables
