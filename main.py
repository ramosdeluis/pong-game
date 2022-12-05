# TODO: Player bar
# TODO: Score Board
# TODO: Ball
from time import sleep


from player_bar import PlayerBar
from turtle import Screen
from board import Board
from ball import Ball


WINNER_NUMBER = 10
SLEEP = 0.1


screen = Screen()
screen.screensize(750, 750)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

board = Board()
ball = Ball()
player_1 = PlayerBar('left')
player_2 = PlayerBar('right')


screen.listen()
screen.onkey(player_1.move_up, 'w')
screen.onkey(player_1.move_down, 's')
screen.onkey(player_2.move_up, 'i')
screen.onkey(player_2.move_down, 'k')

is_game_on = True
while is_game_on:
    screen.update()
    sleep(SLEEP)

    # Detect collision with the wall.
    if ball.ycor() >= 350 or ball.ycor() <= -350:
        ball.hit_y()

    # Detect collision with the player
    if ball.distance(player_1) <= 50 and ball.xcor() < -355 or ball.distance(player_2) <= 50 and ball.xcor() > 350:
        ball.hit_player()
        if SLEEP - 0.005 > 0:
            SLEEP -= 0.005

    # Detect right point.
    if ball.xcor() > 375:
        board.point_2()
        ball.reset_ball()

    # Detect left point.
    if ball.xcor() < -375:
        board.point_1()
        ball.reset_ball()

    ball.ball_move()

    # Ending game.
    if board.player_1 == WINNER_NUMBER or board.player_2 == WINNER_NUMBER:
        is_game_on = False

board.show_winner()
ball.hideturtle()
screen.update()

screen.exitonclick()
