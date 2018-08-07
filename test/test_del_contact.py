from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.go_to_add_new_page()
        app.contact.create(Contact(firstname="test"))
    app.contact.delete_first_contact()
