# coding=utf-8
# Copyright 2018-2020 EVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio

from src.postmaster.postmaster import start_server

from src.configuration.configuration_manager import ConfigurationManager

from src.utils.logging_manager import Logger
from src.utils.logging_manager import LoggingLevel


def eva():
    """
        Start the eva system
    """

    # Get the hostname and port information from the configuration file
    config = ConfigurationManager()
    hostname = config.get_value('core', 'hostname')
    port = config.get_value('core', 'port')

    # Launch postmaster
    try:
        asyncio.run(start_server(hostname=hostname,
                                 port=port)
                    )

    except Exception as e:
        Logger().log(e, LoggingLevel.CRITICAL)
