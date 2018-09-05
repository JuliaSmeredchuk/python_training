# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    group = Group(name="New_name", header="New_header", footer="New_footer")
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    old_groups.remove(random_group)
    group.id = random_group.id
    app.group.modify_group_by_id(random_group.id, group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#   old_groups = app.group.get_group_list()
#   app.group.modify_first_group(Group(header="New header"))
#   new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)


#def test_modify_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="New footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_group_modification(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="1", header="1", footer="1"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

