__author__ = 'vden'


def test_insert_commit_table_fibonacci_number(app, generator, db):
    i_fib = 1
    fib = generator.fibonacci.number(i_fib)
    while fib < 9223372036854775807:
        #str_ins = app.str_insert.str_insert_cfs_fib_bigint(str_v=fib, flag_not_printing=True)
        #app.connect.tfp_execute(conn=conn, str_ex=str_ins)

        db.table_fibonacci_number.insert(fib_number=fib)

        i_fib = i_fib + 1
        fib = generator.fibonacci.number(i_fib)
        print('i_fib=', i_fib, 'fib=', fib)

