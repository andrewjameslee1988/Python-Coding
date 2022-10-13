#BMI calculator
#create inputs for formula of BMI((w/(h ** 2))
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#change inputs into a floating point
h=float(height)
w=float(weight)
#run inputs through formula
BMI=(w/(h ** 2))
#change BMI into integer to have a whole number
BMI_int=int(BMI)
#print message showing your body mass
bmi_message=("Your Body Mass Index is: ")
print(bmi_message + str(BMI_int))
#print exit message, add input for exit
exit_message = input("Enter any key to exit") + exit(input)
