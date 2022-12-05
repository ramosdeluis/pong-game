from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed(1)
        self.setheading(115)
        self.shapesize(stretch_wid=0.8, stretch_len=0.8, outline=1)

    def ball_move(self):
        self.forward(30)

    def change_angle(self):
        self.setheading(360-self.heading())

    def hit_player(self):
        self.setheading(180-self.heading())

    def reset_ball(self):
        self.hit_player()
        self.goto((0, 0))
