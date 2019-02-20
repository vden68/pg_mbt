



def test_drop_all_tables(db):
    list_model=db.finishing_checks.get_list_tables()
    print("list_model=",list_model, len(list_model))

    db.finishing_checks.drop_tables(list_model=list_model)

