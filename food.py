from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food = Turtle()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # scale
        self.color("red")
        self.speed("fastest")
        self.change_position()
    def change_position(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

