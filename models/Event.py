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
import time
import datetime

from os import urandom
from pbkdf2 import PBKDF2
from sqlalchemy import Column, ForeignKey, cast, and_
from sqlalchemy.orm import synonym, relationship, backref
from sqlalchemy.types import Unicode, String, BigInteger, Boolean, DateTime, Float 
from models import dbsession
from models.BaseModels import DatabaseObject
from pytz import timezone


class Event(DatabaseObject):
    ''' Event definition '''

    name = Column(Unicode(256), unique=False, nullable=False)
    fb_id = Column(BigInteger(), unique=True, nullable=False)
    location = Column(Unicode(256), unique=False, nullable=False)
    is_date_only = Column(Boolean(), unique=False, nullable=True)
    owner_name = Column(Unicode(256), unique=False, nullable=True)
    owner_fb_id = Column(BigInteger(), unique=False, nullable=True)
    privacy = Column(Unicode(10), unique=False, nullable=True)
    start_time = Column(DateTime(), unique=False, nullable=False)
    timezone = Column(Unicode(64), unique=False, nullable=True)
    updated_time = Column(DateTime(), unique=False, nullable=True)
    venue_city = Column(Unicode(64), unique=False, nullable=True)
    venue_country = Column(Unicode(64), unique=False, nullable=True)
    venue_fb_id = Column(BigInteger(), unique=False, nullable=True)
    venue_lat = Column(Float(), unique=False, nullable=True)
    venue_long = Column(Float(), unique=False, nullable=True)
    venue_state = Column(Unicode(64), unique=False, nullable=True)
    venue_street = Column(Unicode(64), unique=False, nullable=True)
    venue_zip = Column(Unicode(10), unique=False, nullable=True)
    venue_name = Column(Unicode(256), unique=False, nullable=True)
    end_time = Column(DateTime(), unique=False, nullable=True)

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

    @classmethod
    def by_datetime(cls, input_datetime):
        ''' Returns all events for the day depicted by input_datetime '''
        day = input_datetime.date()
        next_day = day + datetime.timedelta(days=1)
        return dbsession.query(cls).filter(
            and_(cls.start_time >= day, cls.start_time < next_day)
        ).all()

    @classmethod
    def for_today(cls):
        ''' Returns all events for today '''
        return Event.by_datetime(datetime.datetime.now(timezone("US/Eastern")))

    @property
    def maps_search_string(self):
        to_return = self.get_venue_name()
        for cur_val in [self.venue_street, self.venue_city, self.venue_state, self.venue_zip]:
            if cur_val:
                to_return += " %s" % cur_val
        return to_return

    @property
    def time_string(self):
        to_return = self.start_time.strftime("%I:%M%p")
        if self.end_time is not None:
            to_return += " - %s" % self.end_time.strftime("%I:%M%p")
        return to_return

    def get_venue_name(self): #TODO turn these into properties
        if self.venue_name is not None:
            return self.venue_name
        else:
            return self.location

    def get_venue_name_abbrev(self, input_length):
        v_name = self.get_venue_name()
        if len(v_name) > input_length:
            return v_name[:input_length-3] + "..."
        else:
            return v_name

    def get_address_first_line(self):
        if self.venue_street is not None:
            return self.venue_street
        else:
            return "Not available"

    def get_address_first_line_abbrev(self, input_length):
        f_line = self.get_address_first_line()
        if len(f_line) > input_length:
            return f_line[:input_length-3] + "..."
        else:
            return f_line

    def get_address_second_line(self):
        if self.venue_street is not None:
            return "%s, %s %s" % (self.venue_city, self.venue_state, self.venue_zip)
        else:
            return ""

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Event - name: %s>' % (self.name,)