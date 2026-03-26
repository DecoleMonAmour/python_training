# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()  # создает фикстуру (объект типа Application)
    request.addfinalizer(fixture.destroy)  # указание на то, как эта фикстура должна быть разрушена
    return fixture


def test_add_group(app):  # тестовый метод, принимающий в качестве параметра фикстуру и вызывающий в ней вспомогательные методы
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="new group", header="qqqqq", footer="wwwww"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
