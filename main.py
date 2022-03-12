import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def spirograph(size):
    for _ in range(int(360 / size)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(50)
        current_heading = tim.heading()
        tim.setheading(current_heading + 5)


spirograph(5)

turtle.exitonclick()
