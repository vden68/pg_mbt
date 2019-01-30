__author__ = 'vden'
import pytest
import allure
import random
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.pg_pathman
@allure.step('test_table_fn_pg_pathman_hash_update_commit_or_rollback')
def test_table_fn_pg_pathman_hash_update_commit_or_rollback(db, generator):
    print("\n\ntest_table_fn_pg_pathman_hash_update_commit_or_rollback \n\n")

    fib = generator.fibonacci.numbers_list()

    #cycle_factor = db.app.mbt_conn.cycle_factor
    for y in range(10):

        count_table_fn_pg_pathman_hash=db.fn_pg_pathman_hash.get_count_table_fibonacci_number()
        print('count_table_fn_pg_pathman_hash=', count_table_fn_pg_pathman_hash)
        print("\n range=", y)

        for x in range(20):

            list_table_count_table_fn_pg_pathman_hash = []
            for i_fib in fib:
                list_table_count_table_fn_pg_pathman_hash.append(Table_fibonacci_number(fib_number=i_fib))

            with allure.step('insert in the table the Fibonacci number %s' % fib):

                db.fn_pg_pathman_hash.insert(list_table_fibonacci_numbers=list_table_count_table_fn_pg_pathman_hash)

        with allure.step('update id more than number'):
            com_or_ron = random.randint(0, 1)
            if com_or_ron == 0:
                db.fn_pg_pathman_hash.update_id_random()
            else:
                db.fn_pg_pathman_hash.update_id_random(commit=False)


    assert(db.fn_pg_pathman_hash.check_count())
    assert (db.fn_pg_pathman_hash.check_records())
