__author__ = 'vden'


import allure

class FinishingChecklHelper():

    def __init__(self, db):
        self.db = db

    @allure.step('create table {0}')
    def get_list_tables (self):
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
              )
            ORDER BY
              tablename
            ;"""

