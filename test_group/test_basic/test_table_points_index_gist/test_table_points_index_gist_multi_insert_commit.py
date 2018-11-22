__author__ = 'vden'
import pytest

@pytest.mark.test_basic
@pytest.allure.step('test_table_points_index_gist_insert_commit')
def test_table_points_index_gist_insert_commit(db, generator):
    print("\n\ntest_table_points_index_gist_insert_commit \n\n")

    cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(20*cycle_factor):
        list_points = generator.p_points.g_points(coumt_points=10000)

        with pytest.allure.step('insert in the table the points index gist %s' % list_points):
            db.table_points_index_gist.insert(list_points=list_points)

    assert(db.table_points_index_gist.check_count())
    assert (db.table_points_index_gist.check_records())
