from turtle import Turtle
WIDTH = 5
LENGTH = 1
X_START = 350
Y_START = 0


class Paddle1(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Paddle2(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

