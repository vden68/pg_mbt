__author__ = 'vden'
import pytest
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number


@pytest.allure.step('test_table_fibonacci_number_insert_commit')
def test_table_fibonacci_number_insert_commit(db, generator):

    fib = generator.fibonacci.numbers_list()

    for x in range(1):

        for i_fib in fib:
            list_table_fibonacci_numbers = []
            list_table_fibonacci_numbers.append(Table_fibonacci_number(id=0,fib_number=i_fib))
            with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
                db.table_fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers)

    assert(db.table_fibonacci_number.check_count())
    #print(db.table_fibonacci_number.get_list())
    #assert (db.table_fibonacci_number.check_records())
