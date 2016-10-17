import requests, json, datetime

# Send initial request to get response with keys 'interval' and 'datestamp'
url = "http://challenge.code2040.org/api/dating"
r = requests.post(url, json = {'token' : 'f0b70d2efbd8fe9e76312ac0d1a68c16'})
data = json.loads(r.text)

# Store values from the dictionary into the dateGiven and interval variables
dateGiven = data["datestamp"]
interval = data["interval"]

# These values will be used to create a datetime object.
# Once we have the datetime object, we can use timedelta to add interval to our date
year = dateGiven[:4]
month = dateGiven[5:7]
day = dateGiven[8:10]
hour = dateGiven[11:13]
minute = dateGiven[14:16]
second = dateGiven[17:19]

# datetime object from the values of the ISO 8601 format we were given
isoToDatetime = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

# Add the interval to a the variable we will return, called datestamp
interval = datetime.timedelta(seconds=interval)
datestamp = isoToDatetime + interval
datestamp = datestamp.isoformat()

# Append "Z" to the end of the datestamp because the isoformat()
# function did not identically convert to the format we were given
datestamp += "Z"

# Send final request with token and the new date in identical format to what we were given
url = "http://challenge.code2040.org/api/dating/validate"
r = requests.post(url, json = {'token': 'f0b70d2efbd8fe9e76312ac0d1a68c16', 'datestamp' : datestamp})