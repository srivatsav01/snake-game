
from turtle import Turtle, Screen
from snake import Snake
from foods import  Food
from scoreboard import  Scoreboard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)

snake = Snake()
food = Food()
food.move_food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score = Scoreboard()

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    x_cor = snake.head.xcor()
    #detecting collisions with food
    if snake.head.distance(food) < 15:
        food.move_food()
        score.update_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 20:
            score.reset()
            snake.reset()


#
#
# print("your score is",score.score)
screen.exitonclick()