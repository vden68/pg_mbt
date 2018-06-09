__author__ = 'vden'


def test_insert_commit_table_fibonacci_number(app, generator, db):

    i_fib = 1
    fib = generator.fibonacci.number(i_fib)

    while fib < 9223372036854775807:

        db.table_fibonacci_number.insert(fib_number=fib)

        i_fib = i_fib + 1
        fib = generator.fibonacci.number(i_fib)
        print('i_fib=', i_fib, 'fib=', fib)

    get_list=db.table_fibonacci_number.get_list()
    print(get_list)

    assert(db.table_fibonacci_number.check_count())

