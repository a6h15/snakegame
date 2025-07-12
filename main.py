import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("snake gaym")
window.tracer(0)                        # need to use update to make something happen on the screen


snake = Snake()
food = Food()
scoreboard = Scoreboard()

window.listen()
window.onkey(snake.snake_up, "Up")
window.onkey(snake.snake_down,"Down")
window.onkey(snake.snake_left,"Left")
window.onkey(snake.snake_right,"Right")


game_on = True
while game_on:
    window.update()             # here it will make it move entire piece
    time.sleep(0.1)               # delay 1s after all segments have been moved(making it faster)

    snake.move()
    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # detect collision with head and tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

window.exitonclick()