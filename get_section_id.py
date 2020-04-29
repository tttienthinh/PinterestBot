import urllib.request
import json

request = urllib.request.Request('https://www.pinterest.fr/journaldespace/journal-nasa/1995/')
try:
    response = urllib.request.urlopen(request)
except:
    print("something wrong")

print(type(response))

htmlBytes = response.read()

print(type(htmlBytes))

htmlStr = htmlBytes.decode("utf8")

print(type(htmlStr))
print(htmlStr)
htmlSplit = htmlStr.split('<script id="initial-state" type="application/json">')
htmlSplit = htmlSplit[1].split('</script>')
json_file = json.loads(htmlSplit[0])

print(type(htmlSplit))
print(len(htmlSplit))
# print(json.dumps(json_file, sort_keys=True, indent=4))