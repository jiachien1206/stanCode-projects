"""
Name: 李佳謙 Chiachien Li
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program will set the rule that ball will rebound and the game will end.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3		# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # The number of live used for now
    n = 1
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        # If there are still lives to use and there is at least one brick in the window
        if n <= NUM_LIVES and graphics.b > 0:
            # Move the ball with the velocity of dx and dy
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            # The ball falls out of the bottom of the window
            if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                # Use one more live
                n += 1
                # Ball appears at the origin
                graphics.ball_origin()
            # The ball is out of the width of the window
            if graphics.ball.x <= 0 or graphics.window.width - graphics.ball.width <= graphics.ball.x:
                # Reverse the x velocity
                graphics.set_dx(-graphics.get_dx())
            # The ball goes over the top of the window
            if graphics.ball.y <= 0:
                # Reverse the y velocity
                graphics.set_dy(-graphics.get_dy())
            # The ball hits an object
            if graphics.check() is True:
                # The object hit is a brick
                if graphics.check_brick() is True:
                    # Remove the object
                    graphics.remove_brick()
                    # Minus the number of bricks by one
                    graphics.b -= 1
                    # Reverse the y velocity
                    graphics.set_dy(-graphics.get_dy())
                # The object hit is the paddle
                else:
                    # Only when the y velocity is positive the ball will rebound
                    if graphics.get_dy() > 0:
                        graphics.set_dy(-graphics.get_dy())
        # When runs out of lives or there is no brick in the window it this program will stop
        else:
            break


if __name__ == '__main__':
    main()
