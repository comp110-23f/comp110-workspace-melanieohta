"""A turtle draws a scene with trees, mountains, clouds, a sun, grass, and a river.

Breaks up complex functions: lines 48, 63, 77, 86, 94, 99, 103, 108, 111, 113, 118.
Try something fun: circle function line 81, bgcolor line 19.
"""
 
__author__ = "730671130"
 
from turtle import Turtle, colormode, done, tracer, update

colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    # TODO: Declare your Turtle variable(s) here.
    squirtle: Turtle = Turtle()
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    # background
    squirtle.screen.bgcolor("sky blue")
    # components
    tree(squirtle, -300, -200)
    mountain(squirtle, -225, -200)
    tree(squirtle, -50, -200)
    mountain(squirtle, 50, -200)
    tree(squirtle, 225, -200)
    rectangle(squirtle, -400, -400, 750, 200, "dark blue", "royal blue")  # river
    rectangle(squirtle, -400, -250, 750, 50, "dark green", "green")  # grass
    sun(squirtle, -270.0, 200.0)
    cloud(squirtle, -100.0, 200.0)
    cloud(squirtle, 200.0, 200.0)
    # finish
    update()
    done()
 

# TODO: Define the procedures for other components in your scene here.
def initialize_turtle(turtle: Turtle, x: float, y: float, color: str) -> None:
    """Initializes turtle at x, y, and with a color."""
    turtle.color(color)  
    turtle.penup()
    turtle.goto(x, y) 
    turtle.setheading(0.0)
    turtle.pendown()


def rectangle(turtle: Turtle, x: float, y: float, width: int, length: int, border_color: str, fill_color: str) -> None:
    """Draws a rectangle of the given width and length whose bottom-left corner is located at x, y."""
    initialize_turtle(turtle, x, y, border_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    i: int = 0
    while i < 2:
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        i += 1
    turtle.end_fill()


def triangle(turtle: Turtle, x: float, y: float, base: int, side_length: int, border_color: str, fill_color: str, b_angle: float, s_angle: float) -> None:
    """Draws a triangle with given side lengths and color at x, y."""
    initialize_turtle(turtle, x, y, border_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(180 - b_angle)
    turtle.forward(side_length)
    turtle.left(180 - s_angle)
    turtle.forward(side_length)
    turtle.left(180)
    turtle.end_fill()


def draw_circle(turtle: Turtle, radius: int, x: float, y: float, border_color: str, fill_color: str) -> None:
    """Draws a circle with given radius and color at x, y."""
    initialize_turtle(turtle, x, y, border_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def tree(turtle: Turtle, x: float, y: float) -> None:
    """Draws a tree utilizing the rectangle function."""
    rectangle(turtle, x, y, 25, 100, "brown", "saddle brown")
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    x -= 25
    y += 100
    rectangle(turtle, x, y, 75, 75, "dark green", "green")


def mountain(turtle: Turtle, x: float, y: float) -> None:
    """Draws a mountain utilizing the triangle function."""
    triangle(turtle, x, y, 150, 350, "black", "grey", 77.626, 24.747)
    turtle.forward(250)
    x += 53
    y += 245
    triangle(turtle, x, y, 43, 100, "black", "white", 77.626, 24.747)


def cloud(turtle: Turtle, x: float, y: float) -> None:
    """Draws a cloud utilizing the circle function."""
    draw_circle(turtle, 55, x, y, "white", "white")
    x -= 35
    y -= 35
    draw_circle(turtle, 55, x, y, "white", "white")
    x += 70
    draw_circle(turtle, 55, x, y, "white", "white")


def sun(turtle: Turtle, x: float, y: float) -> None:
    """Draws a sun with rays utilizing the circle function."""
    draw_circle(turtle, 50, x, y, "gold", "yellow")
    turtle.color("yellow")
    turtle.setheading(90.0)
    turtle.forward(50)
    i: int = 0
    while i < 10:
        turtle.forward(75)
        turtle.left(180)
        turtle.forward(75)
        turtle.right(120)
        i += 1


# TODO: Use the __name__ is "__main__" idiom shown in class
if __name__ == "__main__":
    main()