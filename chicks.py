import turtle 

WIDTH =  800
HEIGHT = 400
screen = turtle.Screen()
screen.setup (WIDTH, HEIGHT)
t = turtle.Turtle()

def draw_chick(x=0, y=0, w=100, h=100, colour='yellow'):
    body(x, y, w, h)
    head(x + w * 0.5, y + h * 0.8, w * 0.5, h * 0.5)
    

def body(x, y, w, h):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor('orange')
    t.circle(w)
    t.end_fill()

def head(x, y, w, h, colour='yellow'):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    t.circle(w)
    t.end_fill()
    
    # beak
    t.fillcolor('orange')
    t.penup()
    t.goto(x + w*0.4, y + h*0.8)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.forward(w * 0.6)
    t.left(120)
    t.forward(w * 0.6)
    t.end_fill()

draw_chick(0, 0, 50, 50)
draw_chick(300, 0, 50, 50)
draw_chick(-300, 0, 50, 50)
t.hideturtle()

turtle.done()