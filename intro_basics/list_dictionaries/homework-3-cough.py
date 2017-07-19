#Kate Cough
#May 31 2017
#Homework 3

# `my_list_of_numbers = [1, 2, 3, 9, 8, 7, 4, 5, 6]`

# #Set it to 0!
# `counter = 0`

# `for each_element in my_list_of_numbers:`
#     `counter = counter + 1`

# `print(counter)`

#1. Count how many numbers are in the list with a for loop, not len.

numbers = [4,5,1,10,200,34,22,19,43,56,32,11,40,82,23,43,12,65,10]

#the initial condition is 0
numbers_count = 0

#here's the for loop
for number in numbers:
	if number >= 0:
		numbers_count = numbers_count + 1
print("There are", numbers_count, "numbers in this list.")


#2. Add another number to the list.

numbers.append(6)
print("This is the new numbers list with an extra number added:", numbers)

#3. Count how many even numbers are in the list. Use a for loop.

for even in numbers:
 # Check if the number is divisible by two
     if int(even) % 2 == 0:
 	    print("The number", even, "is an even number.")

#4. Count how many values are above the mean and how many are below the mean. Use a for loop.

# first, find the mean. use the statistics library.
import statistics

#save it in a variable for easier use in the for loop
mean = statistics.mean(numbers)
print("The mean is", mean)

for each_element in numbers:
	if each_element >= mean:
		print((number), "is above the mean.")
	elif each_element <= mean:
		print((number), "is below the mean.")
# for some reason it's only cycling through one of the numbers. WHYYY

# 5. Total up the numbers. Use a for loop, do NOT use sum()

counter = 0

for each_element in numbers:
	counter = counter + each_element 
print("The sum of the numbers in the list is", counter)

# 6. Total up the numbers that are above the mean and the numbers below the mean. Use a for loop, do not use sum()

#I know there's a better way to do this...

countermean = 0

for each_element in numbers:
	if each_element >= mean:
		countermean = countermean + each_element
print("The sum of the numbers below", mean, "is equal to", countermean)

countermean = 0
for each_element in numbers:
	if each_element <= mean:
		countermean = countermean + each_element
print("The sum of the numbers above", mean, "is equal to", countermean)


# 7. Find the largest number. Use a for loop.

# max_value = None
# for each_elemente in numbers:
#     if each_element > max_value: max_value = each_element

# # 8. You have a list of dogs, shown below. Add Maxwell your new dog to the list. 

dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]
dogs.append('Maxwell')
print("Here's the new list of dogs:", dogs)

# 9) Make a list of all dogs that have names of 5 characters or less. Use a for loop.

for each_dog in dogs:
	if len(each_dog) <= 5:
		print("These dog names have 5 characters or less",each_dog)

# 10) I'm on a web page with some links about Zurich, and the URL looks like this: http://important-swiss-things.ch/docs/download/ZH


list_of_cantons = ["ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO",
"BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]
for each_element in list_of_cantons:
    print("http://important-swiss-things.ch/docs/download/"+each_element)

# 11) I'm trying to get some top-secret documents from top-secret-secrets.com, and 
# while I know the URL pattern I don't want to type them all out individually!

# Each secret document has a document ID and is made up of 12 pages, pages "001.pdf" through "012.pdf". 
# Each page is available at a different URL. For example, for the document ID of QQ7LTHM, the pages are available at

# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/001.pdf
# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/002.pdf
# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/003.pdf
# ...
# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/012.pdf

# I have the following document IDs:

# qq7lthm
# jemsqhg
# O6itcke
# cp4Iua0
# bkijcmo
# ctoyjrm
# z8wc6xy
# zk4Bmm0

# Can you print out all of the URLs? Note that the document IDs need to be capitalized in the URL!


#each document ID has 12 pages associated with it
#so there are two things that are changing in the URL. the first is the ID, the second is the number of pages.

#let's change only one thing first so we don't get majorly confused. let's change the page numbers.

for i in range(1,13):
	if i < 9:
		print("www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/00"+str(i))
	elif i > 9:
		print("www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/0"+str(i))

#now let's try and change the only document ID

document_ids = ["qq7lthm", "jemsqhg", "O6itcke", "cp4Iua0", "bkijcmo", "ctoyjrm", "z8wc6xy","zk4Bmm0"]
for each_element in document_ids:
	print("www.top-secret-pdfs.com/content/secret/"+each_element+"page/001.pdf")

#now can we put these two things together? and capitalize all of them!
# here's how you capitalize [x.upper() for x in ["a", "b", "c"]] >>>> ['A','B','C']
#also use for i in range(1,13): print(str("{0:03d}".format(i)) which is code that I got from stack overflow re: string formatting
# with leading zeros!>>> "{0:02d}".format(3)
# >>>'03'

document_ids = [x.upper() for x in ["qq7lthm", "jemsqhg", "O6itcke", "cp4Iua0", "bkijcmo", "ctoyjrm", "z8wc6xy","zk4Bmm0"]]
for each_element in document_ids:
	for i in range(1,13):
		print("www.top-secret-pdfs.com/content/secrets/"+each_element+"/page/"+str("{0:03d}".format(i))+".pdf")


#below is the more labor intensive way to add the zeros, which is the first thing I tried.

# document_ids = [x.upper() for x in ["qq7lthm", "jemsqhg", "O6itcke", "cp4Iua0", "bkijcmo", "ctoyjrm", "z8wc6xy","zk4Bmm0"]]
# for each_element in document_ids:
# 	for i in range(1,13):
		# if i < 9:
		# 	print("www.top-secret-pdfs.com/content/secrets/"+each_element+"/page/00"+str(i)+".pdf")
		# elif i > 9:
		# 	print("www.top-secret-pdfs.com/content/secrets/"+each_element+"/page/0"+str(i)+".pdf")


# TIPS

# Every looping question is built up of THREE parts
# 1. The Initial Condition
# 2. The Condition
# 3. The Update
# What does that mean?! Learn more details one the site at 
# http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/

# Instead of always adding one to a number, maybe you should think about adding to a running total, or putting another element into a list.

# When getting the mean and median, DON'T use numpy, use the statistics package.

# If you'd like to get fancy for the last one, you can look up formatting with "leading zeroes"

# Those document IDs are lowercase, but you need them to be capitalized!





# PART TWO: Dictionaries

# Dictionaries are super useful and you use them all of the time, but I wouldn't say there are very many 'tricks' like there are with lists
 # Most of the time you just want to put things in and take things out using keys.

# 1) Let's say we are terrible doctors and we have a patient. Define a dictionary called patient that works with the following code.

#okay, remember that dictionaries look like this:
# dictionary_name = {
# 	'key':'value',
# 	'key2':'value',
# 	'key3':['value0ofkey3','value1ofkey3','value2ofkey3']
# }

# print("Doctor, it looks like the patient's is complaining about", patient['complaint'])

patient = {
'complaint': 'fever'
}

print("Doctor, it looks like the patient's complaining about a", patient['complaint'])
 
 
# 2) We aren't really listening to their complaint, but as more test results come in, we'll add these things to the patient's record.
#  Add the following to the patient dictionary:
#  Heart rate: 70
# Temperature: 98.6
# Infection: No

patient = {
	'complaint':'fever',
	'heart rate':70,
	'temperature': 98.6,
	'infection': 'no'
}

#just a reminder as the first thing you should do when you see a dictionary--look at the keys! maybe the values too.

print(patient.keys())
print(patient.values())


# Store your diagnosis in a key called 'diagnosis'.

patient = {
	'complaint':'fever',
	'heart rate': 70,
	'temperature': 98.6,
	'infection': 'no',
	'diagnosis': ['heat stroke', 'the flu', 'a cold', 'take an aspirin and call me in the morning']
}

#because this is confusing for me, let's print the keys and values again, to make sure I'm on top of this.
print(patient.keys())
print(patient.values())

#let's practice grabbing a certain value from the diagnosis key, which has multiple values
print("I think the patient has a",patient['diagnosis'][2])

# 3) Now let's be doctors! First, if they have a heart rate about 100, we should tell them to relax. 

if patient['heart rate'] > 100:
	print("You should really relax.")

# * If their temperature is above 102 but they do not have an infection, they have heat stroke.

# if patient['temperature'] > 102:
# 	elif patient['infection'] = 'no':
# 		print("They have heat stroke.")
# * If they have a high temperature and they have an infection, they have the flu.
# * If they have an infection but no high temperature, it's probably a cold.
# * If none of the above, tell them to take an aspirin and call you in the morning.

# When you are finished, print "Your diagnosis is _______."
 
# 4) Make a list of 3 different patients, each with different complaint, heart rate, temperature, and whether they have an 
# infection or not. Use a for loop to diagnose each of them.
 
# 5) Because you're such a bad doctor, they've put you in the back. You don't get to talk to patients any more, 
# you just get to diagnose them based on their temperatures. And these ones aren't even sick! They just might have heat stroke.

# Using the following list and a for loop, create some new patient records (a list of dictionaries). 
# Each dictionary should include a tempearture and whether the patient has heat stroke or not. When completed, my "for patient in patients..." code should be able to run.

# temperatures = [ 99, 105, 98, 99, 100, 104, 105, 100 ]

# # YOUR CODE GOES HERE

# for record in records:
#   if record['diagnosis'] == 'heat stroke':
#     print("This patient has heat stroke!")
#   else:
#     print("This patient does not have heat stroke")

# PART THREE: Reading CSV files

# # If we didn't know a better method, we might use csv.DictReader to analyze CSV files in Python 
# (a csv is like a less fancy Excel spreadsheet). In a few weeks we'll learn the "better method," but for 
# now we'll use it to practice with lists and dictionaries.

csv.DictReader

import csv

csvfile = open('/Users/kaitlincough/Documents/Lede/soma/homework_soma/countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()



# When you run this code, it will open up a file and converting it into a list of dictionaries. 
# Each row becomes a dictionary, and each column becomes a key. Not sure what I mean? Print it out to get a good look!

# Note: With Python 3, reading in CSV files is friendlier than it used to be, and uses something 
# called an "ordered dictionary." It means the keys have a specific order to them, but most importantly they don't have { } around them!

# Answer the following questions based on my favorite boring dataset, countries.csv (attached).

# 1) What are the rows in our dataset?

# 2) How many countries do we have in our dataset?

# 3) How many countries in Asia? How about North America?

# 4) What is the total population of the world?

# 5) Which has a larger population, Africa or South America?

# 6) Calculate the total GDP of each country and print it out (right now it's per capita).

# 7) What is the median life expectancy of the world?

# 8) What is the median life expectancy of Europe?

# 9) Print out each country that has a below-average life expectancy.

# 10) Print out each country that has a below-average GDP but an above-average life expectancy.

# 11) Calculate the 75th percentile of GDP.

# 12) What percent of the world population has a life expectancy of below 50 years? Above 80 years?

# TIPS

# A quick way to find out the rows is to select the first dictionary and look at its keys.

# You don't have to use a for loop for number two!

# For most of these, you'll use the same approaches as you did with Part One and the lists, you just need to figure out 
# which patterns are the right ones.

# You know how to get a median if given a list of numbers. For some of these it might be helpful to use your for loop 
# to create a new list of numbers, then calculate the median from it.

# You know how to calculate the 50th percentile - it's the median of ALL of the values. The 75th percentile should be the
 # 50th percentile of only the top 50% of the values.



# Another error! In PART THREE, question ONE

# 1) What are the rows in our dataset?

# Should instead be

# 1) What are the COLUMNS in our dataset?

# Also, the TIP for that one should be "A quick way to find out the columns is to select the first dictionary and look at its keys."


