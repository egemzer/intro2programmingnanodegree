import turtle

#draws a triforce
def draw_triforce():
    window = turtle.Screen()
    window.bgcolor("white")
    index = 0
    triangles = 4 #there are 4 triangles in a triforc
    sides = 3
    deg = 120
    zelda = turtle.Turtle()
    zelda.shape("turtle")
    zelda.speed(1)
    zelda.color("orange")
    zelda.pencolor("orange")
    zelda.fillcolor("yellow")

    #draw the big left angled line
    zelda.left(120)
    zelda.forward(200)

    #draw the bottom left triangle
    zelda.left(120)
    zelda.forward(100)
    zelda.left(120)
    zelda.forward(100)

    #draw the bottom right triangle
    zelda.right(120)
    zelda.forward(100)
    zelda.right(120)
    zelda.forward(100)
    zelda.left(120)
    zelda.forward(100)

    #draw the big right angled line
    zelda.left(120)
    zelda.forward(200)
    
    
    window.exitonclick()

draw_triforce()
