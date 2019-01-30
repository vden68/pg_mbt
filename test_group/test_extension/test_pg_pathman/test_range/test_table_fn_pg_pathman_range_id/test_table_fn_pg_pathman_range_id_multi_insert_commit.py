__author__ = 'vden'
import pytest
import allure
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.pg_pathman
@allure.step('test_table_fn_pg_pathman_range_id_multi_insert_commit')
def test_table_fn_pg_pathman_range_id_multi_insert_commit(db, generator):
    print("\n\ntest_table_fn_pg_pathman_range_id_multi_insert_commit \n\n")

    fib = generator.fibonacci.numbers_list()
    list_table_fn_pg_pathman_range_id = []
    for i_fib in fib:
        list_table_fn_pg_pathman_range_id.append(Table_fibonacci_number(fib_number=i_fib))

    cycle_factor = db.app.mbt_conn.cycle_factor
    for y in range(1000*cycle_factor):
        with allure.step('insert in the table the table_fn_pg_pathman_hash %s' % fib):
            db.fn_pg_pathman_range_id.insert(list_table_fibonacci_numbers=list_table_fn_pg_pathman_range_id)

    assert(db.fn_pg_pathman_range_id.check_count())
    assert (db.fn_pg_pathman_range_id.check_records())
