__author__ = 'vden'
import pytest
import random
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number


@pytest.mark.pg_pathman
@pytest.allure.step('test_table_fn_pg_pathman_hash_insert_commit_or_rollback')
def test_table_fn_pg_pathman_hash_insert_commit_or_rollback(generator, db):
    print("\n\ntest_table_fn_pg_pathman_hash_insert_commit_or_rollback \n\n")
    fib = generator.fibonacci.numbers_list()

    cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(20*cycle_factor):

        for i_fib in fib:
            list_table_fn_pg_pathman_hash = []
            list_table_fn_pg_pathman_hash.append(Table_fibonacci_number(id=0, fib_number=i_fib))
            with pytest.allure.step('insert in the table the fn_pg_pathman_hashr %s' % fib):
                com_or_ron = random.randint(0, 1)
                if com_or_ron == 0:
                    db.fn_pg_pathman_hash.insert(list_table_fibonacci_numbers=list_table_fn_pg_pathman_hash)
                else:
                    db.fn_pg_pathman_hash.insert(list_table_fibonacci_numbers=list_table_fn_pg_pathman_hash, commit=False)

    assert (db.fn_pg_pathman_hash.check_count())
    assert (db.fn_pg_pathman_hash.check_records())

