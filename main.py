import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from socreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgpic("bgimage.gif")
my_screen.title("Snake Game")
my_screen.tracer(0)

# Making our snake to listen to the keys

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
my_screen.listen()
my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Left", fun=snake.left)
my_screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_inc()

    # detection Collion with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # detection collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            game_is_on = False
            scoreboard.game_over()


my_screen.exitonclick()


