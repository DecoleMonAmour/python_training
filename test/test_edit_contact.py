# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov",
                               address="Pupkina-Lupkina str.", email="petrovpetr", bday="2", bmonth="February",
                               byear="2002"))