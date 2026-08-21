import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star Spiral Animation")
t = turtle.Turtle()
t.speed(0)
turtle.tracer(2)
t.hideturtle()

t.pensize(2)


for i in range(2):
  hue = 0.0
  t.goto(0,0)
  for i in range(200):
     color = colorsys.hsv_to_rgb(hue,1,1)#changes the color
     t.pencolor(color)
     t.forward(i*3)
     t.right(145)
     hue+= 0.005

  vue = 0.0
  t.goto(0,0)

  for i in range(200):
     color1 = colorsys.hsv_to_rgb(vue,1,1)#changes the color
     t.pencolor(color1)
     t.forward(i*3)
     t.left(145)
     vue+= 0.005



turtle.done()