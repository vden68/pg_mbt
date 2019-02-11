__author__ = 'vden'

import pytest
import allure


@pytest.mark.create_and_drop_tables_FN
def test_create_tables_FN_empty(db):
    print("\n\ntest_create_tables_FN_empty \n\n")
    cycle_factor=db.app.mbt_conn.cycle_factor
    number_of_tables=100*cycle_factor
    db.create_and_drop_tables_FN.create_tables_empty(number_of_tables=number_of_tables)




@pytest.mark.create_and_drop_tables_FN
def test_drop_tables_FN_empty(db):
    print("\n\ntest_drop_tables_FN_empty \n\n")
    count_tables_fibonacci_number_empty=db.create_and_drop_tables_FN.get_count_tables_fibonacci_number_empty()
    allure.attach('get_count_tables_fibonacci_number_empty=%s' % count_tables_fibonacci_number_empty)
    allure.attach('get_count_tables_fibonacci_number_empty=%s' % count_tables_fibonacci_number_empty)
    print('count_tables_fibonacci_number_empty=', count_tables_fibonacci_number_empty)
    db.create_and_drop_tables_FN.drop_tables_empty()



