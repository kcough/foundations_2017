#Kate Cough
#May 25 2017
#Homework 2, part 2

#1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ["zimbabwe", "algeria", "malawi", "congo", "egypt", "burundi", "rwanda"]
print(countries)

#2) Using a for loop, print each element of the list
for country in countries:
	print(country)

#3) Sort the list permanently.
countries.sort()
print(countries)

#sort_country = sorted(countries)
#print(sort_country)

#4) Display the first element of the list.
print(countries[0])

#5) Display the second-to-last element of the list.
print(countries[-2])

#6) Delete one of the countries from the list using its name.
del countries['zimbabwe']


#7) Using a for loop, print each country's name in all caps.
for country in countries:
	print(countries)
	print(countries.upper())

 #These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by 
 #typing in *coordinates of CITYNAME*. You can also use http://itouchmap.com/latlong.html. 
 #Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. 
 #If the longitude is W, make it negative. See here for explanation: 
 #https://answers.yahoo.com/question/index?qid=20080211182008AAMdUe8
 
#1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'.
# Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees
tree = {
	"name":"Herbie",
	"species":"Ulmus americana",
	"age":212,
	"location_name":"Yarmouth, Maine",
	"latitude":43.8006,
	"longitude": -70.1867 
}
#print(tree.keys())

#2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(tree["name"], "is a", tree["age"], "year old tree that is in", tree["location_name"])

#3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print 
#"The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
print(tree["name"] + ", the tree in", tree["location_name"], "is north of NYC.")
#better to do an if else for this
nyc =
{
	'latitude' : 40.7128
	'longitude': -74.0059
}

if nyc['latitude'] < tree['latitude']:
	print("The tree", tree['name'], "in", tree['location_name'], "is south of NYC")

#4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}."
# If they are younger than the tree, display "{name} was {XXX} years old when you were born."
user_age = int(input("How old are you?"))
if user_age < tree["age"]:
	print(tree["name"], "is roughly", (int(tree["age"]) - user_age), "years older than you are.")


#1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, 
#and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).
#2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? 
#Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.
#3) Loop through the list, printing whether each city is north of south of your tree from the previous section.