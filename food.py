from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        self.x=random.randint(-310,310)
        self.y=random.randint(-260,260)
        self.goto(self.x,self.y)
        self.screen.update()

    def refresh(self):
        self.x = random.randint(-310, 310)
        self.y = random.randint(-260, 260)
        self.goto(self.x, self.y)

        self.screen.update()

