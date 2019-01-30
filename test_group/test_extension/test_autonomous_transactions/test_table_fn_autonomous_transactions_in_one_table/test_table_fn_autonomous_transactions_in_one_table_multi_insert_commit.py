__author__ = 'vden'
import pytest
import allure
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.pg_pathman
@allure.step('test_table_fn_autonomous_transactions_in_one_table_multi_insert_commit')
def test_table_fn_autonomous_transactions_in_one_table_multi_insert_commit(db, generator):
    print("\n\ntest_table_fn_autonomous_transactions_in_one_table_multi_insert_commit \n\n")

    fib = generator.fibonacci.numbers_list()
    list_table_fn_autonomous_transactions_in_one_table = []
    for i_fib in fib:
        list_table_fn_autonomous_transactions_in_one_table.append(Table_fibonacci_number(id=0, fib_number=i_fib))

    cycle_factor=db.app.mbt_conn.cycle_factor
    for x in range(500*cycle_factor):
        with allure.step('insert in the test_table_fn_autonomous_transactions_in_one_table %s'
                                        % fib):
            db.fn_autonomous_transactions_in_one_table.autonomous_transactions_insert(
                list_table_fibonacci_numbers=list_table_fn_autonomous_transactions_in_one_table)

    assert(db.fn_autonomous_transactions_in_one_table.check_count())
    assert (db.fn_autonomous_transactions_in_one_table.check_records())
