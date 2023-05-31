from turtle import *


def init():
    colormode(255)
    bgcolor(0, 0, 0)
    pencolor(255, 255, 255)
    speed(0)
    hideturtle()
    tracer(1000, 0)
    pensize(1)
    screensize(3000, 3000)

    penup()
    goto(-300, 300)
    pendown()


def run():
    update()
    mainloop()


# Uppgift 1
def countdown(n):
    if n == 0:
        return n
    else:
        print(n)
        return countdown(n - 1)


# Uppgift 2
def dec_to_bin(d):
    if d < 2:
        return d
    else:
        return str(dec_to_bin(d // 2)) + str(d % 2)


# Uppgift 3
def mul(a, b):
    if b == 1:
        return a
    else:
        return a + mul(a, b - 1)


# Uppgift 4
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def fib_table():
    for i in range(40):
        print("{:<5d}{:<3d}".format(i, fib(i)))


# Uppgift 5
def koch(level, length, angle):
    if level == 0:
        forward(length)
    else:
        koch(level - 1, length / 3, angle)
        left(angle)
        koch(level - 1, length / 3, angle)
        right(2*angle)
        koch(level - 1, length / 3, angle)
        left(angle)
        koch(level - 1, length / 3, angle)


def uppg5():
    for i in [0, 120, 120]:
        right(i)
        koch(10, 600, 60)


# Uppgift 6
def tree(depth, length):

    if depth > 0:

        color(255, 0, 0)
        fd(length)
        rt(60)

        tree(depth - 1, 0.6 * length)

        color(0, 255 // (depth * 2), 0)
        lt(120)
        tree(depth - 1, 0.6 * length)
        rt(60)
        bk(length)


def uppg6():
    setheading(90)
    penup()
    setposition(0, -400)
    pendown()

    tree(15, 300)


# Uppgift 1 och 2
def s_tri(depth, size, angle):
    if depth == 0:
        for _ in range(3):
            fd(size)
            lt(2 * angle)

    else:
        s_tri(depth - 1, size / 2, angle)
        fd(size / 2)
        s_tri(depth - 1, size / 2, angle)
        bk(size / 2)
        lt(angle)
        fd(size / 2)
        rt(angle)
        s_tri(depth - 1, size / 2, angle)
        lt(angle)
        bk(size / 2)
        rt(angle)


def uppg7():
    setheading(0)
    penup()
    setposition(-1500, -1500)
    pendown()

    s_tri(10, 3000, 60)


def main():

    init()
    #uppg5()
    #uppg6()
    uppg7()
    run()


main()
