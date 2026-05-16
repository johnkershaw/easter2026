import turtle 

WIDTH =  800
HEIGHT = 400
screen = turtle.Screen()
screen.setup (WIDTH, HEIGHT)
t = turtle.Turtle()

def draw_chick(x = 90, colour = 'yellow'):
 t.circle(50)
 t.fillcolor(colour)
 t.begin_fill()
 t.forward(x)
 t.pendown()
 t.back(30)
 t.forward(70)
 t.seth(180)
 t.end_fill()

# body 
t.penup()
t.goto(60, 60)
t.pendown()
t.begin_fill()
t.fillcolor('orange')
t.circle(40)

# head
t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.fillcolor()
t.circle(80)
t.end_fill()

turtle.done()