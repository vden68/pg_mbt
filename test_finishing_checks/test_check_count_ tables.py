



def test_check_count_tables(db):
    list_model=db.finishing_checks.get_list_tables()
    print("list_model=",list_model, len(list_model))

    for selected_node in db.app.mbt_hosts_read:
        if selected_node.node_id==1:
            continue
        else:
            list_node = db.finishing_checks.get_list_tables(selected_node=selected_node)
            print("selected_node.node_id=",selected_node.node_id, "list_node=", list_node)
            assert (list_model==list_node)


