import json
var= open('dwsample1-json.json')
data = json.load(var)
for i in data['nehal']:
	print(i)

var.close()


# import json
# json_data='{"fruit":"banana","size":"normal","color":"yellow","city":"bhavnagar"}'
# var=json.loads(json_data)
# print('json data',var)
# print()

# f=open('dwsample1-json.json','r')
# data=json.loads(f.read())
# for i in data['details']:
# 	print(i)

# f.close()