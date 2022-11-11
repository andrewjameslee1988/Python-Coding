#Create a greeting
print("Welcome to the rollercoaster!")
#Ask for their height and make it an integer
height = int(input("What is your height in cm? "))
#Create conditions for being able to ride the roller coaster if you are tall enough, create prints for yes or no
#Ask for their age, then create pricing based on what their age is using if/else/elif
#Create a bill factor, which will have ticket price and photo prices added together
bill = 0

if height >=120:
    print("You can ride the rollercoaster!")
    age=int(input("what is your age? "))
    if age <= 12:
        bill= 5
        print("Child tickets are $5.")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
#Ask if they want to take a photo.  If they do, add it to their bill.
    wants_photo = input("Do you want a photo taken for $3? Enter Y or N. ")
    if wants_photo == "Y":
        bill +=3
#Make a statement that combines their charges together to show their bill.
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to be taller before you can ride.")
#Create exit message, add input for exit
exit_message = input("Enter any key to exit") + exit(input)
