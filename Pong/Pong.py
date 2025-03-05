from tkinter import *
import random


class GUI:
    CANVAS_WIDTH = 1000
    CANVAS_HEIGHT = 600

    def __init__(self):
        """
        Initialize the GUI.
        """
        # Create the window
        self.window = Tk()
        self.canvas = Canvas(self.window, width=f"{self.CANVAS_WIDTH}",
                             height=self.CANVAS_HEIGHT,
                             background="black")
        self.canvas.pack()
        self.title = self.canvas.create_text(self.CANVAS_WIDTH / 2, 50,
                                             text="PONG", fill="white")
        self.right_number = 0
        self.left_number = 0
        self.right_score = self.canvas.create_text(
            (self.CANVAS_WIDTH / 2) + 100, 50,
            text=f"{self.right_number}", fill="white")
        self.left_score = self.canvas.create_text(
            (self.CANVAS_WIDTH / 2) - 100, 50,
            text=f"{self.left_number}", fill="white")

        # Create the objects for the game - paddles and ball
        self.left = Paddle(self.canvas, 25, self.window)
        self.right = Paddle(self.canvas, self.CANVAS_WIDTH - 25,
                            self.window)
        self.ball = Ball(self.canvas, 10, 50, self.window, 10, self)

        # Bind all the keys
        self.canvas.bind_all("<w>", lambda event: self.left.move_up())
        self.canvas.bind_all("<s>", lambda event: self.left.move_down())
        self.canvas.bind_all("<Up>", lambda event: self.right.move_up())
        self.canvas.bind_all("<Down>", lambda event: self.right.move_down())

        self.canvas.bind_all("<KeyRelease-Down>",
                             lambda event: self.right.stop_moving_down())
        self.canvas.bind_all("<KeyRelease-Up>",
                             lambda event: self.right.stop_moving_up())
        self.canvas.bind_all("<KeyRelease-s>",
                             lambda event: self.left.stop_moving_down())
        self.canvas.bind_all("<KeyRelease-w>",
                             lambda event: self.left.stop_moving_up())

        self.ball.move_random()
        # This line has to be at the end of this function
        self.window.mainloop()

    def right_gain_point(self):
        """Gains point after the right paddle misses the ball."""
        self.right_number += 1
        self.canvas.itemconfig(self.right_score, text=f'{self.right_number}',
                               fill='white')

    def left_gain_point(self):
        """Gains point after the left paddle misses the ball."""
        self.left_number += 1
        self.canvas.itemconfig(self.left_score, text=f'{self.left_number}',
                               fill='white')


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
        self.paddle = self.canvas.create_rectangle(self.x_start_paddle,
                                                   self.Y_START_PADDLE,
                                                   self.x_start_paddle + self.WIDTH_OF_PADDLE,
                                                   self.Y_START_PADDLE + self.HEIGHT_OF_PADDLE,
                                                   fill="white")

    def move_up(self):
        """Allow the paddle to move up."""
        # Check if paddle is at the top of the screen before moving
        if self.canvas.coords(self.paddle)[1] > 0:
            self.canvas.move(self.paddle, 0, -self.Y_VEL)
            # Function calls itself if key is still held down
            self.after_call_up = self.window.after(16, self.move_up)

    def move_down(self):
        """Allow the paddle to move down."""
        if self.canvas.coords(self.paddle)[3] < GUI.CANVAS_HEIGHT:
            self.canvas.move(self.paddle, 0, self.Y_VEL)
            self.after_call_down = self.window.after(16, self.move_down)

    def stop_moving_down(self):
        """Stops the paddle from moving down."""
        self.window.after_cancel(self.after_call_down)

    def stop_moving_up(self):
        """Stops the paddle from moving up."""
        self.window.after_cancel(self.after_call_up)

    def get_position(self):
        pass


class Ball:
    """Created the ball."""
    WIDTH_OF_BALL = 10
    HEIGHT_OF_BALL = 10
    Y_START_BALL = GUI.CANVAS_HEIGHT / 2.2

    def __init__(self, canvas, y_yel, x_coord, window, x_vel, GUI):
        """Created the window."""
        self.window = window
        self.canvas = canvas
        self.y_vel = y_yel
        self.x_vel = x_vel
        self.gui = GUI

        self.x_start_ball = x_coord
        self.ball = self.canvas.create_oval(self.x_start_ball,
                                            self.Y_START_BALL,
                                            self.x_start_ball + self.WIDTH_OF_BALL,
                                            self.Y_START_BALL + self.HEIGHT_OF_BALL,
                                            fill="white")

    def move_random(self):
        """Allow the ball to move randomly."""
        self.canvas.move(self.ball, self.x_vel, self.y_vel)
        if self.canvas.coords(self.ball)[0] < 0:
            self.canvas.move(self.ball, GUI.CANVAS_WIDTH / 2, 0)
            GUI.left_gain_point(self.gui)
        if self.canvas.coords(self.ball)[2] > GUI.CANVAS_WIDTH:
            self.canvas.move(self.ball, -GUI.CANVAS_WIDTH / 2, 0)
            GUI.right_gain_point(self.gui)
        if self.canvas.coords(self.ball)[3] > 600 or \
                self.canvas.coords(self.ball)[1] < 2:
            self.y_vel = -self.y_vel

        self.after_call_ball = self.window.after(16, self.move_random)

    def hit_paddle(self):
        """Hits the paddle, and bounces the ball."""
        pass


GUI()