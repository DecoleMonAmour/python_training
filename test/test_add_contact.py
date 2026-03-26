# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                               address="Somewhere over the rainbow", email="ivanivanov@ivan.com", bday="1", bmonth="January",
                               byear="2001"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                               address="", email="", bday="-", bmonth="-",
                               byear=""))
    app.session.logout()