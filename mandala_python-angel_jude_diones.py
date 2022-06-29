#By Angel Jude Diones BSCS 1A
import turtle

#settings constants
OUTER = 172/.9
CIRCLE_OUTER_TO_INNER = (OUTER-172)
GOLD = (255,215,0)
BLACK = (0,0,0)

#setting the options for the mandala
turtle.title("Mandala")
turtle.screensize(1366,720, "black")
turtle.colormode(255)
turtle.speed(0)
turtle.hideturtle()

turtle.penup()
turtle.setpos((-OUTER)+35, 0)
turtle.pendown()
turtle.pencolor(GOLD)

#used in a for loop to reverse the color options
def reverse_tuple(input_tuple):
    new_tuple = ()
    for x in reversed(input_tuple):
        new_tuple += (x,)
    return new_tuple

#sets the upper half of the color screen to whichever color you prefer
def upper(color):
    firstPos = turtle.pos()
    turtle.penup()
    turtle.setpos(-(turtle.window_width()/2), (turtle.window_height())/2)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setx((turtle.window_width()/2))
    turtle.sety(0)
    turtle.setx(-(turtle.window_width()/2))
    turtle.sety((((turtle.window_height())/2)))
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(firstPos)
    turtle.setheading(0)
    turtle.pendown()

#creates 3 circles of the same ratio which subsequent circles are of size 0.9 compared to the previous
#I should have created an overloading function to take two colors... oh well
def tricircle(radius):
    firstPos = turtle.pos()
    colortuple = (GOLD, BLACK)
    for x in range(3):
        for x in colortuple:
            turtle.fillcolor(x)
            turtle.begin_fill()
            turtle.circle(radius,180)
            turtle.left(90)
            turtle.forward(radius*2)
            turtle.left(90)
            turtle.end_fill()
            turtle.circle(radius,180)     
        radius *= 0.9
        circleGap = radius/9
        turtle.left(90)
        turtle.penup()
        turtle.forward(circleGap)
        turtle.right(90)
        turtle.pendown()
        colortuple = reverse_tuple(colortuple)
    turtle.penup()
    turtle.setpos(firstPos)
    turtle.pendown()

#Creates a circle with different upper and lower half colors; with a custom pen and fill color with a radius
def circle_color_separated(pencolor1, fillcolor1, pencolor2, fillcolor2, radius):
    turtle.pencolor(pencolor1)
    turtle.fillcolor(fillcolor1)
    turtle.begin_fill()
    turtle.circle(radius, 180)
    turtle.left(90)
    turtle.forward(radius*2)
    turtle.end_fill()
    turtle.left(90)
    turtle.circle(radius, 180)
    turtle.pencolor(pencolor2)
    turtle.fillcolor(fillcolor2)
    turtle.begin_fill()
    turtle.circle(radius, 180)
    turtle.left(90)
    turtle.forward(radius*2)
    turtle.end_fill()
    turtle.left(90)
    turtle.circle(radius, 180)

#Slices up a circle into 18 parts
def slices(radius):
    firstPos = turtle.pos()
    colortuple = (BLACK, GOLD)
    for x in range(18):
        for x in colortuple:
            turtle.pencolor(x)
            turtle.forward(radius)
        colortuple = reverse_tuple(colortuple)
        turtle.left(90)
        turtle.pencolor(GOLD)
        turtle.circle(radius, 10)
        turtle.left(90)
    turtle.penup()
    turtle.setpos(firstPos)
    turtle.pendown()

#creates a surrounding group of circles limited by a circle
def surroundCircle(radius, radiusbase):
    for x in range(12):
        if x == 0 or  x==6:
            if x == 0:
                turtle.pencolor(GOLD)
                turtle.fillcolor(BLACK)
            elif x == 6:
                turtle.pencolor(BLACK)
                turtle.fillcolor(GOLD)
            turtle.begin_fill()
            turtle.circle(radius,180)
            turtle.left(90)
            turtle.forward(radius*2)
            turtle.left(90)
            turtle.end_fill()
            turtle.circle(radius,180)
            if x == 0:
                turtle.pencolor(BLACK)
                turtle.fillcolor(GOLD)
            elif x == 6:
                turtle.pencolor(GOLD)
                turtle.fillcolor(BLACK)
            turtle.begin_fill()
            turtle.circle(radius,180)
            turtle.left(90)
            turtle.forward(radius*2)
            turtle.left(90)
            turtle.end_fill()
            turtle.circle(radius,180)
            if x == 0:
                turtle.pencolor(BLACK)
                turtle.fillcolor(GOLD)
            elif x == 6:
                turtle.pencolor(GOLD)
                turtle.fillcolor(BLACK)
        else:
            turtle.begin_fill()
            turtle.circle(radius)
            turtle.end_fill()
        turtle.right(180)
        turtle.circle(radiusbase, 30)
        turtle.right(180)

#creates a leaf shape around a circle 
def leaves(radius, radiusbase):
    firstPos = turtle.pos()
    for x in range(18):
        if x == 0 or x ==9:
            secondPos = turtle.pos()
            if x==0:
                turtle.pencolor(GOLD)
                turtle.fillcolor(BLACK)
            elif x==9:
                turtle.pencolor(BLACK)
                turtle.fillcolor(GOLD)
            turtle.begin_fill()
            secondAngle = turtle.heading()
            turtle.left(180-67.38)
            turtle.circle(radius*2, 134.76)
            turtle.setheading(secondAngle)
            turtle.setpos(secondPos)
            turtle.left(180-67.38)
            turtle.end_fill()
            turtle.circle(radius*2, 134.76)

            
            secondPos = turtle.pos()
            if x==0:
                turtle.fillcolor(GOLD)
            elif x==9:
                turtle.fillcolor(BLACK)
            turtle.begin_fill()
            turtle.left(180 - 2*67.38)
            secondAngle = turtle.heading()
            turtle.circle(radius*2, 134.76)
            turtle.setheading(180)
            turtle.setpos(secondPos)
            turtle.setheading(secondAngle)
            turtle.end_fill()
            turtle.circle(radius*2, 134.76)

            
            turtle.right(67.38)
            turtle.right(90)
            turtle.circle(radiusbase, 20)
            turtle.left(90)
        else:
            turtle.begin_fill()
            turtle.left(180-67.38)
            turtle.circle(radius*2, 134.76)
            turtle.left(180 - 2*67.38)
            turtle.circle(radius*2, 134.76)
            turtle.end_fill()
            turtle.right(67.38)
            turtle.right(90)
            turtle.circle(radiusbase, 20)
            turtle.left(90)
    turtle.penup()
    turtle.setpos(firstPos)
    turtle.setheading(0)
    turtle.pendown()


#upper half of the screen is gold
upper(GOLD)

#creates a leaf effect
leaves(CIRCLE_OUTER_TO_INNER+13, 172)

#readjusts the drawing the go to the center
turtle.penup()
turtle.right(180)
turtle.forward(OUTER - 172)
turtle.pendown()
turtle.left(90)

circle_color_separated(BLACK,GOLD,GOLD,BLACK,OUTER)

#moves a distance of the circle from the outer part of the circle to the next inner cirlcle
turtle.left(90)
turtle.forward(CIRCLE_OUTER_TO_INNER)
turtle.right(90)

circle_color_separated(GOLD,BLACK,BLACK,GOLD,172)

#moves a distance of a diameter of a group of surrounding circles
turtle.left(90)
turtle.forward(72)
turtle.right(90)

#using turtle left to allow to move into the circle
tricircle(100)
turtle.left(90)

#using turtle right to be in position to make circles around the circle
slices(100)
turtle.right(90)
surroundCircle(36,100)

turtle.exitonclick()
