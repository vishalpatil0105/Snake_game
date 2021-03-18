from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)

    def reset_game(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        my_turtle = Turtle(shape="square")
        my_turtle.color("white")
        my_turtle.penup()
        my_turtle.goto(position)
        self.segments.append(my_turtle)

    def increase_snake_size(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_no - 1].xcor()
            new_y = self.segments[segment_no - 1].ycor()
            self.segments[segment_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # self.head.forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # self.head.forward(MOVE_DISTANCE)











