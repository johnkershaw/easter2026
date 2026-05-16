import turtle
import random


WIDTH, HEIGHT = 800, 400
scr = turtle.Screen()
scr.setup(WIDTH, HEIGHT)
scr.tracer(0)

t = turtle.Turtle()


t.speed(0)


def draw_crown():
   r1 = random.randint(1,180)
   r2 = random.randint(1, 45)
   for i in range(360):
       t.circle(100, 1)
       t.left(r2)
       t.forward(r2)
       t.back(r2)
       t.right(r2)
       r2 = random.randint(1, 45)
       t.right(r2)
       t.forward(r2)
       t.back(r2)
       t.left(r2)
       r2 = random.randint(1, 45)
       t.circle(100, 10)
       t.left(r2)
       t.forward(r2)
       t.back(r2)
       t.right(r2)
       r2 = random.randint(1, 45)
       t.right(r2)
       t.forward(r2)
       t.back(r2)
       t.left(r2)
       r2 = random.randint(1, 45)


def draw_cross(value1, value2, value3):
   t.forward(value1)
   t.left(90)
   t.forward(value2)
   t.right(90)
   t.forward(value3)
   t.left(90)
   t.forward(value3)
   t.left(90)
   t.forward(value3)
   t.right(90)
   t.forward(value3)
   t.left(90)
   t.forward(value3)
   t.left(90)
   t.forward(value3)


draw_crown()


t.right(90)
t.forward(100)
t.left(90)


draw_cross(25, 75, 50)

scr.update()
turtle.done()