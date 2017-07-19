print('Hello world')
print("Hello world")

print(3 + int("3"))
print(3,"3")
print(2.5)
print(3/4)
print("Hello","Kate")


#This is a variable
#every time I type 'name' now, it's 
#the same as typing "Soma"
name = "Soma"
print("Hello", name)

#now try this:
a = 5
b = 200
print(a + b)
print(a,name)

print(a, name, "Whatever else")

age = input("How old are you?")
print(age)

#this is called a conditional. It says: if the age variable
#is less than 21, do the indented thing. 
#python knows to do anything that's indented after this.
#need to convert age to 21
#decimals are called floats
#if you want to treat things as an integer instead
#of a string, you have to tell it

if int(age) < 21:
	print("You can't buy alcohol")
#what happens if you don't indent this?
#it won't know that print is attached to the line above
#now go run this in the terminal.
#it will ask you old you are. type an answer less than 21
#if it is, the terminal should answer "You can't buy alcohol"
else:
	print("buy me twenty beer units please")
	print("I'll pay you back")
print("Let's party")





