import requests, json

# Send initial request to get response with keys 'needle' and 'haystack'
url = "http://challenge.code2040.org/api/haystack"
r = requests.post(url, json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16'})
data = json.loads(r.text)

# Store the haystack and needle value from the dictionary
haystack = data["haystack"]
needle = data["needle"]

index = 0
# Loop through the haystack to check if any values are equivalent to the needle
# When we find a match, we break and the value of index is the value we return
for index in range(len(haystack)):
    if (haystack[index] == needle):
        break

# Send final request with token and index of the needle
url = "http://challenge.code2040.org/api/haystack/validate"
r = requests.post(url, json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16', 'needle' : index})
