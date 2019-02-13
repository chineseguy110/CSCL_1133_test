#• Problem A: Poiseuille's Law (30 points)


import math

def poiseuille ():
    length = float(input('Please enter the length:'))

    radius = float(input('Please enter the radius:'))

    viscosity = float(input('Please enter the viscosity:'))

    cap_r = (8 * viscosity * length)/(math.pi * (radius**4))

    if float(viscosity or radius or length) > 0 :

        print('The resistance is : ', cap_r)

    else :
        print('Failed due to input error. Please make sure your inputs are all positive. Exiting program.')


poiseuille()