#Create an introduction
print("Welcome to the Leap year finder.")
#Ask what year it is
year = int(input("Which year do you want to check? "))
#Create rules/arguments for what makes a leap year using if/else statements.  Use modulos to make sure the division comes out with no remainders.
# 1. (On) Leap years are every year that is evenly divisible by 4
# 2. (Except) Leap years are every year that is evenly divisible by 100
# 3. (Unless) The year is also evenly divisible by 400
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
#Print exit message, add input for exit
exit_message = input("Enter any key to exit") + exit(input)