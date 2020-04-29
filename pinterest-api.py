import json
json_file = {}
for i in range(1995, 2021):
    date=str(i)
    json_file[date] = ''
print(json.dumps(json_file, sort_keys=True, indent=4))