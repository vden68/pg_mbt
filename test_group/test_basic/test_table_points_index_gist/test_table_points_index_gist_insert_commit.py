__author__ = 'vden'
import pytest
from model.basic_tables.table_points_index_gist import Table_points_index_gist

@pytest.allure.step('test_table_points_index_gist_insert_commit')
def test_table_points_index_gist_insert_commit(db, generator):
    print("\n\ntest_table_points_index_gist_insert_commit \n\n")

    cycle_factor = db.app.mbt_conn.cycle_factor
    list_points = generator.p_points.g_points(coumt_points=500*cycle_factor)

    for x in list_points:
        #print(x)
        with pytest.allure.step('insert in the table the Fibonacci number %s' % x):
            list_table_points = []
            list_table_points.append(Table_points_index_gist(p_point_x=x.p_point_x, p_point_y=x.p_point_y))
            db.table_points_index_gist.insert(list_points=list_table_points)

    assert(db.table_points_index_gist.check_count())


    """
    cycle_factor=db.app.mbt_conn.cycle_factor
    for x in range(10*cycle_factor):

        for i_fib in fib:
            list_table_fibonacci_numbers = []
            list_table_fibonacci_numbers.append(Table_fibonacci_number(id=0,fib_number=i_fib))
            with pytest.allure.step('insert in the table the Fibonacci number %s' % fib):
                db.table_fibonacci_number.insert(list_table_fibonacci_numbers=list_table_fibonacci_numbers)

    assert(db.table_fibonacci_number.check_count())
    assert (db.table_fibonacci_number.check_records())
    """