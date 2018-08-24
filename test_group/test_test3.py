#from test_group.test_basic.test_table_fibonacci_number_insert_commit import mbt_test_table_fibonacci_number_insert_commit
from test_group.test_basic.test_table_fibonacci_number_insert_commit_or_rollback import mbt_test_table_fibonacci_number_insert_commit_or_roll

import pytest


def test_t3(generator, db):
    t3_list=[]
    #t3_list.append(mbt_test_table_fibonacci_number_insert_commit)
    #t3_list.append(mbt_test_table_fibonacci_number_insert_commit_or_roll)
    print("t3_list=", t3_list)
    for t3 in t3_list:
        print("t3=", t3)
        t3(generator, db)
        "%s(generator, db)" % t3
    #mbt_test_table_fibonacci_number_insert_commit(generator, db)
    #print("mbt_test_table_fibonacci_number_insert_commit")
    #mbt_test_table_fibonacci_number_insert_commit_or_roll(generator, db)
    #print("mbt_test_table_fibonacci_number_insert_commit_or_roll")

