from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

COORDINATE_1 = 295
COORDINATE_2 = -295

snake = Snake()
screen = Screen()
food = Food()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.title(titlestring="My Snake Game")
screen.bgcolor("Black")
screen.tracer(0)

is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 18:
        food.refresh()
        score.increase_score()
        snake.increase_snake_size()

    # Detect collision with wall

    if snake.head.xcor() > COORDINATE_1 or \
            snake.head.xcor() < COORDINATE_2 or \
            snake.head.ycor() > COORDINATE_1 or \
            snake.head.ycor() < COORDINATE_2:
        score.reset()
        snake.reset_game()
        # is_on = False
        # score.game_over()

    # Detect collision with body

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # is_on = False
            # score.game_over()
            score.reset()
            snake.reset_game()
screen.exitonclick()
