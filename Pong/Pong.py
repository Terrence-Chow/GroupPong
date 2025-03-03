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

        self.left = Paddle(20, self.canvas)

        self.canvas.bind_all("<w>", lambda event:self.player_one_up())


        self.window.mainloop()


    def player_one_up(self):
        self.left.move_up()



class Paddle:

    def __init__(self, y_vel, canvas):
        self.canvas = canvas
        self.y = y_vel
    def move_up(self):
        self.canvas.create_rectangle(10, 10, 10 + 100, 10 + 100,
                                     fill=f"#{random.randint(0, 0xFFFFFF):06x}")

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