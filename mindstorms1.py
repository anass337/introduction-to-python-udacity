import turtle
window = turtle.Screen()
window.bgcolor("red")
def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(0, 4):             
        brad.forward(100)
        brad.right(90)
    
 

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
   

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("red")
    trian = turtle.Turtle()
    trian.shape("arrow")
    trian.color("green")
    trian.speed(2)
    for i in range(0, 3):
        trian.forward(100)
        trian.right(120)
   


draw_square()
draw_circle()
draw_triangle()
window.exitonclick()

