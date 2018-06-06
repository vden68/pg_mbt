_author__ = 'vden'


def test_test3(app,db):

    print()
    print("mbt_hosts=", app.mbt_hosts)
    print("mbt_hosts_write=", app.mbt_hosts_write)
    print("mbt_hosts_read=", app.mbt_hosts_read)
    print("mbt_conn=", app.mbt_conn)



    print("Connect db_superuser")
    conn = db.conn.db_superuser()
    conn = db.conn.db_superuser()
    conn = db.conn.db_superuser()
    conn = db.conn.db_superuser()
    conn.close()

    conn=None

    print( "Connect db_write")
    conn = db.conn.db_write()
    conn = db.conn.db_write()
    conn = db.conn.db_write()
    conn = db.conn.db_write()
    conn = db.conn.db_write()
    conn.close()

    conn = None

    print( "Connect db_read")
    conn = db.conn.db_read()
    conn = db.conn.db_read()
    conn = db.conn.db_read()
    conn = db.conn.db_read()
    conn.close()


    print()
    print("mbt_hosts=", app.mbt_hosts)
    print("mbt_hosts_write=", app.mbt_hosts_write)
    print("mbt_hosts_read=", app.mbt_hosts_read)
    print("mbt_conn=", app.mbt_conn)

    db.table_fibonacci_number.insert(fib_number=123456)
    db.table_fibonacci_number.insert(fib_number=234567)
    db.table_fibonacci_number.insert(fib_number=345678)
    db.table_fibonacci_number.insert(fib_number=456789)
    db.table_fibonacci_number.insert(fib_number=567890)

    print(db.table_fibonacci_number.get_list_table_fibonacci_number())






