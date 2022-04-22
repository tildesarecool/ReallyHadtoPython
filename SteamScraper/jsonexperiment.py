import json

json1 = '''{"platform":"Nokia", "ip":"1.1.1.1"},{"platform":"Nokia", "ip":"1.1.1.1"}'''

#dict1 = json.loads(json1)

#print(type(dict1))

#json2 = json.dumps(dict1, indent=4)

#print("json2 is " + str(type(json2)))

#print(json2)

#print(dict1.get('ip'))

#json3 = json.loads(json2)

#print("json3 is " + str(type(json3)))
#print(json3)
#print(json3.get('ip'))

GameDict = '{"appid":1025480,"name":"1-Bit Revival: The Residuals of Null","app_type":1,"logo":"https://cdn.akamai.steamstatic.com/steam/apps/1025480/capsule_184x69.jpg","friendlyURL":1025480,"availStatLinks":{"achievements":true,"global_achievements":true,"stats":false,"gcpd":false,"leaderboards":false,"global_leaderboards":false},"hours_forever":"0.6","last_played":1642216987},{"appid":1025480,"name":"1-Bit Revival: The Residuals of Null","app_type":1,"logo":"https://cdn.akamai.steamstatic.com/steam/apps/1025480/capsule_184x69.jpg","friendlyURL":1025480,"availStatLinks":{"achievements":true,"global_achievements":true,"stats":false,"gcpd":false,"leaderboards":false,"global_leaderboards":false},"hours_forever":"0.6","last_played":1642216987}'

print(type(GameDict))
jsonGame1 = json.loads(GameDict)
print(type(jsonGame1))

print(jsonGame1.get("app_type"))

json4 = { }

json4.values()

print('the values are: ')
print(jsonGame1.values())