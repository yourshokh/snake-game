from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen=Screen()
screen.setup(width=700, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)



snake=Snake()
food=Food()
score=Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        score.increase()
        snake.increase_snake()
        snake.extend()

    if snake.head.xcor() > 340:
        snake.game_is_over()
        game_is_on = False

    elif snake.head.xcor() < -340:
        snake.game_is_over()
        game_is_on = False

    elif snake.head.ycor() > 290:
        snake.game_is_over()
        game_is_on = False

    elif snake.head.ycor() < -290:
        snake.game_is_over()
        game_is_on = False


    for segment in snake.turtles[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            snake.game_is_over()























screen.exitonclick()