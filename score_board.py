from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.new_level = 0
        self.score = Turtle()
        self.level()
        pass

    def level(self):
        self.new_level += 1
        self.score.clear()
        self.score.penup()
        self.score.goto(-260, 260)
        self.score.hideturtle()
        self.score.write(f"Level: {self.new_level}", move=False, align="left", font=FONT)
        pass

    def game_over(self):
        game = Turtle()
        game.hideturtle()
        game.write("GAME OVER", move=False, align="center", font=FONT)


