print("Pham Tuan Dat")
print("235752021610105")
import turtle
import random
screen = turtle.Screen()
screen.bgcolor("white")
painter = turtle.Turtle()
painter.speed(0)  
painter.pensize(2)
colors = ["red", "green", "blue"]
for i in range(12):  
    painter.pencolor(colors[i % len(colors)])  
    painter.circle(100)  
    painter.right(30)  
turtle.done()
