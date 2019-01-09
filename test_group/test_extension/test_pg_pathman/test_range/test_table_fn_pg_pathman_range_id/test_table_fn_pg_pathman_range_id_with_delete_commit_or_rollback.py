__author__ = 'vden'
import pytest
import random
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number


@pytest.mark.pg_pathman
@pytest.allure.step('test_table_fn_pg_pathman_range_id_with_delete_commit_or_rollback')
def test_table_fn_pg_pathman_range_id_with_delete_commit_or_rollback(db, generator):
    print("\n\ntest_table_fn_pg_pathman_range_id_with_delete_commit_or_rollback \n\n")


    if db.fn_pg_pathman_range_id.get_count_table_fibonacci_number()<100:
        fib = generator.fibonacci.numbers_list()
        for x in range(10):
            list_table_fn_pg_pathman_range_id = []
            for i_fib in fib:
                list_table_fn_pg_pathman_range_id.append(Table_fibonacci_number(fib_number=i_fib))

            with pytest.allure.step('insert in the table the table_fn_pg_pathman_range_id %s' % fib):
                db.fn_pg_pathman_range_id.insert(list_table_fibonacci_numbers=list_table_fn_pg_pathman_range_id)



    #test_table_fibonacci_number_with_delete
    #cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(10):
        with pytest.allure.step('update id more than number'):
            com_or_ron = random.randint(0, 1)
            if com_or_ron == 0:
                db.fn_pg_pathman_range_id.delete_2_percent_of_rows()
            else:
                db.fn_pg_pathman_range_id.delete_2_percent_of_rows(commit=False)

        assert(db.fn_pg_pathman_range_id.check_count())
        assert (db.fn_pg_pathman_range_id.check_records())
