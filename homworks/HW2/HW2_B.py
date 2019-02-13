import turtle
#Write a function named fourSidedStar along with a main function that do the following:
speed= turtle.speed
def main():
    length = int(input("Input length of the star’s sides in pixel: "))
    def fourSidedStar ():
        lengthofside = turtle.Turtle()
        #right, up, left, and down
            #angle stay the same after
        lengthofside.left(75)
        lengthofside.forward(length)
        lengthofside.right(60)
        lengthofside.forward(length)
        lengthofside.left(150)
        lengthofside.forward(length)
        lengthofside.right(60)
        lengthofside.forward(length)
        lengthofside.left(150)
        lengthofside.forward(length)
        lengthofside.right(60)
        lengthofside.forward(length)
        lengthofside.left(150)
        lengthofside.forward(length)
        lengthofside.right(60)
        lengthofside.forward(length)
        exit()

    if int(length) > 0:

        fourSidedStar()
    else:
        print("Input not valid")
main()

