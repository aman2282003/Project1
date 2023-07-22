from turtle import *

t = Turtle()
aman = Screen()
aman.title("My First Turtle")   # for changing the title
aman.bgcolor("Skyblue")         # for changing the background color

t.shape("turtle")
t.color("red", "green")
t.speed(1)  # Change the speed of the turtle

# Draw a square
t.penup()
t.goto(-150, 0)
t.pendown()
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# Draw a triangle
t.penup()
t.goto(150, 0)
t.pendown()
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

done()
