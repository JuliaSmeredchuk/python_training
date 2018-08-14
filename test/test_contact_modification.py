# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New", middlename="New name", lastname="3", mobile="1111111", notes="notes"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
