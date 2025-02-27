import turtle
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
turtle.bgcolor('white')
tr = turtle.Turtle()
tr.speed("fastest")
tr.up()
# left decoration
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(-500, 0)
        tr.down()
        tr.color("purple")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("violet")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()
# right decoration
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(470, 0)
        tr.down()
        tr.color("red")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("crimson")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()
# top decoration
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(20, 265)
        tr.down()
        tr.color("forest green")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("lime")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()
# bottom decoration
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(20, -220)
        tr.down()
        tr.color("dark turquoise")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("cyan")
        tr.forward(50)
        tr.right(120)
    tr.right(30)


turtle.up()
turtle.color('red')
turtle.goto(-320, 40)
turtle.write("Happy ",  font=(None, 60))
turtle.goto(-60, 40)
turtle.color('deep pink')
turtle.write("New",  font=(None, 60))
turtle.goto(145, 40)
turtle.color('blue')
turtle.write("Year",  font=(None, 60))
turtle.goto(-74, -60)
turtle.color('green')
turtle.write("2023!", font=(None, 60))
turtle.don
