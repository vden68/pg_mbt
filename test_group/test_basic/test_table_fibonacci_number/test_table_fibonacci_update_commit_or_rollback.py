__author__ = 'vden'
import pytest
import allure
import random
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.test_basic
@allure.step('test_table_fibonacci_update_commit_or_rollback')
def test_table_fibonacci_update_commit_or_rollback(db, generator):
    print("\n\ntest_table_fibonacci_update_commit_or_rollback \n\n")

    fib = generator.fibonacci.numbers_list()

    #cycle_factor = db.app.mbt_conn.cycle_factor
    for y in range(10):

        count_table_fibonacci_number=db.table_fibonacci_number.get_count_table_fibonacci_number()
        print('count_table_fibonacci_number=', count_table_fibonacci_number)
        print("\n range=", y)

        for x in range(10):

            list_table_fibonacci_numbers = []
            for i_fib in fib:
                list_table_fibonacci_numbers.append(Table_fibonacci_number(fib_number=i_fib))

            with allure.step('insert in the table the Fibonacci number %s' % fib):

                db.table_fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers)

        with allure.step('update id more than number'):
            com_or_ron = random.randint(0, 1)
            if com_or_ron == 0:
                db.table_fibonacci_number.update_id_random()
            else:
                db.table_fibonacci_number.update_id_random(commit=False)


    assert(db.table_fibonacci_number.check_count())
    assert (db.table_fibonacci_number.check_records())
