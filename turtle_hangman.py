'''
Created on 6 Apr 2016

@author: aml
'''

import turtle

class TurtleHangman:
    
    def __init__(self):
        # Initialise turtle window and it's properties
        self.window = turtle.Screen()
        self.window.bgcolor("red")

        # Initialise drawing turtle
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("yellow")
        self.turtle.speed(4)
        
    def draw_hang(self):
        self.turtle.left(90)
        self.turtle.forward(200)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(15)
        self.turtle.color('red')
        self.turtle.forward(60)
        self.turtle.color('yellow')
        self.turtle.left(90)
        
    def draw_head(self):
        self.turtle.circle(30)
        
    def draw_body(self):
        self.turtle.right(90)
        self.turtle.forward(70)
        
    def draw_r_hand(self):
        self.turtle.left(180)
        self.turtle.forward(70)
        self.turtle.left(135)
        self.turtle.forward(40)
        
    def draw_l_hand(self):
        self.turtle.left(180)
        self.turtle.forward(40)
        self.turtle.right(90)
        self.turtle.forward(40)
        
    def draw_l_leg(self):
        self.turtle.left(180)
        self.turtle.forward(40)
        self.turtle.left(135)
        self.turtle.forward(70)
        self.turtle.left(45)
        self.turtle.forward(50)
        
        
    def draw_r_leg(self):
        self.turtle.left(180)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        
    def draw_eyes(self):
        self.turtle.left(180)
        self.turtle.forward(50)
        self.turtle.left(45)
        self.turtle.forward(70)
        self.turtle.color('red')
        self.turtle.forward(40)
        self.turtle.right(90)
        self.turtle.forward(20)
        self.turtle.left(180)
        self.turtle.color('yellow')
        self.turtle.forward(15)
        self.turtle.color('red')
        self.turtle.forward(10)
        self.turtle.color('yellow')
        self.turtle.forward(15)
        
    def draw_nose(self):
        self.turtle.left(90)
        self.turtle.color('red')
        self.turtle.forward(5)
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.color('yellow')
        self.turtle.forward(15)
    
    def draw_mouth(self):
        self.turtle.color('red')
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(10)
        self.turtle.color('yellow')
        self.turtle.left(90)
        self.turtle.circle(10, 180)
        self.turtle.hideturtle()
        
    def ready_to_exit(self):
        self.window.exitonclick()
        
th = TurtleHangman()
th.draw_hang()
th.draw_head()
th.draw_body()
th.draw_r_hand()
th.draw_l_hand()
th.draw_l_leg()
th.draw_r_leg()
th.draw_eyes()
th.draw_nose()
th.draw_mouth()
th.ready_to_exit()