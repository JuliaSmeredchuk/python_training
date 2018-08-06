# -*- coding: utf-8 -*-
from model.group_modification import Modification
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="New footer"))


def test_group_modification(app):
    app.group.modification(Modification(name="1", header="1", footer="1"))
