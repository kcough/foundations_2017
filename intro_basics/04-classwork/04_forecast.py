# ALL ABOUT APIs

# darkskynet/dev/account
# https://api.darksky.net/forecast/13d3600a5cd0883a0f7c94181a175dd3/37.8267,-122.4233
#endpoint :: is a URL. the list of URLs you can talk to


#first, bring in the requests library
import requests


#module = library = package they're all the same
#use PIP to install packages/modules/library

#run this in the terminal ::: pip install requests

#define the URL you want
url = "https://api.darksky.net/forecast/13d3600a5cd0883a0f7c94181a175dd3/37.8267,-122.4233"

#hey requests, go get that url! and save the response as "response"
#"reponse" is now a dictionary. to check, print it! then you can see what a variable is
#to get what's in there, use .text or .content
response = requests.get(url)
print(response.text)

#what type of data is this?
# print(type(response.text))
#let's tell response to treat this as JSON
print(response.json)

#you get this error:
#<bound method Response.json of <Response [200]>>
#which means it needs parenthesis, so we write:

print(response.json())
data = response.json()

#what kind of data type is it?
print(type(data))

#look at the keys, because it's kind of like a dictionary
print(data.keys())

#one of them is currently, so we can do data['currently']
print(data['currently'])

#inside of currently (which is inside of data), let's look at the temperature
print(data['currently']['temperature'])

#run jupyter notebook
#we're starting a server on our computer ctrl c will stop it if you want
#we get to the server by going to the browser and go to: localhost:8888. it's opened in the same directory you were in
