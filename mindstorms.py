import turtle

def draw_square(some_turtle):
    brad = turtle.Turtle()
    for i in range(1, 3):             
        some_turtle.forward(200)
        some_turtle.right(120)
        some_turtle.forward(100)
        some_turtle.right(60)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(0.01)
    for i in range(0,90):
        draw_square(brad)
        brad.right(4)
    #Create the turtle Angie - Draws a cirle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    window.exitonclick()

draw_art()

