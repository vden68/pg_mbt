_author__ = 'vden'


def test_test3(db):


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





