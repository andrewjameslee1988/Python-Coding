#Ask for age for input
age = input("What is your current age?")
#Change age to an integer just in case they don't give a whole number
age_as_int= int(age)
#Calculate how many years left until they are 90
years_left = 90 - age_as_int
#Create factors for # of: days/weeks/months they have left
days_left = years_left*365
weeks_left = years_left*52
months_left = years_left*12

#Using an f string, pull all the factors you created into a message
#Print message
message= f"You have {days_left} days, {weeks_left} weeks, {months_left} months left."
print(message)
#print exit message, add input for exit
exit_message = input("Enter any key to exit") + exit(input)
