from tkinter import *
import random


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

        self.canvas.bind("<w>", self.player_one_up)

        # self.left = Paddle()

        self.window.mainloop()


    def player_one_up(self):
        self.canvas.create_rectangle(10, 10, 10 + 100, 10 + 100, fill=f""
                                                             f"#{random.randint(0, 0xFFFFFF):06x}")
        # self.left.MoveUp()



class Paddle:

    def __init__(self, y_vel):
        self.canvas = Canvas(width=10, height= 75, background="white")
        self.y = y_vel
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