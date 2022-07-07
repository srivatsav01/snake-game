from turtle import  Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.highscore = 0
        self.goto(0, 260)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 20, "normal"))
        self.goto(150, 260)
        self.read_highscore()
        self.write(f"HighScore:{self.highscore}", align="center", font=("Arial", 20, "normal"))


    def read_highscore(self):
        with open("data.txt", "r") as file:
            content = file.read()
            self.highscore = int(content)
    def update_score(self):
        self.score += 20
        self.clear()
        self.goto(0, 260)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 20, "normal"))
        self.goto(150, 260)
        self.write(f"HighScore:{self.highscore}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        self.clear()
        if self.highscore < self.score:
            self.highscore = self.score
            with open("data.txt","w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.goto(0, 260)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 20, "normal"))
        self.goto(150, 260)
        self.write(f"HighScore:{self.highscore}", align="center", font=("Arial", 20, "normal"))




    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"GAME OVER \n your Score:{self.score}", align="center", font=("Arial", 20, "normal"))
