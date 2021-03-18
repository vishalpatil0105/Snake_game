from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")
SCORE_X = 0
SCORE_Y = 270


class Scoreboard(Turtle):
    def __init__(self):
        self.score_user = 0
        with open("score.txt") as score:
            self.high_score = int(score.read())
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(SCORE_X, SCORE_Y)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Your Score = {self.score_user} High Score = {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score_user > self.high_score:
            self.high_score = self.score_user
            with open("score.txt", mode="w") as score:
                score.write(f"{self.high_score}")

        self.score_user = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"Game Over Your score is: {self.score_user}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_user += 1
        self.update_score()




