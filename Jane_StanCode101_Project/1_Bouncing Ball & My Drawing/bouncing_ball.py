"""
File: bouncing_ball.py
Name: Jane Huang
-------------------------
TODO: This program is to perform a ball bouncing action
(參考Lecture 1- bouncing rect)
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
COUNT = 0

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball = set_up_ball()
    window.add(ball)
    onmouseclicked(bouncing_ball)


def bouncing_ball(mouse):
    global COUNT
    if COUNT < 3:
        ball = window.get_object_at(START_X + SIZE/2, START_Y + SIZE/2)
        vy = 0  # 還沒點滑鼠之前vy速度為0

        while ball.x + SIZE <= window.width:  # 當還沒碰到右邊牆壁前，不停移動
            vy += GRAVITY
            ball.move(VX, vy)
            if ball.y + SIZE >= window.height and vy > 0:  # 要設置為只要碰到地板，vy都是負數的，直到變成零就會在最高點，再往下掉
                vy = -vy * REDUCE
            elif ball.y + SIZE >= window.height and vy < 0:  # 有些情況當碰到地板時 vy 已經變成負的，這時再加負號就會出問題
                vy = vy * REDUCE
            pause(DELAY)
        vy = 0  # vy 重置
        COUNT += 1
        ball.x = START_X
        ball.y = START_Y


def set_up_ball():
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    ball.fill_color = 'black'
    return ball


if __name__ == "__main__":
    main()
