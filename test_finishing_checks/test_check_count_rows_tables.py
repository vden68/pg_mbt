



def test_check_count_rows_tables(db):
    list_model=db.finishing_checks.get_list_tables()
    print("list_model=",list_model, len(list_model))

    node_x=0
    for selected_node in db.app.mbt_hosts_read:
        if node_x==0:
            list_model = db.finishing_checks.get_list_rows_tables(selected_node=selected_node, list_model=list_model)
            print("list_model=", list_model, len(list_model))
            node_x=1
        list_node = db.finishing_checks.get_list_rows_tables(selected_node=selected_node,  list_model=list_model)
        print("selected_node.node_id=",selected_node.node_id, "list_node=", list_node)
        assert (list_model==list_node)


