"""How to read data from a json format source"""

import requests

"""API --> Application Programming Interface: usually the raw data is returned under the API, eg: api.twitter.com"""  # noqa
"""JSON --> JavaScript Object Notation: it is started in JavaScript but now used in any programming language"""  # noqa

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print('Response received: ', response)
print('\n---Json Data---')
print(json)

print('----The people currently in space are: ----')
for people in json['people']:
    print(people['name'])
