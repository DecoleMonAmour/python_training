# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                               address="Somewhere over the rainbow", email="ivanivanov@ivan.com", bday="1", bmonth="January",
                               byear="2000"))
    app.session.logout()
