import turtle

WIDTH, HEIGHT = 800, 600
scr = turtle.Screen()
scr.setup(WIDTH, HEIGHT)

scr.tracer(0)

t = turtle.Turtle()

def tp(t: turtle.Turtle, x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

def rect(t: turtle.Turtle, w, h, c = "#FFFFFF"):
    t.fillcolor(c)
    t.begin_fill()
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.end_fill()

def cross(t: turtle.Turtle, w1, h1, w2, h2):
    rect(t, w1, h1, '#000000')
    t.left(90)
    t.fd(h1-(h2*2))
    t.right(90)
    t.back((w2-w1)/2)
    rect(t, w2, h2, '#000000')


tp(t, 0, -700)
t.fillcolor('#000000')
t.begin_fill()
t.circle(400)
t.end_fill()

tp(t, 0, -250)
t.fillcolor('#FFFFFF')
t.begin_fill()
t.circle(100)
t.end_fill()


tp(t, -10, 100)
cross(t, 20, 100, 75, 20)
tp(t, -80, 85)
cross(t, 18, 90, 67, 18)
tp(t, 62, 85)
cross(t, 18, 90, 67, 18)




scr.update()
turtle.done()