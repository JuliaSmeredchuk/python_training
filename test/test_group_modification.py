# -*- coding: utf-8 -*-
from model.group_modification import Modification

def test_group_modification(app):
    app.group.modification(Modification(name="1", header="1", footer="1"))

