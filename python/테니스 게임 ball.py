from tkinter import*
from random import*

class Ball:
    def __init__(self, court, x1,y1,x2,y2):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.x1_start = x1
        self.y2_start = y1 = 10
        self.x1_start = x1
        self.y2_start = y2

        self.x_dist = 10
        self.y_dist = 10

        self.width = x2 - x1
        self.height = y2 - y1

        self.court = court

        self.canvas = court.canvas

        self.ball = self.canvas.create_oval(x1, y1, x2, y2, fill = "yellow")

    def move_ball(self):

        self.x1 += self.x_dist
        self.y1 += self.y_dist

        if self.y1 <= 5:
            self.y1 = 5
            self.y_dist *= -1

        if self.y1 >= (self.court.height - (self.height - 5)):
            self.y1 = self.court.height - (self. height - 5)
            self.y_dist *= -1


            self.x1 = self.x1
            self.y1 = self.y1
            self.x2 = self.x2
            self.y2 = self.y2

            self.canvas.coords(self.ball, self.x1, self.y1, self.x2, self.y2)

        def stop_ball(self):
            self.x_dist = 0
            self.y_dist = 0

        def start_ball(self):

            if randint(0,1):
                self.x_dist = 10
            else:
                self.x_dist = -10
            if randint(0,1):
                self.y_dist = 10
            else:
                self.y_dist = -10

            self.x1 = slef.x1_start
            self.y1 = slef.y1_start
            self.x2 = slef.x2_start
            self.y2 = slef.y2_start

            self.canvas.coords(self.ball, self.x1, self. y1, self.x2, self.y2)
            


            
        
