__author__ = 'vden'
import pytest

@pytest.allure.step('test_table_fibonacci_number_insert_rollback')
def test_table_fibonacci_number_insert_rollback(app,generator, db):

    c_count=db.table_fibonacci_number.check_count()
    if not c_count:
        for x in range(10):
            db.table_fibonacci_number.insert(fib_number=x*10)

    i_fib = 1
    fib = generator.fibonacci.number(i_fib)

    while fib < 9223372036854775807:

        with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
            db.table_fibonacci_number.insert(fib_number=fib,commit=False)

        i_fib = i_fib + 1
        fib = generator.fibonacci.number(i_fib)

    assert(db.table_fibonacci_number.check_count())
    assert (db.table_fibonacci_number.check_records())

