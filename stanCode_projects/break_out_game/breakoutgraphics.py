"""
Name: 李佳謙 Chiachien Li
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program will setup the window, bricks, paddle, ball, velocity of the ball.
Check whether the ball hits bricks and remove the bricks.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2,
                            y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.start)
        onmousemoved(self.set_paddle)
        # Draw bricks
        self.b = 0
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)  # 想問這個為什麼一定要放裡面？
                self.b += 1
                self.window.add(self.brick, x=(brick_width+brick_spacing)*i,
                                y=brick_offset+(brick_height+brick_spacing)*j)
                self.brick.filled = True
                if j <= 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif j <= 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif j <= 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif j <= 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif j <= 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'

    def set_paddle(self, m):
        """
        Let paddle follow the mouse to move
        :param m: The information of mouse
        :return: The paddle's position
        """
        if self.__dx != 0 and self.__dy != 0:
            if m.x - self.paddle.width/2 < 0:
                self.paddle.x = 0
            elif m.x + self.paddle.width/2 > self.window.width:
                self.paddle.x = self.window.width-self.paddle.width
            else:
                self.paddle.x = m.x - (self.paddle.width/2)

    def get_dx(self):
        """
        To get dx
        :return: dx
        """
        return self.__dx

    def get_dy(self):
        """
        To get dy
        :return: dy
        """
        return self.__dy

    def set_dx(self, new_dx):
        """
        To set dx
        :return: dx
        """
        self.__dx = new_dx

    def set_dy(self, new_dy):
        """
        To set dy
        :return: dy
        """
        self.__dy = new_dy

    def start(self, y):  # Need to add the information of mouse
        """
        When the ball is not moving and is in the middle of the window, if mouse clicks ball will start to move.
        :param y: The information of mouse
        :return: Ball moves
        """
        if self.__dx == 0 and self.__dy == 0 and self.ball.x == (self.window.width-self.ball.width)/2\
                and self.ball.y == (self.window.height-self.ball.height)/2:
            self.ball_v()

    def ball_v(self):
        """
        Set the velocity of the ball
        :return: The balls velocity
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def check(self):
        """
        Check if the ball hits any objects and save the object as "maybe_brick"
        :return: True if ball hits any objects
        """
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            self.maybe_brick = self.window.get_object_at(self.ball.x, self.ball.y)
            return True
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) is not None:
            self.maybe_brick = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
            return True
        elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is not None:
            self.maybe_brick = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
            return True
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height) is not None:
            self.maybe_brick = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
            return True

    def check_brick(self):
        """
        Check whether maybe_object is paddle or brick
        :return: True if ball hits bricks
        """
        if self.maybe_brick is not self.paddle:
            return True

    def remove_brick(self):
        """
        Remove the object the ball hits
        """
        self.window.remove(self.maybe_brick)

    def ball_origin(self):
        """
        Take the ball back to the origin
        """
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2
        self.__dx = 0
        self.__dy = 0
