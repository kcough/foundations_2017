#
# May 24, 2017: Data Structure
#

# Nothing in here yet...
# But eventually: lists and dictionaries!

#we know about strings/variables


#but we want to be able to group things conceptually, like one thing with different attributes
#this is called a dictionary. myself is the name of the dictionary, 'name' is a key; 'kate' is a value

myself = {
  'name': 'Soma',
  'age': 34,
  'home': 'Brooklyn'
}

friend = {
  'name': 'Jen',
  'age': 33,
  'home': 'Brooklyn'
}
print(friend)
print(myself)

#imagine you just want one part of this--the name, for instance
print(myself['name'])
print("My name is", myself['name'])

#but ugh this is so much to write out. do this instead:
cat_ages = [7,9,2, 5]
print(sum(cat_ages))
print("We have", 4, "cat ages")
print(cat_ages)
#this is also called an ARRAY or a LIST
#the difference between a LIST and a dictionary: a list is the same thing over and over. cats ages, friends, etc. if you have 
#one thing that has different attributes, that is called a dictionary. you can have LISTS of DICTIONARIES. 
#generally, if you see curly braces {} on the outside of something it's a DICTIONARY
#generally, if you see [] square brackets, it is a LIST

#how do you count the number of elements in a list?
#you use length! len
len(cat_ages)

#years of experience
experience = [0,4,5,6,20,30,0]
print(experience)

print(len(experience))
#len() counts the number of elements in a list

print(experience.count(0))
#will count the number of times 0 appears in the list

print(sum(experience))
#this add them all up

print(max(experience))
#want to get the maximum number

print(min(experience))
#to get the min

import statistics
#import this new package so you can calculate the mean. this is called a module, library or package
#it's code that somebody else wrote at some point in time. they called it statistics.

exp_mean = statistics.mean(experience)
#define it! it's easier
exp_median = statistics.median(experience)
print(exp_mean)

print(sorted(experience))
#python is sorting your list for it

#then use it to calculate the mean of experience
#why does len come before and count after? technically speaking, len is a function and .count is a method

#when you are looking for a story, look first for the min, the max, and the average

#can you do a bunch of strings in a list? yes! you can put names, numbers, etc.

cats = ["Smushface", "Boy Abby", "Triples"]
print(cats)

#what if you wanted to do something to every cat individually? you would use a loop
#a FOR LOOP:

for cat in cats:
	print(cat, "!!!!")
	print(cat.upper(), "!!!!") #will transform it to uppercase

#if you only want ONE of the cats
#or one of the ELEMENTS of the list
#you can just grab that

print(cats[0])
#0 is the VERY FIRST ONE!!!

#packages/libraries to get things from the internet

#urllib, urllib2, httplib, BeautifulSoup these are okay, but they're highly technical ways of interacting with the internet
#you want to use requests

import requests


















