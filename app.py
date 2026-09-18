import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def doubleSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length = length + 5
doubleSquares(1)
square(5)

for i in range (60):
    doubleSquares(5)
    t.forward(10)
    t.right(10)