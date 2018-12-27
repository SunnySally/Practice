import json

f = open('subway.json', encoding='utf-8')
j = json.load(f)
path = j['path']
arr1 = []
for p in path:
    arr1.append([p['lng'], p['lat']])
obj = {}
obj['name'] = j['name']
obj['type'] = j['type']
obj['citycode'] = j['citycode']
obj['distance'] = j['distance']
stops = j['via_stops']
arr2 = []
for s in stops:
    ns = {}
    ns['name'] = s['name']
    ns['sequence'] = s['sequence']
    ns['location'] = [s['location']['lng'], s['location']['lat']]
    arr2.append(ns)
obj['path'] = arr1
obj['stops'] = arr2

with open('./NEWsubway.json', 'w', encoding='utf-8') as f:
    json.dump(obj, f)