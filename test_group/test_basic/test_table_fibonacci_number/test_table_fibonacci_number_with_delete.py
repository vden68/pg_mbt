__author__ = 'vden'
import pytest
import allure
import time
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.test_basic
@allure.step('test_table_fibonacci_number_with_delete')
def test_table_fibonacci_number_with_delete(db, generator):
    print("\n\ntest_table_fibonacci_number_with_delete \n\n")


    if db.table_fibonacci_number.get_count_table_fibonacci_number()<100:
        fib = generator.fibonacci.numbers_list()
        for x in range(10):
            list_table_fibonacci_numbers = []
            for i_fib in fib:
                list_table_fibonacci_numbers.append(Table_fibonacci_number(fib_number=i_fib))

            with allure.step('insert in the table the Fibonacci number %s' % fib):
                db.table_fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers)



    #test_table_fibonacci_number_with_delete
    #cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(10):
        with allure.step('delete 2 percent of rows'):
            db.table_fibonacci_number.delete_2_percent_of_rows()

        assert(db.table_fibonacci_number.check_count())
        assert (db.table_fibonacci_number.check_records())
