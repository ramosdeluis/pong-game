from turtle import Turtle


BAR_SIZE = 5


class PlayerBar(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=1.0, stretch_len=BAR_SIZE, outline=1)
        if side == 'left':
            self.setposition(-390, 0)
        if side == 'right':
            self.setposition(380, 0)
        self.setheading(90)

    def move_up(self):
        if self.ycor() < 350:
            self.forward(40)

    def move_down(self):
        if self.ycor() > -350:
            self.backward(40)
