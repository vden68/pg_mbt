__author__ = 'vden'
import pytest
import time
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.allure.step('test table fibonacci update from the number of lines and above')
def test_table_fibonacci_update_from_the_number_of_lines_and_above(db, generator):
    print("\n\ntest_table_fibonacci_update_from_the_number_of_lines_and_above \n\n")

    fib = generator.fibonacci.numbers_list()

    cycle_factor = db.app.mbt_conn.cycle_factor
    for y in range(10*cycle_factor):

        count_table_fibonacci_number=db.table_fibonacci_number.get_count_table_fibonacci_number()
        print('count_table_fibonacci_number=', count_table_fibonacci_number)
        print("\n range=", y)

        for x in range(50):

            list_table_fibonacci_numbers = []
            for i_fib in fib:
                list_table_fibonacci_numbers.append(Table_fibonacci_number(fib_number=i_fib))

            with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
                db.table_fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers)

        with pytest.allure.step('update id more than number'):
            db.table_fibonacci_number.update_id_more_than_number(number_write=(y+1), number_id=count_table_fibonacci_number)

    assert(db.table_fibonacci_number.check_count())
    assert (db.table_fibonacci_number.check_records())
