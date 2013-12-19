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

'''

import datetime
from models import Event
from libs.Singleton import Singleton
from libs.FileHelpers import FileHelper

@Singleton
class DataGrabber(object):

    def __init__(self):
        pass

    def create_events_from_fb_org_file(self):
        ''' Creates events from the organizations found in fb data file '''
        organizations = FileHelper.get_organizations_from_file()

    def get_fb_time(self, input_fb_time):
        ''' Get Python datetime object from timestamp supplied by fb '''
        if 'T' in input_fb_time: #some of the times come back with only year, month, day
            return datetime.datetime.strptime(input_fb_time[:-5], '%Y-%m-%dT%H:%M:%S') #TODO get the timezone stuff figured out
        else:
            return datetime.datetime.strptime(input_fb_time, '%Y-%m-%d') #TODO get the timezone stuff figured out

    def get_event_from_fb_dict(self, input_dict):
        ''' Creates an Event instance from an event obtained from Facebook '''
        if not 'location' in input_dict:
            return None
        c_name = unicode(input_dict['name'])
        c_fb_id = int(input_dict['id'])
        c_location = unicode(input_dict['location'])
        c_is_date_only = input_dict['is_date_only'] if 'is_date_only' in input_dict else None
        if 'owner' in input_dict:
            c_owner_name = unicode(input_dict['owner']['name'])
            c_owner_fb_id = int(input_dict['owner']['id'])
        else:
            c_owner_name = None
            c_owner_fb_id = None
        c_privacy = unicode(input_dict['privacy']) if 'privacy' in input_dict else None
        c_start_time = self.get_fb_time(input_dict['start_time'])
        c_timezone = unicode(input_dict['timezone']) if 'timezone' in input_dict else None
        c_updated_time = self.get_fb_time(input_dict['updated_time']) if 'updated_time' in input_dict else None
        if 'venue' in input_dict:
            print(input_dict['venue'])
            c_venue_city = unicode(input_dict['venue']['city']) if 'city' in input_dict['venue'] else None
            c_venue_country = unicode(input_dict['venue']['country']) if 'country' in input_dict['venue'] else None
            c_venue_fb_id = int(input_dict['venue']['id']) if 'id' in input_dict['venue'] else None
            c_venue_lat = input_dict['venue']['latitude'] if 'latitude' in input_dict['venue'] else None
            c_venue_long = input_dict['venue']['longitude'] if 'longitude' in input_dict['venue'] else None
            c_venue_state = unicode(input_dict['venue']['state']) if 'state' in input_dict['venue'] else None
            c_venue_street = unicode(input_dict['venue']['street']) if 'street' in input_dict['venue'] else None
            c_venue_zip = unicode(input_dict['venue']['zip']) if 'zip' in input_dict['venue'] else None
            c_venue_name = unicode(input_dict['venue']['name']) if 'name' in input_dict['venue'] else None
        else:
            c_venue_city = None
            c_venue_country = None
            c_venue_fb_id = None
            c_venue_lat = None
            c_venue_long = None
            c_venue_state = None
            c_venue_street = None
            c_venue_zip = None
            c_venue_name = None
        c_end_time = self.get_fb_time(input_dict['end_time']) if 'end_time' in input_dict else None
        new_event = Event(
            name=c_name,
            fb_id=c_fb_id,
            location=c_location,
            is_date_only=c_is_date_only,
            owner_name=c_owner_name,
            owner_fb_id=c_owner_fb_id,
            privacy=c_privacy,
            start_time=c_start_time,
            timezone=c_timezone,
            updated_time=c_updated_time,
            venue_city=c_venue_city,
            venue_country=c_venue_country,
            venue_fb_id=c_venue_fb_id,
            venue_lat=c_venue_lat,
            venue_long=c_venue_long,
            venue_state=c_venue_state,
            venue_street=c_venue_street,
            venue_zip=c_venue_zip,
            venue_name=c_venue_name,
            end_time=c_end_time
        )
        return new_event
