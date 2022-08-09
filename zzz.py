#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

import vk_api

from core.core import *

vk_session = vk_api.VkApi(login, password)

try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print(error_msg)
