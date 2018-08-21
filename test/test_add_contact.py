# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test1", middlename="Test", lastname="Test2", nickname="-", title="fdte", company="sderty", address="asdfghj", home="qwerty",
                               mobile="654321", work="4512368", fax="789456", email="1@1!.com", email2="1@1^.com", email3="1@1.com", homepage="---", byear="1988", ayear="2018",
                               address2="bhgyfte", phone2="852963", notes="rtyuioppm")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


