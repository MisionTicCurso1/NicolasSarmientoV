import turtle
from typing import Text
from collections import deque
import random


window=turtle.Screen()
window.title('Tic Tac Toe')
window.setup(width=600, height=700)
window.delay(0)

line=turtle.Turtle()
line.hideturtle()
line.pu()
line.goto(-300,280)
line.pd()
line.fd(600)

titl=turtle.Turtle()
titl.hideturtle()
titl.pu()
titl.goto(-300,300)
titl.write('  TIC TAC TOE', font=('courier', 25))
titl.fd(400)
titl.write('Turn: ', font=('courier', 23))


row1=turtle.Turtle()
row1.hideturtle()
row1.penup()
row2=row1.clone()
row1.goto(-250,100)
row1.pendown()
row1.forward(500)

row2.goto(-250,-100)
row2.pd()
row2.fd(500)

col1=turtle.Turtle()
col1.pu()
col1.hideturtle()
col2=col1.clone()

col1.goto(-100,250)
col1.pd()
col1.right(90)
col1.fd(500)

col2.goto(100,250)
col2.pd()
col2.right(90)
col2.fd(500)

pos_x1=-230
pos_y1=220
pos_y2=-140

nums=turtle.Turtle()
nums.hideturtle()
nums.pu()
nums.goto(pos_x1, pos_y1)
nums.write('1', font=('courier', 20))

nums.goto(0, pos_y1)
nums.write('2', font=('courier', 20))

nums.goto(-pos_x1, pos_y1)
nums.write('3', font=('courier', 20))

nums.goto(pos_x1, 60)
nums.write('4', font=('courier', 20))

nums.goto(0, 60)
nums.write('5', font=('courier', 20))

nums.goto(-pos_x1, 60)
nums.write('6', font=('courier', 20))

nums.goto(pos_x1, pos_y2)
nums.write('7', font=('courier', 20))

nums.goto(0, pos_y2)
nums.write('8', font=('courier', 20))

nums.goto(-pos_x1,pos_y2)
nums.write('9', font=('courier', 20))


turn=deque(['O','X'])

board=[
    ['','',''],
    ['','',''],
    ['','','']
]




    
    


turtle.done()


