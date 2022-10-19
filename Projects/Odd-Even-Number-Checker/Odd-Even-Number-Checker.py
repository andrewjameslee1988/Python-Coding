#Create a greeting
print("Welcome to the odd/even number checker!")
#ask for a number and make it a whole number
number = int(input("Which number do you want to check? "))
#use a modulo to divide the number in 2
modulo = number % 2
#Using if/else statement to have it check if it comes out as an integer or a fraction
#Then print a response for both cases
if modulo >= 1:
    print("Your number is an odd number.")

else:
    print("Your number is an even number.")
#Create an exit message, add input for exit so the script doesn't auto close or shut down.
exit_message = input("Enter any key to exit") + exit(input)
