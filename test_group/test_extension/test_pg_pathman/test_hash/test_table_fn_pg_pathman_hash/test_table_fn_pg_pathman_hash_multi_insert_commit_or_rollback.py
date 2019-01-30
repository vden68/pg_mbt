__author__ = 'vden'
import pytest
import allure
import random
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.pg_pathman
@allure.step('test_table_fn_pg_pathman_hash_multi_insert_commit_or_rollback')
def test_table_fn_pg_pathman_hash_multi_insert_commit_or_rollback(db, generator):
    print("\n\ntest_table_fn_pg_pathman_hash_multi_insert_commit_or_rollback \n\n")

    fib = generator.fibonacci.numbers_list()
    list_table_fn_pg_pathman_hash = []
    for i_fib in fib:
        list_table_fn_pg_pathman_hash.append(Table_fibonacci_number(fib_number=i_fib))

    cycle_factor = db.app.mbt_conn.cycle_factor
    for y in range(2000*cycle_factor):
        with allure.step('insert in the table the table_fn_pg_pathman_hash %s' % fib):
            com_or_ron = random.randint(0, 1)
            if com_or_ron == 0:
                db.fn_pg_pathman_hash.insert(list_table_fibonacci_numbers=list_table_fn_pg_pathman_hash)
            else:
                db.fn_pg_pathman_hash.insert(list_table_fibonacci_numbers=list_table_fn_pg_pathman_hash, commit=False)


    assert(db.fn_pg_pathman_hash.check_count())
    assert (db.fn_pg_pathman_hash.check_records())
