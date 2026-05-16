import turtle 

WIDTH =  800
HEIGHT = 400
screen = turtle.Screen()
screen.setup (WIDTH, HEIGHT)
t = turtle.Turtle()

def draw_chick(x=0, y=0, w=100, h=100, colour='yellow'):
    body(x, y, w, h)
    head(x + w/2, y + h/2, w/4, h/4)
    

def body(x, y, w, h):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor('orange')
    t.circle(40)

def head(x, y, w, h, colour='yellow'):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(colour)
    t.circle(50)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.end_fill()
    
    t.begin_fill()
    t.fillcolor()
    t.circle(80)
    t.end_fill()
    
    # beak
    t.begin_fill()
    t.forward(x)
    t.pendown()
    t.back(30)
    t.forward(70)
    t.seth(180)
    t.end_fill()

draw_chick(0, 0, 50, 50)
# draw_chick(100, 100, 50, 50)
# draw_chick(-100, 100, 50, 50)
turtle.done()