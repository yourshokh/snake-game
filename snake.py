from turtle import Turtle
# from food import Food
POSITIONS= [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST=20

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.turtles = []
        self.create_snake()
        self.GAME_IS_ON = True
        self.head=self.turtles[0]
        self.head.color('green')

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)
    def add_segment(self, pos):
        ilon = Turtle('square')
        ilon.color('white')
        ilon.speed()
        ilon.penup()
        ilon.goto(pos)
        self.turtles.append(ilon)
    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def increase_snake(self):
        x, y=self.turtles[-1].pos()

        cor=(x,y)
        POSITIONS.append(cor)




    def move(self):

        for num in range(len(self.turtles) - 1, 0, -1):
            x_cor = self.turtles[num - 1].xcor()
            y_cor = self.turtles[num - 1].ycor()
            self.turtles[num].goto(x_cor, y_cor)


        self.turtles[0].forward(MOVE_DIST)



    def game_is_on(self):
        return self.GAME_IS_ON
    def up(self):

        if self.turtles[0].heading()==0:
            self.turtles[0].left(90)
        elif self.turtles[0].heading()==180:
            self.turtles[0].right(90)
    def down(self):

        if self.turtles[0].heading()==0:
            self.turtles[0].right(90)
        elif self.turtles[0].heading()==180:
            self.turtles[0].left(90)
    def right(self):

        if self.turtles[0].heading()==90:
            self.turtles[0].right(90)
        elif self.turtles[0].heading()==270:
            self.turtles[0].left(90)
    def left(self):

        if self.turtles[0].heading()==90:
            self.turtles[0].left(90)
        elif self.turtles[0].heading()==270:
            self.turtles[0].right(90)
    def game_is_over(self):
        self.penup()
        self.hideturtle()
        self.goto(-10,-10)
        self.color('white')
        self.write(f'GAME IS OVER', True, align="left", font=("Arial",16,"normal"))

