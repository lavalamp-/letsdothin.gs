# -*- coding: utf-8 -*-
'''
@author: lavalamp-

    Copyright 2013

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
----------------------------------------------------------------------------

This file contiains the user object, used to store data related to an
indiviudal event

'''


import logging

from os import urandom
from pbkdf2 import PBKDF2
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import synonym, relationship, backref
from sqlalchemy.types import Unicode, String 
from models import dbsession, Permission
from models.BaseModels import DatabaseObject


class Event(DatabaseObject):
    ''' Event definition '''

    name = Column(Unicode(256), unique=False, nullable=False)
    fb_id = Column(BigInteger(), unique=True, nullable=False)
    location = Column(Unicode(256), unique=False, nullable=False)
    is_date_only = Column(Boolean(), unique=False, nullable=True)
    owner_name = Column(Unicode(256), unique=False, nullable=True)
    owner_fb_id = Column(BigInteger(), unique=False, nullable=True)
    privacy = Column(Unicode(10), unique=False, nullable=True)
    start_time = Column(Date(), unique=False, nullable=False)
    timezone = Column(Unicode(64), unique=False, nullable=True)
    updated_time = Column(Date(), unique=False, nullable=True)
    venue_city = Column(Unicode(64), unique=False, nullable=False)
    venue_country = Column(Unicode(64), unique=False, nullable=False)
    venue_fb_id = Column(BigInteger(), unique=False, nullable=False)
    venue_lat = Column(Float(), unique=False, nullable=False)
    venue_long = Column(Float(), unique=False, nullable=False)
    venue_state = Column(Unicode(64), unique=False, nullable=False)
    venue_street = Column(Unicode(64), unique=False, nullable=False)
    venue_zip = Column(Unicode(10), unique=False, nullable=False)
    name = Column(Unicode(256), unique=False, nullable=False)
    end_time = Column(Date(), unique=False, nullable=True)

    # name = Column(Unicode(16), unique=True, nullable=False)
    # _password = Column('password', String(64))
    # password = synonym('_password', descriptor=property(
    #     lambda self: self._password,
    #     lambda self, password: setattr(
    #             self, '_password', self.__class__._hash_password(password))
    # ))
    # permissions = relationship("Permission", 
    #     backref=backref("User", lazy="select"), 
    #     cascade="all, delete-orphan"
    # )

    @classmethod
    def all(cls):
        ''' Returns a list of all objects in the database '''
        return dbsession.query(cls).all()

    @classmethod
    def by_id(cls, identifier):
        ''' Returns a the object with id of identifier '''
        return dbsession.query(cls).filter_by(
            id=identifier
        ).first()

    @classmethod
    def by_name(cls, event_name):
        ''' Returns a the object with event name of event_name '''
        return dbsession.query(cls).filter_by(
            name=unicode(event_name)
        ).first()

    # def validate_password(self, attempt):
    #     ''' Check the password against existing credentials '''
    #     if self._password is not None:
    #         return self.password == PBKDF2.crypt(attempt, self.password)
    #     else:
    #         return False

    # def __str__(self):
    #     return self.name

    # def __repr__(self):
    #     return '<User - name: %s>' % (self.name,)
