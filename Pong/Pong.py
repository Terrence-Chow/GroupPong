from tkinter import *


class GUI:
    CANVAS_WIDTH = 800

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=f"{self.CANVAS_WIDTH}",
                             height="500",
                             background="black")
        self.canvas.pack()
        self.title = self.canvas.create_text(self.CANVAS_WIDTH/2, 50,
                                             text="PONG", fill="white")

        self.canvas.bind("<Button-1>", self.player_one_up)

        self.left = Paddle()
        self.window.mainloop()

    def player_one_up(self):
        self.left.MoveUp()

    def gain_point(self):
        pass



class Paddle:

    def __init__(self, y_vel):
        self.canvas = Canvas(width=10, height= 75, background="white")
        self.y = y_vel
    def move_up(self):


    def move_down(self):
        pass

    def stop(self):
        pass

    def get_position(self):
        pass

class Ball:
    def __init__(self):
        self.canvas = Canvas

    def appear_random(self):
        pass

    def move_ball(self):
        pass

    def hit_paddle(self):
        pass

    def hit_wall(self):
        pass


GUI()