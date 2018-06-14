__author__ = 'vden'
import pytest

@pytest.allure.step('test_table_fibonacci_number_insert_commit')
def test_table_fibonacci_number_insert_commit(app,generator, db):

    i_fib = 1
    fib = generator.fibonacci.number(i_fib)

    while fib < 9223372036854775807:

        with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
            db.table_fibonacci_number.insert(fib_number=fib)

        i_fib = i_fib + 1
        fib = generator.fibonacci.number(i_fib)
        print('i_fib=', i_fib, 'fib=', fib)

    assert(db.table_fibonacci_number.check_count())
    assert (db.table_fibonacci_number.check_records())
    print("mbt_hosts=", app.mbt_hosts)

