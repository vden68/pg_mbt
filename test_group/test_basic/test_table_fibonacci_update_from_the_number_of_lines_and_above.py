__author__ = 'vden'
import pytest
import time
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.allure.step('test_table_fibonacci_number_multi_insert_commit')
def test_table_fibonacci_number_multi_insert_commit(db, generator):
    print("\n\ntest_table_fibonacci_number_multi_insert_commit \n\n")

    fib = generator.fibonacci.numbers_list()

    for y in range(10):

        count_table_fibonacci_number=db.table_fibonacci_number.get_count_table_fibonacci_number()
        print('count_table_fibonacci_number=', count_table_fibonacci_number)
        print("\n range=", y)

        for x in range(10):

            list_table_fibonacci_numbers = []
            for i_fib in fib:
                list_table_fibonacci_numbers.append(Table_fibonacci_number(fib_number=i_fib))

            with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
                db.table_fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers)

        db.table_fibonacci_number.update_id_more_than_number(number_write=(y+1), number_id=count_table_fibonacci_number)
        #time.sleep(20)

        assert(db.table_fibonacci_number.check_count())
        assert (db.table_fibonacci_number.check_records())
