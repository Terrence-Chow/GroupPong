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
        self.window.mainloop()

        self.canvas.bind("<Button-1>", self.player_1_up)

        self.left = Paddle()

    def player_one_up(self):
        self.left.MoveUp()

k


class Paddle:

    def move_up(self):
        pass

    def move_down(self):
        pass

    def stop(self):
        pass

    def get_position(self):
        pass

class Ball:
    pass


GUI()