import turtle

myTurtle = turtle.Turtle()
myTurtle.speed(10)

myTurtle.penup()
myTurtle.goto(50, 0)
myTurtle.pendown()

myTurtle.color("brown", "brown")

myTurtle.begin_fill()
for i in range(4):
    myTurtle.forward(20)
    myTurtle.right(90)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(0, 0)
myTurtle.pendown()

myTurtle.color("green", "green")

myTurtle.begin_fill()
for i in range(3):
    myTurtle.forward(130)
    myTurtle.left(120)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(0, 50)
myTurtle.pendown()

myTurtle.begin_fill()
for i in range(3):
    myTurtle.forward(130)
    myTurtle.left(120)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(0, 110)
myTurtle.pendown()

myTurtle.begin_fill()
for i in range(3):
    myTurtle.forward(130)
    myTurtle.left(120)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(40, 230)
myTurtle.pendown()

myTurtle.color("yellow", "yellow")

myTurtle.begin_fill()
for i in range(5):
    myTurtle.forward(50)
    myTurtle.right(144)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(30, 130)
myTurtle.pendown()

myTurtle.color("blue", "blue")

myTurtle.begin_fill()
myTurtle.circle(10)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(70, 100)
myTurtle.pendown()

myTurtle.begin_fill()
myTurtle.circle(10)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(80, 50)
myTurtle.pendown()

myTurtle.begin_fill()
myTurtle.circle(10)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(55, 170)
myTurtle.pendown()

myTurtle.color("red", "red")

myTurtle.begin_fill()
myTurtle.circle(10)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(70, 140)
myTurtle.pendown()

myTurtle.begin_fill()
myTurtle.circle(10)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(30, 60)
myTurtle.pendown()

myTurtle.begin_fill()
myTurtle.circle(10)
myTurtle.end_fill()

myTurtle.color("silver", "silver")

myTurtle.penup()
myTurtle.goto(90, 130)
myTurtle.pendown()

myTurtle.begin_fill()
myTurtle.circle(10)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(70, 75)
myTurtle.pendown()

myTurtle.begin_fill()
myTurtle.circle(10)
myTurtle.end_fill()

myTurtle.penup()
myTurtle.goto(70, 10)
myTurtle.pendown()

myTurtle.begin_fill()
myTurtle.circle(10)
myTurtle.end_fill()

