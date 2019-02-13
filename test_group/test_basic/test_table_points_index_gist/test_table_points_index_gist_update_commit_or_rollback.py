__author__ = 'vden'
import pytest
import allure
import random

@pytest.mark.test_basic
@allure.step('test_table_points_index_gist_update_commit_or_rollback')
def test_table_points_index_gist_update_commit_or_rollback(db, generator):
    print("\n\ntest_table_points_index_gist_update_commit_or_rollback \n\n")

    #cycle_factor = db.app.mbt_conn.cycle_factor
    for x in range(10):
        list_points = generator.p_points.g_points(coumt_points=1000)

        with allure.step('insert in the table the points index gist %s' % list_points):
            db.table_points_index_gist.insert(list_points=list_points)



        #test_table_points_index_gist_update
        with allure.step('update id more than number'):
            com_or_ron = random.randint(0, 1)
            if com_or_ron == 0:
                db.table_points_index_gist.update_id_random()
            else:
                db.table_points_index_gist.update_id_random(commit=False)


    assert(db.table_points_index_gist.check_count())
    assert (db.table_points_index_gist.check_records())
