#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code and PC02
ATLS 1300
Author: Dr. Z
Author: Logan Turner
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

#move to first grafitti position
turtle.penup() #puts pen up so turtle can move to first location without drawing

#moustache
centerStache = (25,65) #this is where the center of Bezos' beautiful and bushy 'stache begins
turtle.goto(centerStache) 
turtle.pendown() #put the pen down and let's start drawing!!
turtle.pensize(5) #increase the line thickness

#right...wing? Are they called wings? Like eyeliner? Ok, well, time to draw the right wing of the moustache
turtle.circle(-45, 30)
turtle.circle(10, 285)
turtle.penup()

turtle.goto(centerStache)
turtle.setheading(180)

#left wing
turtle.pendown()
turtle.circle(135, 15)
turtle.circle(-10, 270)
turtle.penup()

#earwax
turtle.setheading(0)
turtle.backward(80)
turtle.pensize(1)
turtle.pendown()
turtle.fillcolor("DarkGoldenrod") #gross earwax color: check!
turtle.color("DarkGoldenrod3")
turtle.begin_fill()
#draw earwax polygon
turtle.circle(10, 75)
turtle.left(5)
turtle.circle(10,20)
turtle.left(5)
turtle.circle(10,10)
turtle.left(5)
turtle.circle(10,25)
turtle.left(5)
turtle.circle(10,20)
turtle.left(5)
turtle.circle(10,5)
turtle.end_fill()
turtle.penup()

#beard
turtle.speed(1)
turtle.pensize(3)
turtle.goto(15,25)
turtle.pencolor("black")
turtle.pendown()
turtle.fillcolor("black")
#make upside down trianlge as chin hair beard
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(10)
turtle.setheading(270)
turtle.right(10)
turtle.forward(25)
turtle.goto(15,25)
turtle.end_fill()

#glasses
turtle.setheading(90)
turtle.penup()
turtle.pencolor("DeepPink")
turtle.forward(105)
turtle.setheading(180)
turtle.forward(30)
turtle.pendown()
#making old fashioned loop glasses
turtle.circle(20)
turtle.setheading(5)
turtle.forward(60)
turtle.setheading(180)
turtle.circle(20)
turtle.penup()


#unibrow
turtle.speed(10)
turtle.pensize(5)
turtle.goto(-40,125)
turtle.pencolor("black")
turtle.pendown()

#let's add some FLAIR! This makes a zig-zag unibrow
turtle.setheading(0)
turtle.left(45)
turtle.forward(10)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(5)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(10)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(5)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(5)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(5)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(5)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(5)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(5)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(10)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.setheading(0)
turtle.left(45)
turtle.forward(10)
turtle.setheading(0)
turtle.right(45)
turtle.forward(5)

turtle.exitonclick() #exits with click so that program ends but you can sit and take in the beauty of the graffiti

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
