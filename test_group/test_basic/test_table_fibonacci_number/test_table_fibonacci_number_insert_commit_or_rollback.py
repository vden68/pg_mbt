__author__ = 'vden'
import pytest
import allure
import random
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number


@pytest.mark.test_basic
@allure.step('test_table_fibonacci_number_insert_commit_or_rollback')
def test_table_fibonacci_number_insert_commit_or_rollback(generator, db):
    print("\n\ntest_table_fibonacci_number_insert_commit_or_rollback \n\n")
    fib = generator.fibonacci.numbers_list()

    cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(20*cycle_factor):

        for i_fib in fib:
            list_table_fibonacci_numbers = []
            list_table_fibonacci_numbers.append(Table_fibonacci_number(id=0, fib_number=i_fib))
            with allure.step('insert in the table the Fibonacci number %s' % fib):
                com_or_ron = random.randint(0, 1)
                if com_or_ron == 0:
                    db.table_fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers)
                else:
                    db.table_fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers, commit=False)

    assert (db.table_fibonacci_number.check_count())
    assert (db.table_fibonacci_number.check_records())

