#Kate Cough
#May 24 2017
#Homework 2, Part 1

#LISTS

#1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48

numbers = [22,90,0,-10,3,22,48]
print(numbers) 

#2) Display the number of elements in the list.

print(len(numbers))

#3) Display the 4th element of this list.

print(numbers[3])
 
#4) Display the sum of the 2nd and 4th element of the list.
#GO BACK THIS ISN"T WORKING RIGHT it should be 80
print(numbers[1] + numbers[3])

#5) Display the 2nd-largest value in the list.

numb_sort = sorted(numbers)
print(numb_sort)
print(numb_sort[-2])

#6) Display the last element of the original unsorted list

print(numbers[6])

#7) For each number, display a number: if your original number is less than 10, 
#multiply it by thirty. If it's also even, add six. If it's greater than 50 subtract ten. 
#If it's not negative ten, subtract one. 
#(For example: 2 is less than 10, so 2 * 30 = 60, 2 is also even, so 60 + 6 = 66, 2 is not negative ten, so 66 - 1 = 65.)

for number in numbers:
	if number < 10:
		print(number * 30)
	elif number % 2 == 0:
		print(number + 6)
	elif number > 50:
		print(number - 10)
	elif number != -10:
		print(number - 1)

#8) Display the sum of all of the numbers divided by two.
sum_num = sum(numbers)
print(sum_num/2)



#DICTIONARIES

#8) Sometimes dictionaries are used to describe multiple aspects of a single object. 
#Like, say, a movie. Define a dictionary called movie that works with the following code.

#print("My favorite movie is", movie['title'], "which was released in", movie['year'],
#"and was directed by", movie['director'])

movie = {
  'title': 'Top Gun',
  'year': 1968,
  'director': 'Tony Scott'
}

print(movie)

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'] + ".")


#9) On the lines after that, add entries to the movie dictionary for 
#budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.
 
movie = {
  'title': 'Top Gun',
  'year': 1968,
  'director': 'Tony Scott',
  'budget': 100000,
  'revenue': 500000
	}

print(movie['title'], "grossed", movie['revenue'] - movie['budget'], "dollars more than it cost to make.")

#10) If the movie cost more to make than it made in theaters, print "It was a flop". If the film's 
#revenue was more than five times the amount it cost to make, print "That was a good investment."

for top_gun in movie:
	if movie['budget'] * 5 < movie['revenue']:
		print("That was a good investment.")
	elif movie['budget'] > movie['revenue']:
		print("It was a flop.")

 
#11) Sometimes dictionaries are used to describe the same aspects of many different objects. 
#Make ONE dictionary that describes the population of the boroughs of NYC. 
#Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, 
#Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)
 
pop = {
  'man': 1600000,
  'brk': 2600000,
  'brx': 1400000,
  'que': 2300000,
  'sti': 470000
  }


#12) Display the population of Brooklyn.
print("Brooklyn has a population of", pop['brk'] // 1000000, "million people.")
 
#13) Display the combined population of all five boroughs. it's not a list, so you need to add the values.
#remember that to call the values in a key : value pair, you do [dictionaryname.valuename]
total_pop = sum(pop.values())
print("The total population of the boroughs combined is", total_pop // 1000000, "million people. That is a lot of people.")
 
#14) Display what percent of NYC's population lives in Manhattan.
print(((pop['man'] / total_pop) * 100), "percent of the city's population lives in Manhattan.")

