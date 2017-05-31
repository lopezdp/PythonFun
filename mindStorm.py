import turtle
import math
   
def draw_square():
    sq = turtle.Turtle()
    sq.shape("turtle")
    sq.color("blue")
    sq.speed(10)
    
    for i in range(4):
        sq.forward(200)
        sq.right(90)

def draw_circle():
    circ = turtle.Turtle()
    circ.shape("arrow")
    circ.color("red")

    circ.penup()
    circ.setpos(-150, 150)
    circ.pendown()
    circ.circle(100)

def draw_triangle():
    tr = turtle.Turtle()
    tr.shape("turtle")
    tr.color("yellow")

    tr.penup()
    tr.setpos(125,250)
    tr.pendown()

    tr.forward(200)
    tr.right(135)
    
    tr.forward(math.sqrt(200**2 + 200**2))
    tr.right(135)

    tr.forward(200)

def draw_objects():
    window = turtle.Screen()
    window.bgcolor("grey")

    draw_square()
    draw_circle()
    draw_triangle()
    
    window.exitonclick()
 
draw_objects()

 


