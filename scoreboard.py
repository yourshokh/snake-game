from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()

        self.hideturtle()

        self.update_screen()
    def update_screen(self):
        self.goto(0, 270)
        self.write(f'Score: {self.score}', True, align="left", font=("Arial",12,"normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.update_screen()