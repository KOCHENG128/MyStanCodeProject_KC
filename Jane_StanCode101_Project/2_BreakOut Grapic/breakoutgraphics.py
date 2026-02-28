"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
This program has 4 milestones
1st milestone: To build window, paddle, ball and all the bricks

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball
MOUSE_CLICK_COUNT = 0  # Number total times of user clicking mouse


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT,
                            x=(self.window_width - PADDLE_WIDTH) // 2,
                            y=(self.window_height - PADDLE_HEIGHT - PADDLE_OFFSET))
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(2 * BALL_RADIUS, 2 * BALL_RADIUS,
                          x=(self.window_width - 2 * BALL_RADIUS) // 2,
                          y=(self.window_height - 2 * BALL_RADIUS) // 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.drop_ball)
        onmousemoved(self.move_paddle)
        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT,
                              x=i*(BRICK_WIDTH+BRICK_SPACING), y=j*(BRICK_HEIGHT+BRICK_SPACING))
                self.brick.filled = True
                if j % 10 <= 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'black'
                if 1 < j % 10 <= 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'black'
                if 3 < j % 10 <= 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'black'
                if 5 < j % 10 <= 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'black'
                if 7 < j % 10 <= 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'black'
                self.window.add(self.brick)
        # mouse_click_count
        self.mouse_click_count = MOUSE_CLICK_COUNT
        # brick count
        self.brick_count = BRICK_ROWS * BRICK_COLS
        # originally allow to click
        self.able_to_start = True
        # Add score sign
        self.point = 0
        self.score = GLabel("Score: " + str(self.point), x=0, y=self.window_height)
        self.score.font = '-15'
        self.window.add(self.score)
        # Add life sign

    # animation for paddle movement with the mouse
    # method 要寫在 init 外
    def move_paddle(self, mouse):
        if (PADDLE_WIDTH//2) <= mouse.x <= self.window_width-(PADDLE_WIDTH//2):
            self.paddle.x = mouse.x-(PADDLE_WIDTH//2)
            self.paddle.y = self.window_height - PADDLE_HEIGHT - PADDLE_OFFSET
        elif mouse.x < (PADDLE_WIDTH//2):
            self.paddle.x = 0
            self.paddle.y = self.window_height - PADDLE_HEIGHT - PADDLE_OFFSET
        else:
            self.paddle.x = self.window_width-PADDLE_WIDTH
            self.paddle.y = self.window_height - PADDLE_HEIGHT - PADDLE_OFFSET

    def drop_ball(self, mouse):
        if self.mouse_click_count == 0 and self.able_to_start:  # check
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.mouse_click_count += 1
            self.able_to_start = False  # after click for once, suspend

    def reset_click_count(self):
        self.mouse_click_count = 0
        self.able_to_start = True

    def get_dx(self):
       return self.__dx

    @staticmethod
    def get_dy():
        return INITIAL_Y_SPEED

    # 這些不是private，所以不用寫getter，用graphics.就可以選到了
    # def get_window(self):
    #     return self.window
    #
    # def get_ball(self):
    #     return self.ball
    #
    # def get_paddle(self):
    #     return self.paddle
    #
    # def get_score(self):
    #     return self.score


# 以下測試coder端
def test():
    graphics = BreakoutGraphics()


if __name__ == '__main__':
    test()
