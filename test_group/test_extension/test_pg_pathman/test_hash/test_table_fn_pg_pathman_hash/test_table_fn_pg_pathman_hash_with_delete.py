__author__ = 'vden'
import pytest
from model.basic_tables.table_fibonacci_number import Table_fibonacci_number

@pytest.mark.xfail
@pytest.mark.pg_pathman
@pytest.allure.step('test_table_fn_pg_pathman_hash_with_delete')
def test_table_fn_pg_pathman_hash_with_delete(db, generator):
    print("\n\ntest_table_fn_pg_pathman_hash_with_delete \n\n")


    if db.fn_pg_pathman_hash.get_count_table_fibonacci_number()<100:
        fib = generator.fibonacci.numbers_list()
        for x in range(10):
            list_table_fn_pg_pathman_hash = []
            for i_fib in fib:
                list_table_fn_pg_pathman_hash.append(Table_fibonacci_number(fib_number=i_fib))

            with pytest.allure.step('insert in the table the table_fn_pg_pathman_hash %s' % fib):
                db.fn_pg_pathman_hash.insert(list_table_fibonacci_numbers=list_table_fn_pg_pathman_hash)



    #test_table_fibonacci_number_with_delete
    #cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(1):
        with pytest.allure.step('delete 2 percent of rows'):
            db.fn_pg_pathman_hash.delete_2_percent_of_rows()

        assert(db.fn_pg_pathman_hash.check_count())
        assert (db.fn_pg_pathman_hash.check_records())
