from turtle import Turtle


WINNER_NUMBER = 10


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1 = 0
        self.player_2 = 0
        self.penup()
        self.hideturtle()
        self.sety(y=320)
        self.color('white')
        self.show_score()
        self.line = []
        self.mid_line()

    def point_1(self):
        self.player_1 += 1
        self.clear()
        self.show_score()

    def point_2(self):
        self.player_2 += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f'   {self.player_1}', move=False, align='left', font=('Arial', 50, 'normal'))
        self.write(f'{self.player_2}   ', move=False, align='right', font=('Arial', 50, 'normal'))

    def mid_line(self):
        for c in range(12):
            line_part = Turtle(shape='square')
            line_part.shapesize(stretch_wid=0.35, stretch_len=2, outline=1)
            line_part.penup()
            line_part.sety(-350)
            line_part.color('white')
            line_part.setheading(90)
            line_part.forward(65*c)
            self.line.append(line_part)

    def show_winner(self):
        self.clear()
        for li in self.line:
            li.hideturtle()
        self.home()
        if self.player_1 == WINNER_NUMBER:
            self.write(f'END GAME!\n'
                       f'Player One {self.player_1} / {self.player_2} Player Two\n'
                       f'Player One Win The Game With {WINNER_NUMBER} points.',
                       move=False, align='center', font=('Arial', 30, 'normal'))
        else:
            self.write(f'END GAME!      \n'
                       f'Player One {self.player_1} / {self.player_2} Player Two     \n'
                       f'Player Two Win The Game With {WINNER_NUMBER} points.', move=False, align='center',
                       font=('Arial', 30, 'normal'))
