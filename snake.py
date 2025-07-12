from turtle import Turtle
START_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in START_POSITION:
          self.add_segment(positions)

    def add_segment(self, positions):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_nums in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_nums - 1].xcor()
            new_y = self.segments[seg_nums - 1].ycor()
            self.segments[seg_nums].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

