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
from models import Event
from handlers.BaseHandlers import BaseHandler


class EventHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('public/events.html', events=Event.all(), event_html=self.get_events_row)

    def get_event_html(self, input_event):
        return self.loader.load("events/event.html").generate(event=input_event)

    def get_events_row(self, input_events):
        events_html = [self.get_event_html(cur_event) for cur_event in input_events]
        return self.loader.load("events/event_row.html").generate(events="".join(events_html))
