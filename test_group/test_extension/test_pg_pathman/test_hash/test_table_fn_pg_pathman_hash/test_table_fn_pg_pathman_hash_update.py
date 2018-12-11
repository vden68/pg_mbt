__author__ = 'vden'
import pytest
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.pg_pathman
@pytest.allure.step('test_table_fn_pg_pathman_hash_update')
def test_table_fn_pg_pathman_hash_update(db, generator):
    print("\n\ntest_table_fn_pg_pathman_hash_update \n\n")

    fib = generator.fibonacci.numbers_list()

    #cycle_factor = db.app.mbt_conn.cycle_factor
    for y in range(10):

        count_table_fn_pg_pathman_hash=db.fn_pg_pathman_hash.get_count_table_fibonacci_number()
        print('count_table_fn_pg_pathman_hash=', count_table_fn_pg_pathman_hash)
        print("\n range=", y)

        for x in range(20):

            list_table_fn_pg_pathman_hash = []
            for i_fib in fib:
                list_table_fn_pg_pathman_hash.append(Table_fibonacci_number(fib_number=i_fib))

            with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
                db.fn_pg_pathman_hash.insert(list_table_fibonacci_numbers=list_table_fn_pg_pathman_hash)

        with pytest.allure.step('update id more than number'):
            db.fn_pg_pathman_hash.update_id_random()

    assert(db.fn_pg_pathman_hash.check_count())
    assert (db.fn_pg_pathman_hash.check_records())
