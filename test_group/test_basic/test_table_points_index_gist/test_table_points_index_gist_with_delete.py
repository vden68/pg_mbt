__author__ = 'vden'
import pytest
import allure

@pytest.mark.test_basic
@allure.step('test_table_points_index_gist_with_delete')
def test_table_points_index_gist_with_delete(db, generator):
    print("\n\ntest_table_points_index_gist_with_delete \n\n")

    if db.table_points_index_gist.get_count_table_points_index_gist()<100:
        list_points = generator.p_points.g_points(coumt_points=10000)
        with allure.step('insert in the table the points index gist %s' % list_points):
            db.table_points_index_gist.insert(list_points=list_points)


    for x in range(10):
        with allure.step('delete 2 percent of rows'):
            db.table_points_index_gist.delete_2_percent_of_rows()

        assert(db.table_points_index_gist.check_count())
        assert (db.table_points_index_gist.check_records())
