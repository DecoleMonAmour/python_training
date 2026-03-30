# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):  # тестовый метод, принимающий в качестве параметра фикстуру и вызывающий в ней вспомогательные методы
    app.group.create(Group(name="new group", header="qqqqq", footer="wwwww"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
