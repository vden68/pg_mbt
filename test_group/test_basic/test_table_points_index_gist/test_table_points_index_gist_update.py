__author__ = 'vden'
import pytest
import allure

@pytest.mark.test_basic
@allure.step('test_table_points_index_gist_update')
def test_table_points_index_gist_update(db, generator):
    print("\n\ntest_table_points_index_gist_update \n\n")

    #cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(5):
        list_points = generator.p_points.g_points(coumt_points=100)

        with allure.step('insert in the table the points index gist %s' % list_points):
            db.table_points_index_gist.insert(list_points=list_points)



        #test_table_points_index_gist_update
        with allure.step('update id more than number'):
            db.table_points_index_gist.update_id_random()

    assert(db.table_points_index_gist.check_count())
    assert (db.table_points_index_gist.check_records())
