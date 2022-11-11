#Create a greeting"
print("Welcome to Python Pizza Deliveries!")
#Ask what size pizza they want
size = input("What size pizza do you want? S, M, or L ?")
#Ask if they want pepperoni or extra cheese
add_pepperoni = input("Do you want pepperoni? Y or N ?")
extra_cheese = input("Do you want extra cheese? Y or N ")

#create a bill that will add up their pricing
bill = 0
#create pricing for sizes
#create pricing for pepperoni cost based on size of pizza
#create pricing for extra cheese
#Use if/else statements to make calculations for the pricing
if size == "S":
    bill += 15
    print("A small pizza is $15.")
elif size == "M":
    bill += 20
    print("A medium pizza is $20.")
else:
    bill += 25
    print("A large pizza is $25.")

if add_pepperoni == "Y":
    if size == "S":
        bill +=2
        print("Pepperoni on a small is an extra $2.")
    else:
        bill +=3
        print("Pepperoni on a Large is an extra $3.")
if extra_cheese == "Y":
    bill += 1
    print("Extra cheese is an extra $1.")

#Create message saying how much it will cost
print(f"Your final bill is ${bill}")
print("We will call you when your pizza is ready.")
#Create exit message
exit_message = input("Enter any key to exit") + exit(input)