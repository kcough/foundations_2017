year_of_birth = input("What year were you born in?")
#define it as an integer so you don't have to repeat yourself over and over
year_of_birth = int(year_of_birth)
print("you were born in",  year_of_birth)

age = 2017 - year_of_birth
age = int(age)
#note: don't generally need too many parenthesis. don't need them here. 
print("You are roughly ", str(age), " years old")

heartbeats = age * 42000000
#add the link where you go this information (42 million beats per year) into your code
#calculate heartbeat out based on 70 bpm
heartbeats = age * 365 * 24 * 60 * 70
#make heartbeat an integer so it's always an integer
heartbeats = int(heartbeats)

print("Your heart has beaten", heartbeats)

#calculate whale heartbeat based on 8 bpm and rabbit heartbeat based on 120 bpm
whale_heartbeats = age * 365 * 24 * 60 * 8
whale_heartbeats = int(whale_heartbeats)

rabbit_heartbeats = age * 365 * 24 * 60 * 120
rabbit_heartbeats = int(rabbit_heartbeats)

#convert heartbeats to xxx billion instead of the raw number
if rabbit_heartbeats > 1000000000:
	rabbit_beats_billion = int(rabbit_heartbeats / 1000000000)
	print (rabbit_beats_billion, "billion beats")
	#you can used int or round to get rid of the things after the decimal and make it cleaner
if whale_heartbeats > 1000000000:
	whale_beats_billion = round(whale_heartbeats / 1000000000)
	print (whale_beats_billion, "billion beats")

#sentence = "%.2f billion beats" % rabbit_beats_billion
#print(sentence)
#check back on this!!

#Steelers won the Superbowl in: 1975, 1976, 1979, 1980, 2006, 2009

if year_of_birth <= 1975:
	print("They have won 6 Superbowls since you were born")
elif year_of_birth <= 1976:
	print("They have won 5 Superbowls since you were born")
elif year_of_birth <= 1979:
	print ("They have won 4")
elif year_of_birth <= 1980:
	print ("They have won 3")
elif year_of_birth <= 2006:
	print ("They have won 2")
elif year_of_birth <= 2009:
	print ("They have won 1")

if year_of_birth <= 1933:
	print("Franklin Delano Roosevelt is your man")
