# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Julia", middlename="Vladimirovna", lastname="Smeredchuk", nickname="-", title="fdte", company="sderty", address="asdfghj", home="qwerty",
                               mobile="89257789625", work="4512368", fax="789456", email="1@1.com", email2="1@1.com", email3="1@1.com", homepage="---", byear="1988", ayear="2018",
                               address2="bhgyfte", phone2="rteyuimn", notes="rtyuioppm")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


