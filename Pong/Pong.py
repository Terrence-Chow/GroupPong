from tkinter import *
import random


class GUI:
    CANVAS_WIDTH = 1000
    CANVAS_HEIGHT = 600

    def __init__(self):
        """
        Initialize the GUI.
        """
        self.window = Tk()
        self.canvas = Canvas(self.window, width=f"{self.CANVAS_WIDTH}",
                             height=self.CANVAS_HEIGHT,
                             background="black")
        self.canvas.pack()
        self.title = self.canvas.create_text(self.CANVAS_WIDTH / 2, 50,
                                             text="PONG", fill="white")

        self.left = Paddle(20, self.canvas, 25, self.window)
        self.right = Paddle(20, self.canvas, self.CANVAS_WIDTH - 25,
                            self.window)

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

        #self.ball = Ball(self.canvas, 10, 50, 10)

        self.window.mainloop()

    def player_one_up(self):
        self.left.move_up()
        pass

    def gain_point(self):
        pass


class Paddle:
    WIDTH_OF_PADDLE = 10
    HEIGHT_OF_PADDLE = 100
    Y_START_PADDLE = GUI.CANVAS_HEIGHT / 2.5

    def __init__(self, y_vel, canvas, x_coord, window):
        self.canvas = canvas
        self.window = window
        self.y_vel = y_vel
        self.x_start_paddle = x_coord
        self.paddle = self.canvas.create_rectangle(self.x_start_paddle,
                                                   self.Y_START_PADDLE,
                                                   self.x_start_paddle + self.WIDTH_OF_PADDLE,
                                                   self.Y_START_PADDLE + self.HEIGHT_OF_PADDLE,
                                                   fill="white")

    def move_up(self):
        if self.canvas.coords(self.paddle)[1] > 0:
            self.canvas.move(self.paddle, 0, -self.y_vel)
        self.after_call_up = self.window.after(16, self.move_up)

    def move_down(self):
        if self.canvas.coords(self.paddle)[3] < GUI.CANVAS_HEIGHT:
            self.canvas.move(self.paddle, 0, self.y_vel)
        self.after_call_down = self.window.after(16, self.move_up)

    def stop_moving_down(self):
        self.window.after_cancel(self.after_call_down)

    def stop_moving_up(self):
        self.window.after_cancel(self.after_call_up)

    def get_position(self):
        pass

    class Ball:
        WIDTH_OF_BALL = 10
        HEIGHT_OF_BALL = 10
        Y_START_BALL = GUI.CANVAS_HEIGHT / 2.2

        def __init__(self, canvas, y_yel, x_coord):
            self.canvas = canvas
            self.y = y_yel
            self.x_start_ball = x_coord
            self.canvas.create_oval(self.x_start_ball, self.Y_START_BALL,
                                    self.x_start_ball + self.WIDTH_OF_BALL,
                                    self.Y_START_BALL + self.HEIGHT_OF_BALL,
                                    fill="white")

    def move_random(self):
        pass

    def hit_paddle(self):
        pass

    def hit_wall(self):
        pass


GUI()