# WhileLoopNameSpiral

import turtle

t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange",
          "purple", "white", "brown", "gray", "pink"]
family = []  # empty list for family names

name = turtle.textinput("It's time to build a list of family names.",
                        "Enter a name, or just hit [ENTER] to quit:")
# keep asking for names
while name != "":
    family.append(name)

# draw a spiral of the names on the screen:
for x in range(100):
    t.pencolor(colors[x % len(family)])  # rotate through the colors
    t.penup()  # do not draw the regular spiral lines
    t.forward(x * 4)  # just move the turtle to the next spiral angle
    t.pendown()  # draw the next family member's name
    t.write(family[x % len(family)], font=("Arial", int((x + 4) / 4), "bold"))
    t.left(360 / len(family) + 2)  # turn left for our spiral