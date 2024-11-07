'''
Assignments 14.2: In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/opengeo.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first plus_code from the JSON.

API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Open Street Map Data.

http://py4e-data.dr-chuck.net/opengeo?

This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.

To call the API, you need to provide the address that you are requesting as the q= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/opengeo.py
'''

import urllib.request, urllib.parse, urllib.error
import json

serviceUrl = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter Location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceUrl + urllib.parse.urlencode(parms)
    print('Retriving', url)

    uh = urllib.request.urlopen(url)
    location = uh.read().decode()

    print('Retrieved', len(location))

    js = json.loads(location)
    # print(json.dumps(js, indent=4))

    print('Plus code', js['features'][0]['properties']['plus_code'])