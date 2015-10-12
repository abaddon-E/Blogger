#-*- coding: utf-8 -*-
from datetime import datetime
from mongoengine import *


class Social(EmbeddedDocument):
    username = StringField()
    apiKey = StringField()


class User(Document):
    """
    users model object
    """

    email = StringField()
    password = StringField()

    fullname = StringField()
    socials = EmbeddedDocumentListField(Social)

    # group --> 1 => admin, 2 => manager, 3 => user
    group = IntField(default=3)
    created = DateTimeField(default=datetime.now)

    def can(self, role):
        roles = ['login']
        if self.group == 1:
            roles.append('admin')
        if role in roles:
            return True
