import time

#This is the introduction to the code
print("Hello, this is a simple reminder function I created in python.")

#I ask what the code shall remind you about after a specific amount of time
print("What shall I remind you about?")

#This converts the value given in the brackets into a string
text = str(input())

#Asks how much time until you need to get reminded
print("In how many minutes?")

#Declared a variable as "local_time", and also added a float() command
local_time = float(input())

#Python reads time in seconds, so we have to convert minutes into seconds
local_time = local_time * 60

#This stops the timer
time.sleep(local_time)

#Obviously, this tells you the time is over, and reminds you about what you input in the second line of code
print("You told me to remind you of " + (text))