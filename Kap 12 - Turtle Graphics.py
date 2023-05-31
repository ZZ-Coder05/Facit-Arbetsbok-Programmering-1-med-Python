from turtle import *
import random as ran
import math as m

colormode(255)
bgcolor(0, 0, 0)
pencolor(255, 255, 255)
speed("fastest")
hideturtle()
tracer(1000, 1000)
pensize(1)
screensize(10000, 10000)


def cen_circle(x, y, rad):
    penup()
    goto(x, y - rad)
    pendown()
    circle(rad)


def line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)


def uppg1():
    # Röd cirkel
    begin_fill()
    pencolor(255, 0, 0)
    fillcolor(255, 0, 0)
    cen_circle(0, 0, 150)
    end_fill()

    # Blå cirkel
    begin_fill()
    pencolor(0, 0, 255)
    fillcolor(0, 0, 255)
    cen_circle(0, 0, 100)
    end_fill()

    # 2 röda streck
    penup()
    pencolor(255, 0, 0)
    fillcolor(255, 0, 0)
    seth(315)
    pensize(50)
    goto(-85, 85)

    pendown()
    fd(240)
    penup()
    seth(45)
    goto(-85, -85)

    pendown()
    fd(240)


def uppg2():
    for i in range(0, 50):
        penup()
        goto(ran.randrange(-300, 300), ran.randrange(-300, 300))
        pendown()
        dot(ran.randrange(1, 50), "white")


def uppg3():
    setworldcoordinates(-50, -50, 50, 50)
    pencolor(255, 255, 255)

    for i in range(1, 20):
        line(i - 10, -10, i - 10, 10)
        line(-10, i - 10, 10, i - 10)


def uppg4():
    def fill_box(x, y):
        penup()
        goto(m.floor(x), m.floor(y))
        pendown()

        begin_fill()
        fillcolor("green")
        line(m.floor(x), m.floor(y), m.ceil(x), m.floor(y))
        line(m.ceil(x), m.floor(y), m.ceil(x), m.ceil(y))
        line(m.ceil(x), m.ceil(y), m.floor(x), m.ceil(y))
        line(m.floor(x), m.ceil(y), m.floor(x), m.floor(y))
        end_fill()
        penup()

    setworldcoordinates(-10, -10, 10, 10)
    pencolor(255, 255, 255)

    for i in range(1, 20):
        line(i - 10, -10, i - 10, 10)
        line(-10, i - 10, 10, i - 10)

    onscreenclick(fill_box)
    mainloop()


def uppg5():
    setworldcoordinates(-50, -50, 50, 50)
    pencolor(255, 255, 255)

    for i in range(0, 20):
        line(-10, 10 - i, -10 + i, -10)


def uppg6():
    setworldcoordinates(-50, -50, 50, 50)
    pencolor(255, 255, 255)

    for i in range(0, 11):
        line(0, 10 - i, i, 0)
        line(i, 0, 0, i - 10)
        line(0, i - 10, -i, 0)
        line(-i, 0, 0, 10 - i)


def uppg7(length):
    for i in range(4):
        fd(length)
        rt(90)


def uppg8(radius):
    x = pos()[0]
    y = pos()[1]
    cen_circle(x, y, radius)
    penup()
    goto(x, y)
    pendown()


def uppg9(x, y, n, r):

    matrix = [[m.cos((x * 2 * m.pi) / n) * r for x in range(1, n + 1)],
              [m.sin((y * 2 * m.pi) / n) * r for y in range(1, n + 1)]]

    penup()
    goto(x + matrix[0][0], y + matrix[1][0])
    pendown()

    n1 = n - 2
    for f in range(n1, -1, -1):

        line(matrix[0][0], matrix[1][0], matrix[0][n - f - 1], matrix[1][n - f - 1])

    for i in range(1, n - 2):

        for j in range(n - i - 2, -1, -1):

            pencolor("white")
            line(matrix[0][i], matrix[1][i], matrix[0][n - j - 1], matrix[1][n - j - 1])
    line(matrix[0][n - 2], matrix[1][n - 2], matrix[0][n - 1], matrix[1][n - 1])


uppg9(0, 0, 20, 600)
update()
mainloop()
