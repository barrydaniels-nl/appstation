import json 
with open('configure.json') as json_file:
    data = json.load(json_file)
    
print(data)
