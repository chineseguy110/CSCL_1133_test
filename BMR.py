#BMR


weight = float(input(" Enter your weight in lb :"))
height = float(input(" Enter your height in inch :"))
age = float(input("Enter your age :") )
gender = (input(" Enter gender ( M or F) : "))

F_BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
M_BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)

if gender == 'M':
    print (int(M_BMR/230))

else:
    print (int(F_BMR/230))