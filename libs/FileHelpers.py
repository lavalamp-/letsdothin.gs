# -*- coding: utf-8 -*-
'''
@author: lavalamp

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


import logging
import json
from libs.ConfigManager import ConfigManager


class FileHelper(object):
    
    @staticmethod
    def get_organizations_from_file():
        ''' Gets the JSON object containing an org list from the configured file '''
        config = ConfigManager.instance()
        with open(config.fb_organization_file, 'r') as f:
            return json.loads(f.read())