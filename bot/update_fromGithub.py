import json
obj = json.load(open('data.json'))
obj['name']='jyoti'
json.dump(obj,open('data.json','w'))