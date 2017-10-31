import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("pink")

    #draw a square
    sides = 4
    i = 0
    erika = turtle.Turtle()
    erika.shape("turtle")
    erika.color("white")
    erika.speed(3)
    
    while i < sides:
        erika.forward(100)
        erika.right(90)
        i += 1

    #draw a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    #draw a triangle
    sides2 = 3
    i2 = 0
    erika = turtle.Turtle()
    erika.shape("arrow")
    erika.color("yellow")
    while i2 < sides2:
        erika.forward(250)
        erika.right(120)
        i2 += 1

    window.exitonclick()

draw_shapes()
