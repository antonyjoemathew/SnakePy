from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONTSIZE = 15


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 240)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT, FONTSIZE, 'normal'))
    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=(FONT, FONTSIZE, 'normal'))

