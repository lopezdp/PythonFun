import turtle

def draw_diamonds():
    dia = turtle.Turtle()
    dia.shape("turtle")
    dia.color("blue")
    dia.speed(10)

    for i in range(72):
        dia.forward(100)
        dia.right(45)
        dia.forward(100)
        dia.right(135)
        dia.forward(100)
        dia.right(45)
        dia.forward(100)

        dia.right(10)

    dia.right(90)
    dia.forward(300)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("grey")

    draw_diamonds()

    window.exitonclick()

draw_flower()

    
