# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Julia", middlename="Vladimirovna", lastname="Smeredchuk", nickname="-", title="fdte", company="sderty", address="asdfghj", home="qwerty",
                            mobile="89257789625", work="4512368", fax="789456", email="1@1.com", email2="1@1.com", email3="1@1.com", homepage="---", byear="1988", ayear="2018",
                            address2="bhgyfte", phone2="rteyuimn", notes="rtyuioppm"))
    app.logout()

