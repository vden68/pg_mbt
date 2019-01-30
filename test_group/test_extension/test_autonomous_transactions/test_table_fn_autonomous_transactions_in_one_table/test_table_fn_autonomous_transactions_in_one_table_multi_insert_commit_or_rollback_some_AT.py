__author__ = 'vden'
import pytest
import allure
import random
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number


@pytest.mark.pg_pathman
@allure.step('test_table_fn_autonomous_transactions_in_one_table_insert_commit_or_rollback')
def test_table_fn_autonomous_transactions_in_one_table_insert_commit_or_rollback(generator, db):
    print("\n\ntest_table_fn_autonomous_transactions_in_one_table_insert_commit_or_rollback \n\n")
    fib = generator.fibonacci.numbers_list()
    list_table_fn_autonomous_transactions_in_one_table = []
    for i_fib in fib:
        list_table_fn_autonomous_transactions_in_one_table.append(Table_fibonacci_number(id=0, fib_number=i_fib))

    cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(500*cycle_factor):
        with allure.step('insert in the table_fn_autonomous_transactions_in_one_table %s' % fib):
            com_or_ron = random.randint(0, 3)
            if com_or_ron == 0:
                db.fn_autonomous_transactions_in_one_table.autonomous_transactions_insert(
                    list_table_fibonacci_numbers=list_table_fn_autonomous_transactions_in_one_table,
                    count_autonomous_transactions=cycle_factor + 1)
            elif com_or_ron == 1:
                db.fn_autonomous_transactions_in_one_table.autonomous_transactions_insert(
                    list_table_fibonacci_numbers=list_table_fn_autonomous_transactions_in_one_table,
                    commit=False, count_autonomous_transactions=cycle_factor+1)
            elif com_or_ron == 2:
                db.fn_autonomous_transactions_in_one_table.autonomous_transactions_insert(
                    list_table_fibonacci_numbers=list_table_fn_autonomous_transactions_in_one_table,
                    commit_autonomous_transactions=False, count_autonomous_transactions=cycle_factor+1)
            else:
                db.fn_autonomous_transactions_in_one_table.autonomous_transactions_insert(
                    list_table_fibonacci_numbers=list_table_fn_autonomous_transactions_in_one_table,
                    commit=False, commit_autonomous_transactions=False, count_autonomous_transactions=cycle_factor+1)

    assert (db.fn_autonomous_transactions_in_one_table.check_count())
    assert (db.fn_autonomous_transactions_in_one_table.check_records())

