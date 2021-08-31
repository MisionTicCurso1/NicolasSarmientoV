import turtle

canvas= turtle.Screen()
canvas.bgcolor('#9096e6')

pen= turtle.Turtle()
canvas.delay(-1)
pen.penup()

pen.pendown()
pen.pencolor('red')
pen.fillcolor('#000000')

pen.begin_fill()
while True:
    pen.fd(300)
    pen.left(130)

    if (pen.xcor()) <1:
        break

print(abs(pen.pos()))

pen.end_fill()

    

turtle.done()