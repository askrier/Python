"""
kochCurve.py
Andrew Krier
10/14/18

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: ak513
"""

#%% Imports
import turtle

#%% Define Functions
def koch_curve(t, length, lvl=0):
    if lvl==0:
        t.forward(length)
    else:
        koch_curve(t, length / 3, lvl - 1)
        t.left(60)
        koch_curve(t, length / 3, lvl - 1)
        t.right(120)
        koch_curve(t, length / 3, lvl - 1)
        t.left(60)
        koch_curve(t, length / 3, lvl - 1)
        
def init_turtle(t):
    t.pensize(2)
    t.speed(0)
    t.color('white')

#%% Main code if script is run
if __name__ == '__main__':
    wn = turtle.Screen()
    wn.clearscreen()
    wn.bgcolor('black')
    try:
        kasa = turtle.Turtle()
    except:
        kasa = turtle.Turtle()
        
    init_turtle(kasa)
    kasa.penup()
    kasa.setposition(-300, 0)
    kasa.pendown()
    koch_curve(kasa, 600, 4)