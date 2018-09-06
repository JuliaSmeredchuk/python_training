from model.contact import Contact
#import re
#from random import randrange

#def test_contact_check(app):
    #all_contacts = app.contact.get_contact_list()
    #index = randrange(len(all_contacts))
    #contact_from_home_page = app.contact.get_contact_list()[index]
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    #assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    #assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    #assert contact_from_home_page.address == contact_from_edit_page.address


def test_contact_check(app, db):
    contacts_ui = app.contact.get_contact_list()
    contacts_db = db.get_contact_list()
    assert sorted(contacts_ui, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)



