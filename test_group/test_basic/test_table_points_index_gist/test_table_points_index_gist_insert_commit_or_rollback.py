__author__ = 'vden'
import pytest
import allure
import random
from model.basic_tables.table_points_index_gist import Table_points_index_gist

@pytest.mark.test_basic
@allure.step('test_table_points_index_gist_insert_commit_or_rollback')
def test_table_points_index_gist_insert_commit_or_rollback(db, generator):
    print("\n\ntest_table_points_index_gist_insert_commit_or_rollback \n\n")

    cycle_factor = db.app.mbt_conn.cycle_factor
    list_points = generator.p_points.g_points(coumt_points=800*cycle_factor)

    for x in list_points:
        #print(x)
        with allure.step('insert in the table the points index gist %s' % x):
            list_table_points = []
            list_table_points.append(Table_points_index_gist(p_point_x=x.p_point_x, p_point_y=x.p_point_y))
            com_or_ron = random.randint(0, 1)
            if com_or_ron == 0:
                db.table_points_index_gist.insert(list_points=list_table_points)
            else:
                db.table_points_index_gist.insert(list_points=list_table_points, commit=False)

    assert(db.table_points_index_gist.check_count())
    assert(db.table_points_index_gist.check_records())
