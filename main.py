import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#000000")
screen.title("Snake Game")
screen.tracer(0)  # for disabling initial animation
food = Food()
score = Score()
snake = Snake()
screen.listen()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

is_moving = True
print(screen.window_width())


def is_collided_with_wall() :
    offset = 10

    if snake.head.xcor() >= screen.window_width() / 2 - offset or snake.head.xcor() <= -1 * screen.window_width() / 2 \
            + offset or snake.head.ycor() >= screen.window_height() / 2 - offset or snake.head.ycor() <= -1 \
            * screen.window_height() / 2 + offset:
        return True
    return False

def detect_wall_collision():
    offset = 10

    if snake.head.xcor() >= screen.window_width() / 2 - offset or snake.head.xcor() <= -1 * screen.window_width() / 2 \
            + offset or snake.head.ycor() >= screen.window_height() / 2 - offset or snake.head.ycor() <= -1 \
            * screen.window_height() / 2 + offset:
        return True

    return False

while is_moving:
    screen.update()
    time.sleep(0.2)
    if snake.head.distance(food) <= 15:  # 10+5
        print("collected food")
        food.change_position()
        score.update_score()
        snake.add_new_segment()
    elif detect_wall_collision():
        print("Game Over")
        score.game_over()
        is_moving = False
    else:
        # following loop is called slicing eg : array[2,5] // array [2:5:2]
        # for segment in snake.snake_segments[1:len(snake.snake_segments)-1]:
        for segment in snake.snake_segments[1:]:

            if snake.head.distance(segment) < 10:
                score.game_over()
                is_moving = False

        # for segment in snake.snake_segments:
        #     if segment == snake.head:
        #         pass
        #     elif snake.head.distance(segment) < 10:
        #         score.game_over()
        #         is_moving = False

    snake.move()


screen.exitonclick()
