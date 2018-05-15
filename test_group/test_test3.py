_author__ = 'vden'


def test_test3(db):
    #print(db.mbt_hosts)
    #db.conn.connection()
    conn = db.conn.db_postgres()
    conn = db.conn.db_postgres()
    conn = db.conn.db_postgres()
    conn = db.conn.db_postgres()
    conn.close()

    conn=None

    conn = db.conn.db_write()
    conn = db.conn.db_write()
    conn = db.conn.db_write()
    conn = db.conn.db_write()
    conn = db.conn.db_write()
    conn.close()

