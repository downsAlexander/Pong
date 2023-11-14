from turtle import Turtle
ALIGNMENT = 'center'
STYLE = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'{self.score}', align=ALIGNMENT, font=STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=STYLE)


    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


