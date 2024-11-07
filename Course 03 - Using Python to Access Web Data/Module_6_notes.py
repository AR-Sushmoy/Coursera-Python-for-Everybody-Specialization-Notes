'''
Video: 13.5
Topic: JavaScript Object Notation (JSON)
'''


'''
JSON represents data as nested "lists" and "dictionaries".
'''
import json

data1 = '''{
    "name": "Sushmoy",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data1) # loads() -> Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object.

print(info)
'''
Output: 
{'name': 'Sushmoy', 'phone': {'type': 'intl', 'number': '+1 734 303 4456'}, 'email': {'hide': 'yes'}}
'''

print('Name:', info['name']) # Name: Sushmoy

print('Phone:', info['phone']['number']) # Phone: +1 734 303 4456




user_input = '''[
 {  "id" : "001",
    "x" : "2",
    "name" : "Chuck"
 },
 {  "id" : "009",
    "x" : "7",
    "name" : "Tuck"
 }
]'''

data2 = json.loads(user_input)

print('User Count:', len(data2)) # Output: 2

for item in data2:
    print('Name: ', item['name'])
    print('ID: ', item['id'])
    print('Attribute: ', item['x'])

'''
Output:
 
Name:  Chuck
ID:  001
Attribute:  2
Name:  Tuck
ID:  009
Attribute:  7
'''











'''
Video: 13.7
Topic: Application Programming Interfaces (APIs)
'''



'''
# Accessing JSON Data form a API
'''


import urllib.request, urllib.error, urllib.parse
import http, ssl

serviceUrl = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter Location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    print(parms)

    url = serviceUrl + urllib.parse.urlencode(parms) # urlencode() is being used to append properly encoded parameters to the end of a URL -> https://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI

    print('Retriving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrived', len(data), 'characters', data[:20].replace('\n', ' ')) # Output: Retrived 1318 characters {"type":"FeatureColl

    js = json.loads(data)

    # print(json.dumps(js, indent=4))

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon) # Output: lat 42.2813722 lon -83.7484616
    location = js['features'][0]['properties']['formatted']
    print(location) # Output: Ann Arbor, MI, United States of America
 












'''
Video: Worked Example: OpenStreetMap API (Chapter 13)
'''


'''
The act of going from a text address to a location is called geocoding.
'''