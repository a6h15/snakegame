from turtle import Turtle
import random



# # Create a heart shape
# heart = turtle.Turtle()
# heart.hideturtle()
# heart.penup()
# heart.goto(0, 0)
# heart.begin_poly()
#
# heart.goto(0, -10)
# heart.circle(10, 180)
# heart.goto(0, 0)
# heart.circle(10, -180)
# heart.goto(0, -10)
#
# heart.end_poly()
# turtle.register_shape("heart", heart.get_poly())


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("Yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
