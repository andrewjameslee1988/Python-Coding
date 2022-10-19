#create a greeting for the roller coaster checker
print("Welcome to the rollercoaster!")
#Ask for their height in cm, and turn it into an integer so we have a whole number
height = int(input("What is your height in cm? "))
#Create and if/else and messages for both if they meet the conditions
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to be taller before you can ride.")
#create exit message, add input for exit
exit_message = input("Enter any key to exit") + exit(input)
