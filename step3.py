import requests, json

r = requests.post("http://challenge.code2040.org/api/haystack", json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16'})
data = json.loads(r.text)
print(r.text)
haystack = data["haystack"]
needle = data["needle"]

index = 0

for index in range(len(haystack)):
    if (haystack[index] == needle):
        break

print(index)
r = requests.post("http://challenge.code2040.org/api/haystack/validate", json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16',
                                                                                'needle' : index})
