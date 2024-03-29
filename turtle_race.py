from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

red = Turtle()
red.color('red')
red.shape('turtle')

red.penup()
red.goto(-160, 100)
red.pendown()

for turn in range(10):
  red.right(36)

blue = Turtle()
blue.color('blue')
blue.shape('turtle')

blue.penup()
blue.goto(-160, 70)
blue.pendown()

for turn in range(72):
  blue.left(5)

green = Turtle()
green.shape('turtle')
green.color('green')

green.penup()
green.goto(-160, 40)
green.pendown()

for turn in range(60):
  green.right(6)

turquoise = Turtle()
turquoise.shape('turtle')
turquoise.color('turquoise')

turquoise.penup()
turquoise.goto(-160, 10)
turquoise.pendown()

for turn in range(30):
  turquoise.left(12)


for turn in range(100):
  red.forward(randint(1, 5))
  blue.forward(randint(1, 5))
  green.forward(randint(1, 5))
  turquoise.forward(randint(1, 5))
