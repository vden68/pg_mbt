__author__ = 'vden'
import pytest
import random
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number


@pytest.mark.pg_pathman
@pytest.allure.step('test_table_fn_pg_pathman_hash_with_delete_commit_or_rollback')
def test_table_fn_pg_pathman_hash_with_delete_commit_or_rollback(db, generator):
    print("\n\ntest_table_fn_pg_pathman_hash_with_delete_commit_or_rollback \n\n")


    if db.fn_pg_pathman_hash.get_count_table_fibonacci_number()<100:
        fib = generator.fibonacci.numbers_list()
        for x in range(10):
            list_table_fibonacci_numbers = []
            for i_fib in fib:
                list_table_fibonacci_numbers.append(Table_fibonacci_number(fib_number=i_fib))

            with pytest.allure.step('insert in the table the table_fn_pg_pathman_hash %s' % fib):
                db.fn_pg_pathman_hash.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers)



    #test_table_fibonacci_number_with_delete
    #cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(10):
        with pytest.allure.step('update id more than number'):
            com_or_ron = random.randint(0, 1)
            if com_or_ron == 0:
                db.fn_pg_pathman_hash.delete_2_percent_of_rows()
            else:
                db.fn_pg_pathman_hash.delete_2_percent_of_rows(commit=False)

        assert(db.fn_pg_pathman_hash.check_count())
        assert (db.fn_pg_pathman_hash.check_records())
