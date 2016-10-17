import requests, json

# Send initial request to get response with keys 'prefix' and 'array'
url = "http://challenge.code2040.org/api/prefix"
r = requests.post(url, json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16'})
data = json.loads(r.text)

# Store values from the dictionary into a prefix and an array we will loop through
prefix = data["prefix"]
givenArray = data["array"]

# This is the array we will append() all values that do not begin with the prefix
array = []

# Loop through the array we were given, if the prefix is not in the word, add it to our array
for givenArrayIndex in range(0, len(givenArray)):
    word = givenArray[givenArrayIndex]
    if prefix[0:len(prefix)] != word[0:len(prefix)]:
        array.append(word)

# Finally, POST our array with all the values that do not begin with the prefix
url = "http://challenge.code2040.org/api/prefix/validate"
r = requests.post(url, json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16', 'array' : array})
