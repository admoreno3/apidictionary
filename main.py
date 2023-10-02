#rest apis
#application programming interface
import requests  #request something from
#the internet
import json  #json stands for java script object notation

response = requests.get("https://randomuser.me/api/")
#print(response.json())
gender = response.json()['results'][0]['gender']
print(gender)
title = response.json()['results'][0]['name']['title']
print(title)
fname = response.json()['results'][0]['name']['first']
lname = response.json()['results'][0]['name']['last']
print(fname)
print(lname)
email = response.json()['results'][0]["email"]
print(email)
number = response.json()['results'][0]['phone']
print(number)
city = response.json()['results'][0]['location']['city']
print(city)
pcode = response.json()['results'][0]['location']['postcode']
print(pcode)
address = response.json()['results'][0]['location']['street']
print(address)
dob = response.json()["results"][0]["dob"]["date"]
print(dob)
id = response.json()['results'][0]["login"]["uuid"]
print(id)
age = response.json()['results'][0]["registered"]["date"]
print(age)
