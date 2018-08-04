# -*- coding: utf-8 -*-
from model.contact_modification import Editing

def test_contact_modification(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification(Editing(firstname="1", middlename="2", lastname="3", mobile="1111111", notes="jhggfd"))
    app.session.logout()
