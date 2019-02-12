
yes = 'Y'

while yes == 'Y':
    x = float(input(' Enter value :'))
    unit = input(" Enter a unit 'pounds', 'ounces', 'miles', 'inches', 'kilos', 'grams', 'kilometers', 'centimeters' : ")
    if unit == 'pounds' :
        x = x * 2.20462
        print(format(x,"0.4f"), 'kilos')
    elif unit == 'ounces' :
        x = x * 0.035274
        print( format(x,"0.4f"), 'grams')
    elif unit == 'miles' :
        x = x * 1.609344
        print( format(x,"0.4f"), "kilometers" )
    elif unit == 'inches':
        x = x * 2.54
        print( format(x,"0.4f"), 'centimeter')
    elif unit == 'kilos':
        x = x * 0.62137119224
        print( format(x,"0.4f"), ' miles ')
    elif unit == 'grams':
        x = x * 0.035274
        print( format(x,"0.4f"), 'ounces')
    elif unit == 'kilometers':
        x = x * 0.62137119224
        print( format(x,"0.4f") , "miles")
    elif unit == 'centimeters':
        x = x * 0.393701
        print( format(x,"0.4f") , 'inches')


    yes = input("Do you want to continue? : ")

