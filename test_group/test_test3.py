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






