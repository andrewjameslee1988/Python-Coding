#Create a greeting
print("Welcome to the rollercoaster!")
#Ask for their height and make it an integer
height = int(input("What is your height in cm? "))
#Create conditions for being able to ride the roller coaster if you are tall enough, create prints for yes or no
#Ask for their age, then create pricing based on what their age is using if/else/elif
if height >=120:
    print("You can ride the rollercoaster!")
    age=int(input("what is your age? "))
    if age <= 12:
        print("Please pay $5")
    elif age <=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to be taller before you can ride.")
#Create exit message, add input for exit
exit_message = input("Enter any key to exit") + exit(input)
