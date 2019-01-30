__author__ = 'vden'
import pytest
import allure
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.pg_pathman
@allure.step('test_table_fn_pg_pathman_hash_insert_commit')
def test_table_fn_pg_pathman_hash_insert_commit(db, generator):
    print("\n\ntest_table_fn_pg_pathman_hash_insert_commit \n\n")

    fib = generator.fibonacci.numbers_list()

    cycle_factor=db.app.mbt_conn.cycle_factor
    for x in range(10*cycle_factor):

        for i_fib in fib:
            list_table_fn_pg_pathman_hash = []
            list_table_fn_pg_pathman_hash.append(Table_fibonacci_number(id=0,fib_number=i_fib))
            with allure.step('insert in the table the table_fn_pg_pathman_hash %s' % fib):
                db.fn_pg_pathman_hash.insert(list_table_fibonacci_numbers=list_table_fn_pg_pathman_hash)

    assert(db.fn_pg_pathman_hash.check_count())
    assert (db.fn_pg_pathman_hash.check_records())
