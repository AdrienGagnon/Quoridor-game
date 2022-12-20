import turtle
import math




GRID_SIZE = 600

sub_divisions = 9

cell_size = GRID_SIZE / sub_divisions

cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2
scn = turtle.Screen()
scn.title("Quoridor")
scn.setup(width=800, height=800)
turtle=turtle.Turtle()
'turtle.hideturtle()'
turtle.speed("fastest")

turtle.penup()
turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
turtle.pendown()

angle = 90

for _ in range(4):
    turtle.forward(GRID_SIZE)
    turtle.right(angle)

for _ in range(2):
    for _ in range(1, sub_divisions):
        turtle.forward(cell_size)
        turtle.right(angle)
        turtle.forward(GRID_SIZE)
        turtle.left(angle)

        angle = -angle

    turtle.forward(cell_size)
    turtle.right(angle)

turtle.penup()
turtle.goto(-GRID_SIZE/2 + 35, -GRID_SIZE/2 - 20)
for x in range(9):
    turtle.write(f'{x + 1}', move=False, align='center', font=('Arial', 10, 'normal'))
    turtle.setx(-GRID_SIZE/2 + 35 + (x + 1) * 67)
turtle.goto(-GRID_SIZE/2 - 20, -GRID_SIZE/2 + 25)
for x in range(9):
    turtle.write(f'{x + 1}', move=False, align='center', font=('Arial', 10, 'normal'))
    turtle.sety(-GRID_SIZE/2 + 25 + (x + 1) * 67)

def remplir(x, y):
    turtle.setposition(x // 800, y)
    turtle.stamp()
    position = turtle.pos()  
    print(position)
turtle.onclick(remplir)

scn.mainloop()

