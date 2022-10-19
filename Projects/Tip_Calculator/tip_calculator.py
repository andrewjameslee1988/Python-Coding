#Create a welcome message
print("Welcome to the tip Calculator")
#Ask how much the bill was
bill = float(input("How much was the bill? $"))
#Ask how many ways it is split
split = int(input("How many ways will it be split?"))
#Ask what percentage of tip they want to leave
tip = int(input("What percent tip will you leave: 10, 15, or 20%?"))
#Create equations to show the amounts for bill/tips/total/shares
tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / split
final_amount = round(bill_per_person, 2)
#Create a message saying how much money each person will pay
#Use an fString to pull the integer amount into the message as a string
print(f"Each person will have to pay ${final_amount}")
#Print exit message, add input for exit
exit_message = input("Enter any key to exit") + exit(input)
