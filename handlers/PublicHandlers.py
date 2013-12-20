# -*- coding: utf-8 -*-
'''
@author: moloch

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
'''

from tornado import template
import datetime
from models import Event
from handlers.BaseHandlers import BaseHandler
from pytz import timezone


class EventHandler(BaseHandler):

    def get(self, *args, **kwargs):
        if 'day' in kwargs:
            try:
                event_day = datetime.datetime.strptime(kwargs['day'], "%y-%m-%d")
                self.render('public/events.html', events=Event.by_datetime(event_day), event_html=self.get_events_row)
            except ValueError:
                self.render('errors/404.html')
        elif 'day_word' in kwargs:
            if kwargs['day_word'] == 'today':
                self.render('public/events.html', events=Event.for_today(), event_html=self.get_events_row)
            elif kwargs['day_word'] == 'tomorrow':
                self.render('public/events.html', events=Event.by_datetime(datetime.datetime.now(timezone("US/Eastern")) + datetime.timedelta(days=1)), event_html=self.get_events_row)
            elif kwargs['day_word'] == 'dat':
                self.render('public/events.html', events=Event.by_datetime(datetime.datetime.now(timezone("US/Eastern")) + datetime.timedelta(days=2)), event_html=self.get_events_row)
            else:
                self.render('errors/404.html')
        else:
            self.render('public/events.html', events=Event.for_today(), event_html=self.get_events_row)

    def get_event_html(self, input_event):
        return self.loader.load("events/event.html").generate(event=input_event)

    def get_events_row(self, input_events):
        events_html = [self.get_event_html(cur_event) for cur_event in input_events]
        return self.loader.load("events/event_row.html").generate(events="".join(events_html))
