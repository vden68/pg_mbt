__author__ = 'vden'

from test_group.test_basic.test_table_fibonacci_number.test_table_fibonacci_number_insert_commit import test_table_fibonacci_number_insert_commit



class Mbtfixture:

    def __init__(self):
        self.mbt_test_table_fibonacci_number_insert_commit = test_table_fibonacci_number_insert_commit(self)



    def destroy(self):
        pass


