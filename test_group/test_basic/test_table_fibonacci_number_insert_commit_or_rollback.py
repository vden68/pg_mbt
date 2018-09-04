__author__ = 'vden'
import pytest
import random

@pytest.allure.step('test_table_fibonacci_number_insert_commit_or_rollback')
def test_table_fibonacci_number_insert_commit_or_rollback(generator, db):

    i_fib = 1
    fib = generator.fibonacci.number(i_fib)

    while fib < 9223372036854775807:

        with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
            com_or_ron=random.randint(0,1)
            if com_or_ron==0:
                db.table_fibonacci_number.insert(fib_number=fib)
            else:
                db.table_fibonacci_number.insert(fib_number=fib, commit=False)

        i_fib = i_fib + 1
        fib = generator.fibonacci.number(i_fib)

    assert(db.table_fibonacci_number.check_count())
    #assert (db.table_fibonacci_number.check_records())

#mbt_test_table_fibonacci_number_insert_commit_or_roll=test_table_fibonacci_number_insert_commit_or_rollback