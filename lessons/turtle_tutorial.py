from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()

leo.color(99, 204, 250)
leo.pencolor("pink")

leo.penup()
leo.goto(-120, -100)
leo.pendown()

leo.fillcolor(32, 67, 93)
leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

bob: Turtle = Turtle()
bob.speed(100)
bob.hideturtle()

bob.color("black")
bob.pencolor("black")

bob.penup()
bob.goto(-120, -100)
bob.pendown()

side_length: int = 300
 
i: int = 0
while (i < 5):
    bob.forward(side_length)
    bob.left(122)
    i += 1

done()