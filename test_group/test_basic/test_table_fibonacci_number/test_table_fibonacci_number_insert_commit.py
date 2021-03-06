__author__ = 'vden'
import pytest
import allure
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.test_basic
@allure.step('test_table_fibonacci_number_insert_commit')
def test_table_fibonacci_number_insert_commit(db, generator):
    print("\n\ntest_table_fibonacci_number_insert_commit \n\n")

    fib = generator.fibonacci.numbers_list()

    cycle_factor=db.app.mbt_conn.cycle_factor
    for x in range(5*cycle_factor):

        for i_fib in fib:
            list_table_fibonacci_numbers = []
            list_table_fibonacci_numbers.append(Table_fibonacci_number(id=0,fib_number=i_fib))
            with allure.step('insert in the table the Fibonacci number %s' % fib):
                db.table_fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers)

    assert(db.table_fibonacci_number.check_count())
    assert (db.table_fibonacci_number.check_records())
