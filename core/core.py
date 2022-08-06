#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import requests
from rich import print
from rich import print_json

token = 'vk1.a.j5Nig09jcaELbyAkC4-apZMkbq0pxJOto2RtH7TWj-fEJBb9O-RmNWDUGOR7xfN6A7DIpjetlaP_R9fLFHP8dCPnmXsYIK6f-qHKtiTbPKYXFZKtiP6ykxbwDlXx72cdhn0RuZAelto21SedE9xJIM7oSCctS0jnAZZgH1I8r61HtRoAK_6UUTE6Ds3KTXaf'
user_id = '660621363'

headers = {
    'User-Agent':
    'Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://dev.vk.com/method/friends.get',
    'Origin': 'https://dev.vk.com',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
}

params = {
    'fields': 'bdate,city'
}
