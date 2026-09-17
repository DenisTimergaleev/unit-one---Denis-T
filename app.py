import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(999)

for i in range (60):
    square(999)
    t.right(5)

turtle.done()
