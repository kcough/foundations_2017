#
# "It doesn't work"
#
# 1. The error message
# 2. The code around where the error is happening
# 3. Expected output
# 4. Actual output
# 5. What you've tried already
#the first kind of error that comes up is a syntax error-it doesn't even know what you're trying to do
#EOL means end of line-you started a string and you never finished it


# Error 1
num = 4.55
#print((round(4) * int('5') + 3)
	#first count your open and closed parenthesis to make sure the number matches if you have a syntax error
print(round(4) * int('5') + 3)

# Error 2
name = "Roberta"
degrees = 14
#print("Hello, my name is " + name + " and it is " + degrees "out today")
print("Hello, my name is ", name, " and it is ", degrees, "degrees out today")

# Error 3
name = "Smushface"
print("I have a cat named", name)

# Error 4
age = 4
if age < 18:
    print("You aren't old enough to vote") 

# Error 5
print("One two three four")
print("Five six seven eight")
print("Nine ten eleven twelve")

# Error 6
pies = 9
print("You have eaten", pies, "pies today")

# Error 7
current_year = 2013
travel = "future"
cars = True
animal_type = "lions"
if current_year > 2017:
    print("It's the future!")

# Error 8
print('4' + '4')

# Error 9
year = 2017
if year >= 1607:
    print("The American colonies existed")
elif year >= 1776: #this code doesn't get run because it's already said yes to something
    print("The United States exists")
else:
    print("America was just a dream")

# Error 9
year = 2017
elif year >= 1776: #this code doesn't get run because it's already said yes to something
    print("The United States exists")
if year >= 1607:
    print("The American colonies existed")
else:
    print("America was just a dream")
