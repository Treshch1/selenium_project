def test_waiting_after_removing_items_from_cart(app):
    app.open_main_site()
    while app.get_cart_quntity() < 3:
        app.add_item_to_the_cart()
    app.open_cart()
    while app.is_image_displayed():
        table_element = app.get_table_element()
        app.remove_item_from_cart()
        app.wait_until_element_become_changed(table_element)
