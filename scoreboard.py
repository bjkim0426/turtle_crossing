from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'level: {self.current_level}', align='left', font=FONT)

    def increase_score(self):
        self.current_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color('black')
        self.write('GAME OVER', align='center', font=FONT)
