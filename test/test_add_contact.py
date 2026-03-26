# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()  # создает фикстуру (объект типа Application)
    request.addfinalizer(fixture.destroy)  # указание на то, как эта фикстура должна быть разрушена
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                   address="Somewhere over the rainbow", email="ivanivanov@ivan.com", bday="1", bmonth="January",
                   byear="2000"))
    app.logout()
