#!/usr/bin/env python3

import requests

resp = requests.get('https://dev.azure.com/gannonbrian')

if resp.status_code != 200:
    raise ApiError('GET /gannonbrian/ {}'.format(resp.status_code))
for stuff in resp.json():
    print('{} {}'.format(stuff['id'], stuff['summary']))
