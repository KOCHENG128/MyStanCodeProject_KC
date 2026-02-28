"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
CAP_POINT = 1000        # 10 (points per brick) * BRICK_ROWS * BRICK_COLS


def main():
    number_lives = NUM_LIVES
    graphics = BreakoutGraphics()
    # window, ball, paddle, score 不需要用getter
    dx = 0
    dy = 0

    # Add the animation loop here!

    while number_lives > 0 and graphics.brick_count > 0:
        while dx == 0:
            pause(FRAME_RATE)
            if graphics.mouse_click_count != 0:  # 如果點擊，才獲取速度，否則繼續維持1
                dx = graphics.get_dx()
                dy = graphics.get_dy()
                break
        graphics.ball.move(dx, dy)  # 點擊後 while 迴圈終止，球開始移

        # check if touches the walls
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            dx = -dx
        if graphics.ball.y <= 0:
            dy = -dy
        # if touches the ground, click to restart
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.ball.x, graphics.ball.y = reset_ball_position(graphics.ball, graphics.window)
            dx = 0
            dy = 0
            graphics.reset_click_count()  # reset
            number_lives -= 1
        dx, dy, plus_point, minus_brick, collision_object = check_collision(graphics.window, graphics.paddle,
                                                                            graphics.ball, dx, dy, graphics.score)
        graphics.point += plus_point
        graphics.brick_count -= minus_brick
        graphics.score.text = "Score: " + str(graphics.point)
        # pause
        pause(FRAME_RATE)
    if graphics.brick_count == 0:  # 當全部磚塊打完了
        graphics.ball.x, graphics.ball.y = reset_ball_position(graphics.ball, graphics.window)
        dx = 0
        dy = 0


def check_collision(window, paddle, ball, dx, dy, score):
    # define possible collision points
    collision_point1 = window.get_object_at(ball.x, ball.y)
    collision_point2 = window.get_object_at(ball.x + ball.width, ball.y)
    collision_point3 = window.get_object_at(ball.x + ball.width, ball.y + ball.height)
    collision_point4 = window.get_object_at(ball.x, ball.y + ball.height)

    # define plus point
    plus_point = 0

    # find collision object
    collision_object = None
    if collision_point1 is not None:
        collision_object = collision_point1
    elif collision_point2 is not None:
        collision_object = collision_point2
    elif collision_point3 is not None:
        collision_object = collision_point3
    elif collision_point4 is not None:
        collision_object = collision_point4

    # bounce ball
    if collision_object is not None and collision_object is not score:
        if collision_object is paddle:
            if dy > 0:
                dy = -dy  # x軸方向速度不用變

        else:  # when collides with bricks
            if dy < 0:
                dy = -dy  # x軸方向速度不用變
            window.remove(collision_object)
            plus_point = 10  # 因為只會check 一次
            minus_brick = 1
    return dx, dy, plus_point, collision_object


def reset_ball_position(ball, window):
    ball.x = (window.width - ball.width) // 2
    ball.y = (window.height - ball.height) // 2
    return ball.x, ball.y


if __name__ == '__main__':
    main()
