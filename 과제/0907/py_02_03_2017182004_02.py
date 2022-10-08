import turtle

size = 500

def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.shape('turtle')
x, y = turtle.pos()

for i in range(6):
    move(x, y + i * size / 5)
    turtle.setheading(0)
    turtle.forward(size)
    move(x + i * size / 5, y)
    turtle.left(90)
    turtle.forward(size)

turtle.exitonclick()