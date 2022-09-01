from turtle import Turtle

MOVE_CONSTANTS = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def add_new_segment(self):
        segment = get_snake_single_segment()
        segment.goto((self.snake_segments[len(self.snake_segments) - 1].xcor(), self.snake_segments[len(self.snake_segments) - 1].ycor()))
        self.snake_segments.append(segment)

    def create_snake(self):
        for sb in range(3):
            segment = get_snake_single_segment()
            segment.goto(-1 * sb * 20, 0)
            self.snake_segments.append(segment)

    def move(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[seg].goto((self.snake_segments[seg - 1].xcor(), self.snake_segments[seg - 1].ycor()))
        self.head.forward(MOVE_CONSTANTS)

    def move_up(self):
        if self.head.heading() == DOWN:
            return
        # for seg in range(len(self.snake_segments) - 1, 0, -1):
        #    self.snake_segments[seg].setheading(self.snake_segments[seg-1].heading())
        self.head.setheading(UP)

    def move_down(self):
        print("move_down")
        if self.head.heading() == UP:
            return
        # for seg in range(len(self.snake_segments) - 1, 0, -1):
        #     self.snake_segments[seg].setheading(self.snake_segments[seg - 1].heading())
        self.head.setheading(DOWN)

    def move_left(self):

        print(f"move_left {self.head.heading()}")

        if self.head.heading() == RIGHT:
            return
        # for seg in range(len(self.snake_segments) - 1, 0, -1):
        #     self.snake_segments[seg].setheading(self.snake_segments[seg - 1].heading())
        self.head.setheading(LEFT)

    def move_right(self):
        print("move_right")
        if self.head.heading() == LEFT:
            return
        # for seg in range(len(self.snake_segments) - 1, 0, -1):
        #     self.snake_segments[seg].setheading(self.snake_segments[seg - 1].heading())
        self.head.setheading(RIGHT)


def get_snake_single_segment():  # this method doesn't uses any object inside the class, so kind of static method
    segment = Turtle()
    segment.penup()
    segment.shape("square")
    segment.color("white")
    return segment
