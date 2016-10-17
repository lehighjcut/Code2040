import requests

# Send initial request to gather the response
url = "http://challenge.code2040.org/api/reverse"
r = requests.post(url, json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16'})

# Reverse the string passed in.
def reverseString(string):
    return string[::-1]

# Set the string that will be returned to the reversed string
newString = reverseString(r.text)

# Send new post request with the reversed string
url = "http://challenge.code2040.org/api/reverse/validate"
r = requests.post(url, json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16', 'string' : newString})