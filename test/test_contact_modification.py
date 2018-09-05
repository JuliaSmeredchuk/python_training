# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_modify_some_contact(app, db, check_ui):
    contact = Contact(firstname="New", middlename="New name", lastname="New", mobile="1111111", notes="notes")
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    old_contacts.remove(random_contact)
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(random_contact.id, contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
