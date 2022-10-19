#Create a greeting
print("Welcome to the advanced BMI checker!")
#Ask for their height/weight
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#Calculate their bmi with their inputs👆
result = weight/height**2
bmi=round(result)
#Create if/elif/else statements to put their weight into a classification for BMI
#Display their BMI and a message telling them which category they are in for their BMI
if bmi < 18.5:
    print("Your BMI is " + str(bmi) + " , you are underweight.")
elif bmi < 25:
    print("Your BMI is " + str(bmi) + " , you have a normal weight.")
elif bmi < 30:
    print("Your BMI is " + str(bmi) + " , you are slightly overweight.")
elif bmi < 35:
    print("Your BMI is " + str(bmi) + " , you are obese.")
else:
    print("Your BMI is " + str(bmi) + " , you are clinically obese.")
#Create an exit message
#Print exit message, add input for exit so it doesn't auto close.
exit_message = input("Enter any key to exit") + exit(input)
