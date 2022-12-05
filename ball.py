from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed(1)
        self.x_move = 10
        self.y_move = 10
        self.shapesize(stretch_wid=0.8, stretch_len=0.8, outline=1)

    def ball_move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def hit_y(self):
        self.y_move *= -1

    def hit_player(self):
        self.x_move *= -1

    def reset_ball(self):
        self.hit_player()
        self.goto((0, 0))
