__author__ = 'vden'
import pytest

@pytest.allure.step('test_table_fibonacci_number_insert_commit')
def test_table_fibonacci_number_insert_commit(db, generator):

    fib = generator.fibonacci.numbers_list()

    for x in range(2):

        for i_fib in fib:
            with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
                db.table_fibonacci_number.insert(fib_number=i_fib)

    assert(db.table_fibonacci_number.check_count())
    #assert (db.table_fibonacci_number.check_records())
