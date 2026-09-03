import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Circle Animation")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

color_list = ["red", "blue", "green", "yellow", "purple", "orange"]

for i in range(150):
    pen.pencolor(color_list[i % len(color_list)])
    pen.circle(100)
    pen.left(3)

pen.hideturtle()

turtle.done()
