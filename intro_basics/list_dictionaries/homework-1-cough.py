#kate cough
#may 22, 2017
#homework 1

#here we've created a new variable, "year_of_birth"

year_of_birth = input("What year were you born in? ")
#create a new variable, age. Remember you have to tell it that year_of_birth is an integer

if year_of_birth > "2017":
	print("Oops! That looks like it's in the future. Let's try again.")
	#don't want dates in the future.
	year_of_birth = input("What year were you born in? ")
	#don't forget to ask again and use the same variable.

#calculate their age based on the year and their year of birth
age = 2017 - int(year_of_birth)


print("You are roughly " + str(age) + " years old")

#create a new variable with the person's age * 42 million, which is the avg. beats/per year. you could also add the calculation
#directly into the print line (line 26)

beats_per_year = int(age * 42000000)
print("Your heart has beaten roughly " + str(beats_per_year) + " times")

#create a new variable with the blue whale's heartbeat, based on the age input and information from THE GOOGLE

blue_whale_beats_per_year = int(age * 5256000)
if blue_whale_beats_per_year > 1000000000:
	print(" A " + str(age) + " year old blue whale's heart has beaten " + str(blue_whale_beats_per_year / 1000000000) + " billion times")
#make it say billion because giant numbers are ugly
else:
	print("A " + str(age) + " year old blue whale's heart has beaten " + str(blue_whale_beats_per_year) + " times")

#create a rabbit heartbeat variable

rabbit_heart_beat_per_year = int(age * 70956000)
if rabbit_heart_beat_per_year > 1000000000:
	print("A " + str(age) + " year old rabbit's heart has beaten " + str(rabbit_heart_beat_per_year / 1000000000) + " billion times")
else:
	print("A " + str(age) + " year old rabbit's heart has beaten " + str(rabbit_heart_beat_per_year) + " times")

#to calculate your age on other planets, figure our your age in days first. create a new variable for this:

earth_age_days = int(age * 365)

#then divide this by 224.7, the number of earth days it takes for venus to do one full rotation around the sun

age_venus = int(earth_age_days / 224.7)
print("On Venus, you're " + str(age_venus) + " years old")

#create a new variable with your age on Neptune, dividing it by 60,148.35 because that is how many days it
#takes for neptune to complete a full revolution around the sun WOW:

age_neptune = int(earth_age_days / 60148.35)
print("On Neptune, you're " + str(age_neptune) + " years old")
#if you divide with // two slashes you can get an integer e.g. age_neptune = int(earth_age_days // 60148.35)

if age > 29:
	print("You're " + str((age) - 29) + " years older than I am, and most likely much much wiser")
else:
	print("You're " + str(29 - (age)) + " years younger than I am. Enjoy your youth and vigor!")

if (int(year_of_birth) % 2 == 0): #the % sign is like division except it also checks for the remainder. if the
#number divided by two has a remainder of 0 it's even, otherwise it's odd. thanks stackoverflow.
	print("You were born in an even year!")
else: 
	print("You were born in an odd year!")
#you want to use abs(int(myage) - int(age)) in order to avoid a negative year

#I'm sure there's a better way to do this, but for now:

if (year_of_birth == str(1974)):
	print("The Steelers have won the Superbowl 6 times since you were born.")
if (year_of_birth >= str(1975) and year_of_birth <= str(1978)):
	print("The Steelers have won the Superbowl 5 times since you were born.")
if (year_of_birth == str(1979)):
	print("The Steelers have won the Superbowl 4 times since you were born.")
if (year_of_birth >= str(1980) and year_of_birth <= str(2005)):
	print("The Steelers have won the Superbowl 3 times since you were born.")
if (year_of_birth >= str(2006) and year_of_birth <= str(2007)):
	print("The Steelers have won the Superbowl 2 times since you were born.")
if (year_of_birth >= str(2008)):
	print("The Steelers have won the Superbowl once since you were born.")

#let's calculate the presidents! I know there's probably a better way to do this...

if (year_of_birth >= str(1933) and year_of_birth <= str(1945)):
	print("Franklin Delano Roosevelt is your man")
if (year_of_birth >= str(1945) and year_of_birth <= str(1953)):
	print("Harry S. Truman is your man")
if (year_of_birth >= str(1953) and year_of_birth <= str(1961)):
	print("Dwight D. Eisenhower is your man")
if (year_of_birth >= str(1961) and year_of_birth <= str(1963)):
	print("John F. Kennedy is your man")
if (year_of_birth >= str(1963) and year_of_birth <= str(1969)):
	print("Hey hey LBJ!")
if (year_of_birth >= str(1969) and year_of_birth <= str(1974)):
	print("Nixon's your guy...at least they were good years for journalism")
if (year_of_birth >= str(1974) and year_of_birth <= str(1977)):
	print("Gerald Ford is your president!")
if (year_of_birth >= str(1977) and year_of_birth <= str(1981)):
	print("Jimmy Carter!")
if (year_of_birth >= str(1981) and year_of_birth <= str(1989)):
	print("Reagan's your guy.")
if (year_of_birth >= str(1989) and year_of_birth <= str(1993)):
	print("George H.W. is your president. Maybe he'll go skydiving with you.")
if (year_of_birth >= str(1993) and year_of_birth <= str(2001)):
	print("You were born during the Clinton dynasty.")
if (year_of_birth >= str(2001) and year_of_birth <= str(2009)):
	print("Congratulations, you were born under the venerated artist George W. Bush.")
if (year_of_birth >= str(2009) and year_of_birth <= str(2017)):
	print("You were born under Obama! Maybe Michelle will teach you to garden.")






