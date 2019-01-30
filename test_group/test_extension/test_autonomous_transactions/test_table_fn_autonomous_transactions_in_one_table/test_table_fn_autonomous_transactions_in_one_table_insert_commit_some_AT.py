__author__ = 'vden'
import pytest
import allure
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.pg_pathman
@allure.step('test_table_fn_autonomous_transactions_in_one_table_insert_commit_some_at')
def test_table_fn_autonomous_transactions_in_one_table_insert_commit_some_at(db, generator):
    print("\n\ntest_table_fn_autonomous_transactions_in_one_table_insert_commit_some_at \n\n")

    fib = generator.fibonacci.numbers_list()

    cycle_factor=db.app.mbt_conn.cycle_factor
    for x in range(10*cycle_factor):

        for i_fib in fib:
            list_table_fn_autonomous_transactions_in_one_table = []
            list_table_fn_autonomous_transactions_in_one_table.append(Table_fibonacci_number(id=0,fib_number=i_fib))
            with allure.step('insert in the test_table_fn_autonomous_transactions_in_one_table %s'
                                            % fib):
                db.fn_autonomous_transactions_in_one_table.autonomous_transactions_insert(
                    list_table_fibonacci_numbers=list_table_fn_autonomous_transactions_in_one_table,
                    count_autonomous_transactions=cycle_factor+1)

    assert(db.fn_autonomous_transactions_in_one_table.check_count())
    assert (db.fn_autonomous_transactions_in_one_table.check_records())
