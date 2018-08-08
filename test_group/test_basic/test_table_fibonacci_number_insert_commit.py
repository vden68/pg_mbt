__author__ = 'vden'
import pytest
from functools import wraps

@pytest.mark.test_table_fibonacci_number_insert_commit
@pytest.allure.step('test_table_fibonacci_number_insert_commit')
def test_table_fibonacci_number_insert_commit(generator, db):


    i_fib = 1
    fib = generator.fibonacci.number(i_fib)

    while fib < 9223372036854775807:

        with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
            db.table_fibonacci_number.insert(fib_number=fib)

        i_fib = i_fib + 1
        fib = generator.fibonacci.number(i_fib)

    assert(db.table_fibonacci_number.check_count())
    assert (db.table_fibonacci_number.check_records())



mbt_test_table_fibonacci_number_insert_commit=test_table_fibonacci_number_insert_commit
