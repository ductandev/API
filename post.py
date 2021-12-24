from requests import get, post
from json import dumps, loads, dump, load

url = 'https://gateway.systemkul.com/api/Gateway/GetListPeopleByUnit'

data_request_new = {
  "requestKey": "66540EEE-61D6-48E2-B9B6-61BA0228B0FD",
  "unitCode": "vietthang"
}
r = post(url, timeout=10, data=dumps(data_request_new), headers={'Content-Type': 'application/json', })
print(r.status_code)
print(r.json())

data_getway = loads(r.text)

with open('data3.json', 'w') as f_getway:
    dump(data_getway, f_getway)
    
    