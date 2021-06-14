from turtle import Turtle
from gpiozero import Button
from time import sleep
harold = Turtle(shape = 'triangle')
forward = Button('BOARD37')
back = Button('BOARD33')
left = Button('BOARD22')
right = Button('BOARD35')
while not back.is_pressed:
    if forward.is_pressed:
        harold.forward(10)
    elif left.is_pressed:
        harold.left(22.5)
    elif right.is_pressed:
        harold.right(22.5)
    elif back.is_pressed:
        harold.clear()
    sleep(.1)