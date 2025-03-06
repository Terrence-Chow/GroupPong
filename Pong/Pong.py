"""Creation of the PONG game."""
from tkinter import *
import random


class GUI:
    """Class for GUI."""

    CANVAS_WIDTH = 1000
    CANVAS_HEIGHT = 600

    def __init__(self):
        """Initialise the GUI."""
        # Create the window
        self.window = Tk()
        self.canvas = Canvas(self.window,
                             width=f"{self.CANVAS_WIDTH}",
                             height=self.CANVAS_HEIGHT,
                             background="black")
        self.canvas.create_line(self.CANVAS_WIDTH/2, 80, self.CANVAS_WIDTH/2, 570, dash=(20), width=2, fill="white")

        self.canvas.pack()

        self.title = self.canvas.create_text(self.CANVAS_WIDTH / 2,
                                             50,
                                             text="PONG",
                                             fill="white")
        self.right_number = 0
        self.left_number = 0
        self.right_score = self.canvas.create_text(
            (self.CANVAS_WIDTH / 2) + 100,
            50,
            text=f"{self.right_number}",
            fill="white")
        self.left_score = self.canvas.create_text(
            (self.CANVAS_WIDTH / 2) - 100,
            50,
            text=f"{self.left_number}",
            fill="white")

        # Create the objects for the game - paddles and ball
        self.left = Paddle(self.canvas, 25, self.window)
        self.right = Paddle(self.canvas, self.CANVAS_WIDTH - 25, self.window)
        self.ball = Ball(self.canvas, 5, 50, self.window, 5, self)

        # Bind all the keys
        binding = [self.left.move_up, self.left.move_down,
                   self.right.move_up, self.right.move_down,
                   self.right.stop_moving_down, self.right.stop_moving_up,
                   self.left.stop_moving_down, self.left.stop_moving_up]
        binding_keys = ["w", "s", "<Up>", "<Down>", "<KeyRelease-Down>", "<KeyRelease-Up>",
                        "<KeyRelease-s>", "<KeyRelease-w>"]
        for i in range(0, len(binding_keys)):
            self.window.bind(binding_keys[i], binding[i])


        self.ball.move_random()
        # This line has to be at the end of this function
        self.window.mainloop()

    def right_gain_point(self):
        """Gains point after the right paddle misses the ball."""
        self.right_number += 1
        self.canvas.itemconfig(self.right_score,
                               text=f'{self.right_number}',
                               fill='white')

    def left_gain_point(self):
        """Gains point after the left paddle misses the ball."""
        self.left_number += 1
        self.canvas.itemconfig(self.left_score,
                               text=f'{self.left_number}',
                               fill='white')

    def get_right_paddle_coords(self):
        """Make a list of the coordinates of the right paddle."""
        return self.right.get_position()

    def get_left_paddle_coords(self):
        """Make a list of the coordintes of the left paddle."""
        return self.left.get_position()


class Paddle:
    """Created paddles."""

    WIDTH_OF_PADDLE = 10
    HEIGHT_OF_PADDLE = 100
    Y_START_PADDLE = GUI.CANVAS_HEIGHT / 2.5
    Y_VEL = 15

    def __init__(self, canvas, x_coord, window):
        """Create the paddle."""
        self.after_call_up = None
        self.after_call_down = None
        self.canvas = canvas
        self.window = window
        self.x_start_paddle = x_coord
        self.paddle = self.canvas.create_rectangle(
            self.x_start_paddle,
            self.Y_START_PADDLE,
            self.x_start_paddle + self.WIDTH_OF_PADDLE,
            self.Y_START_PADDLE + self.HEIGHT_OF_PADDLE,
            fill="white")

    def move_up(self, event=None):
        """Allow the paddle to move up."""
        # Check if paddle is at the top of the screen before moving
        if self.canvas.coords(self.paddle)[1] > 0:
            self.canvas.move(self.paddle, 0, -self.Y_VEL)
            # Function calls itself if key is still held down
            self.after_call_up = self.window.after(16, self.move_up)

    def move_down(self, event=None):
        """Allow the paddle to move down."""
        if self.canvas.coords(self.paddle)[3] < GUI.CANVAS_HEIGHT:
            self.canvas.move(self.paddle, 0, self.Y_VEL)
            self.after_call_down = self.window.after(16, self.move_down)

    def stop_moving_down(self, event=None):
        """Stop the paddle from moving down."""
        self.window.after_cancel(self.after_call_down)

    def stop_moving_up(self, event=None):
        """Stop the paddle from moving up."""
        self.window.after_cancel(self.after_call_up)

    def get_position(self):
        """Return the coordinates of th paddle."""
        return self.canvas.coords(self.paddle)


class Ball:
    """Created the ball."""

    WIDTH_OF_BALL = 15
    HEIGHT_OF_BALL = 15
    Y_START_BALL = GUI.CANVAS_HEIGHT / 2.2

    def __init__(self, canvas, y_yel, x_coord, window, x_vel, gui):
        """Create the window."""
        self.after_call_ball = None
        self.window = window
        self.canvas = canvas
        self.y_vel = y_yel
        self.x_vel = x_vel
        self.gui = gui
        self.turning = False

        self.x_start_ball = x_coord
        self.ball = self.canvas.create_oval(
            self.x_start_ball,
            self.Y_START_BALL,
            self.x_start_ball + self.WIDTH_OF_BALL,
            self.Y_START_BALL + self.HEIGHT_OF_BALL,
            fill="white")

    def move_random(self):
        """Allow the ball to move randomly."""
        self.canvas.move(self.ball, self.x_vel, self.y_vel)

        self.check_hit_paddle()

        if self.canvas.coords(self.ball)[0] < 0:
            self.canvas.move(self.ball, GUI.CANVAS_WIDTH / 2, 0)
            GUI.right_gain_point(self.gui)
        if self.canvas.coords(self.ball)[2] > GUI.CANVAS_WIDTH:
            self.canvas.move(self.ball, -GUI.CANVAS_WIDTH / 2, 0)
            GUI.left_gain_point(self.gui)
        if self.canvas.coords(self.ball)[3] > 600 or \
                self.canvas.coords(self.ball)[1] < 2:
            self.y_vel = -self.y_vel

        self.after_call_ball = self.window.after(16, self.move_random)

    def check_hit_paddle(self):
        """Check if the ball hits the paddle."""
        right_pos = GUI.get_right_paddle_coords(self.gui)
        left_pos = GUI.get_left_paddle_coords(self.gui)
        if ((self.ball in self.canvas.find_overlapping(
                right_pos[0], right_pos[1], right_pos[2], right_pos[3]))
                or (self.ball in self.canvas.find_overlapping(
                    left_pos[0], left_pos[1], left_pos[2], left_pos[3]))):
            self.x_vel = -self.x_vel
            self.y_vel += 1
            self.x_vel += 1


GUI()