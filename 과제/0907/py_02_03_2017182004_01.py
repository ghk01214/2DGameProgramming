import turtle

size = 200

def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

#기억 그리기
def draw_r():
    x, y = turtle.pos()
    turtle.setheading(0)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    move(x, y)

#ㅣ그리기
def draw_l():
    move(turtle.xcor() + size + 50, turtle.ycor() + 50)
    x, y = turtle.pos()
    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(size + 100)
    move(x, y)

#ㅁ그리기
def draw_a():
    x, y = turtle.pos()
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    move(x, y)

#ㅓ그리기
def draw_j():
    move(turtle.xcor() + size + 50, turtle.ycor() + 50)
    x, y = turtle.pos()
    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(size + 100)
    move(turtle.xcor() - 50, turtle.ycor() + (size + 100) / 2)
    turtle.left(90)
    turtle.forward(50)
    move(x, y)

#ㄴ그리기
def draw_s():
    x, y = turtle.pos()
    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    move(x, y)

#ㅎ그리기
def draw_g():
    x, y = turtle.pos()
    turtle.setheading(0)
    move(x + 25, y)
    turtle.forward(size - 50)
    move(x, y - 50)
    turtle.forward(size)
    move(x + size / 2, y - size - 50)
    turtle.circle((size - 50) / 2)
    move(x, y)

#ㅗ그리기
def draw_h():
    move(turtle.xcor() + size / 2, turtle.ycor() - size - 100)
    x, y = turtle.pos()
    turtle.right(90)
    turtle.forward(size / 2)
    move(x - size / 2, y - size / 2)
    turtle.left(90)
    turtle.forward(size)


#받침 그리기
def draw_final_consonant(consonant = None):
    move(turtle.xcor() - size, turtle.ycor() - size * 2 + 80)
    if consonant != None:
        consonant()
    move(turtle.xcor() + size + 80, turtle.ycor() + size * 2 - 130)


turtle.shape('turtle')

move(-450, 400)

draw_r()
draw_l()
draw_final_consonant(draw_a)

draw_r()
draw_j()
draw_final_consonant(draw_s)

draw_g()
draw_h()

turtle.exitonclick()