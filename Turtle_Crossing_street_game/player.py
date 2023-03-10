from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.from_starting_point()
        self.setheading(90)

    def from_starting_point(self):
        self.goto(STARTING_POSITION)

    def move(self):
        """new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)"""
        self.forward(MOVE_DISTANCE)

    def reach_end_point(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True


