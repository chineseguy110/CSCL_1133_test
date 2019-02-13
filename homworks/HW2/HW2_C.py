#Calculating the calories burned during workouts.

height = float(input('Please input the height of the person'))
weight = float(input('Please input the body weight of person, in pounds: '))
heart_rpm = float(input('Please input the average heart rate of the person during the workout,in beats per minute: '))
age = float(input('Please input the age of the person, in years: '))
duration = float(input('Please input the duration of the workout of the person, in minutes: ' ))


def calories_short():
        short_cal_burend = float(((age * 0.074)+(heart_rpm * 0.4472 ) - (weight * 0.05741)- 20.4022)*duration) / 4.184
        print("\nYou entered the following information:\nHeight:", height,
            "\nBody weight: ", weight,
            '\nAverage heart rate: ', heart_rpm,
            '\nAge', age,
            '\nDuration of workout: ', duration,
            "\nThe number of calories burned for this short person is ", int(short_cal_burend), "calories.")


def calories_tall():
        tall_cal_burend = float(((age * 0.2017) + (heart_rpm * 0.6309) - (weight * 0.09036) - 55.0969) * duration) / 4.184
        print("\nYou entered the following information:\nHeight:", height,
              "\nBody weight: ", weight,
              '\nAverage heart rate: ', heart_rpm,
              '\nAge', age,
              '\nDuration of workout: ', duration,
              "\nThe number of calories burned for this tall person is ", int(tall_cal_burend), "calories.")



if float(height) <= float(5.6):
    calories_short()

else:
    calories_tall()


