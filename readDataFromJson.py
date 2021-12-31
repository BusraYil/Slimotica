import json

#Read file
myJsonFile = open('database\example_database.json', 'r')              
JsonData = myJsonFile.read()

#parse Json data
obj = json.loads(JsonData)

#print(str(obj['nodes']))
#print(str(obj['UUID']))
#print(str(obj['name']))

list = obj['nodes']
print(list)
print(len(list))

for i in range(len(list)):
    print("Nodes of", i, "is....")
    print("Devicekey:", list[i].get("deviceKey"))
    print("UUID:", list[i].get("UUID"))
    print("name:", list[i].get("name"))
