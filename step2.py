import requests

r = requests.post("http://challenge.code2040.org/api/reverse", json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16'})

print("Hello World")
print("sup brah")
print(r.text)
newString = ""

def reverseString(string):
    return string[::-1]

newString = reverseString(r.text)

r = requests.post("http://challenge.code2040.org/api/reverse/validate", json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16',
                                                                                'string' : newString})

