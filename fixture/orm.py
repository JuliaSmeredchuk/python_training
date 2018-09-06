from pony.orm import *
#from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:
    db = Database()  #объект, на основании которого строится привязка
#привязка строится в виде набора классов

    class ORMGroup(db.Entity): #класс описывает объекты, которые сохраняются в базу данных
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id') #обязательное поле, по которому идентифицируются объекты
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')

    def __init__(self, host, name, user, password):#привязка к базе данных
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()    #происходит сопоставление св-в описанных классов с таблицами и полями этих таблиц
    sql_debug(True)


    def convert_groups_to_model(self, groups):  #преобразование объекта типа ORMGroup в тип просто Group
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session  #метка того, что функция выполняется в рамках сессии
    def get_group_list(self):  #реализуем функции, кот. получают списки объектов
        return self.convert_groups_to_model(select (g for g in ORMFixture.ORMGroup))

    @db_session  #метка того, что функция выполняется в рамках сессии
    def get_contact_list(self):  #реализуем функции, кот. получают списки объектов
        return self.convert_contacts_to_model(select (c for c in ORMFixture.ORMContact if c.deprecated is None))

    def convert_contacts_to_model(self, contacts):  #преобразование объекта типа ORMGroup в тип просто Group
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))
