#!/usr/bin/python
 
import requests,json
cookies = {"spip_session": "145667_3537d30ca3754d33c7038cd194a8fa9b"}
resp = requests.get("https://api.www.root-me.org/challenges/5", cookies=cookies)
if resp.status_code != 200:
    raise Exception("GET /challenges/ {}".format(resp.status_code))
data = resp.json()
print(json.dumps(data, indent=4, sort_keys=True)) 