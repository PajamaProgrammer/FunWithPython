# Name: Pajama Programmer
# Date: 5-Nov-2015
# 
# I am a big fan of the Life of Fred Math series.
# In honor of my favorite math set, I am writing this fun little program.
# This program will use the turtle module to draw the cover logo of Life of Fred.
# 

from __future__ import print_function, division

import turtle
import math

"""
Level 1 Primitive Definitions
"""

def fwbk(t, n):
    """Forward and back, ending at the original position"""
    t.fd(n)
    t.bk(n)

def skip(t, n):
    """lift the pen and move"""
    t.pu()
    t.fd(n)
    t.pd()

def s_goto(t, x, y):
    """lift the pen and move"""
    t.pu()
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.rt(90)
    t.pd()
    
"""
Level 2 Primitive Definitions
"""

def post(t, n):
    """Vertical Line and back to original position"""
    t.lt(90)
    fwbk(t, n)
    t.rt(90)
    
def beam(t, n, height):
    """horizontal Line at given height, then back to original position"""
    t.lt(90)
    skip(t, height)
    t.rt(90)
    fwbk(t, n)
    t.rt(90)
    skip(t, height)
    t.lt(90)

def dia(t, x, y):
    """diagonal line to the x,y offsets and returns to original position"""
    angle = math.atan2(y,x)*180/math.pi
    hep = math.sqrt(x*x + y*y)
    t.lt(angle)
    fwbk(t, hep)
    t.rt(angle)

"""
Shape Functions
"""

def poly_line (t, n, size, angle):
    """draw a shape with n sides, each side with lentgh = size, and angle = degrees between sides"""
    for i in range(n):
        t.fd(size)
        t.lt(angle)
    

def arc(t, r, angle):
    #n = angle #You can do this, but I want to speed the program up
    arc_len = 2*math.pi*r*angle/360
    n = int(arc_len/5)+2
    step_len = arc_len/n
    step_angle = angle/n
    poly_line (t, n, step_len, step_angle)

def circle(t, r):
    arc_len = 2*math.pi*r
    n = int(arc_len/5)+2
    step_len = arc_len/n
    step_angle = 360/n
    poly_line(t, n, step_len, step_angle)
    
def square(t, size):
    poly_line(t, 4, size, 90)

def iso_trap(t, base, height, angle):
    """Draw an isosceles trapezoid (0 < angle < 180)"""
    t.fd(base)
    t.lt(180-angle)
    if (angle == 90):
        hep = top = height
    elif (angle < 90):
        hep = height/math.sin(angle*math.pi/180)
        top = base - 2*hep*math.cos(angle*math.pi/180)
    elif (angle > 90):
        hep = height/math.sin((180-angle)*math.pi/180)
        top = base + 2*hep*math.cos((180-angle)*math.pi/180)

    t.fd(hep)
    t.lt(angle)
    t.fd(top)
    t.lt(angle)
    t.fd(hep)
    t.lt(180-angle)
    
def flutes(t, n, size, angle):
    step_angle = int(angle/(4*n-1))
    angle1 = int(3*step_angle)
    angle2 = int(4.5*angle1)
    angle3 = int((360-angle2-angle1)/2)

##    print("inner angle", step_angle)
##    print("flute angle 1", angle1)
##    print("flute angle 2", angle2)
##    print("flute angle 3", angle3)
    
    for i in range(n):
        t.fd(size)
        t.lt(180-angle3)
        t.fd(size/4)
        t.lt(180-angle2)
        t.fd(size/4)
        t.lt(180-angle3)
        t.fd(size)
        t.lt(180)

        t.lt(step_angle)

"""
All letters start in lower left corner and end in lower right corner
Letters will be n x 2n in size
"""
def draw_l (t, size):
    skip(t, size/2)
    post(t, size*2)
    beam(t, size, 0)
    skip(t, size)

def draw_i (t, size):
    skip(t, size/2)
    beam(t, size, 2*size)
    beam(t, size, 0)
    skip(t, size/2)
    post(t, size*2)
    skip(t, size/2)

def draw_f (t, size):
    skip(t, size/2)
    post(t, 2*size)
    beam(t, size, 2*size)
    beam(t, size, size)
    skip(t, size)

def draw_e (t, size):
    skip(t, size/2)
    post(t, 2*size)
    beam(t, size, 2*size)
    beam(t, size, size)
    beam(t, size, 0)
    skip(t, size)

def draw_o (t, size):
    skip(t, size/2)
    skip(t,size)
    circle(t,size)
    skip(t,size)

def draw_r (t, size):
    skip(t, size/2)
    post(t, 2*size)
    t.lt(90)
    skip(t,size)
    t.rt(90)
    arc(t, size/2, 180)
    t.lt(90)
    skip(t,size)
    t.lt(90)
    dia(t, size/2, -size)
    skip(t,size/2)
    t.rt(90)
    skip(t,size)
    t.lt(90)

def draw_d (t, size):
    skip(t, size/2)
    post(t, size*2)
    arc(t, size, 180)
    t.lt(90)
    skip(t, 2*size)
    t.lt(90)
    skip(t, size)
    
"""
Functions - assume turtle is in lower left corner (faceing right) and will end in lower right corner (facing right)
"""
def LOF_Title(t, size):
    draw_l(fred, size)
    draw_i(fred, size)
    draw_f(fred, size)
    draw_e(fred, size)
    skip(fred, size)
    draw_o(fred, size)
    draw_f(fred, size)
    skip(fred, size)
    draw_f(fred, size)
    draw_r(fred, size)
    draw_e(fred, size)
    draw_d(fred, size)
    

def FredFace(t, size):
    fred.lt(120)
    
    arc(fred, size*2/3, 30)
    fred.rt(120)
    arc(fred, size/3, 30)
    fred.lt(120)
    fred.fd(size/5)
    fred.rt(90)
    arc(fred, size*2/3, 5)
    fred.rt(90)
    beam(fred, size*2/15, 0)
    fred.rt(180)
    fred.fd(size*8/15)
    fred.rt(160)
    fred.fd(size*2/3)
    fred.lt(70)
    skip(fred, size/15)
    fred.rt(90)
    skip(fred, size/15)
    circle(fred, 1)
    fred.rt(180)
    skip(fred, size*2/15)
    fred.rt(180)
    circle(fred, 1)
    fred.rt(180)
    skip(fred, size/6)
    fred.rt(5)
    post(fred, size*22/150)
    fred.rt(90)
    fred.fd(size/3)
    fred.rt(90)
    fred.fd(size*2/3)
    fred.rt(90)
    fred.fd(size)
    fred.lt(90)
    

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':

    fred = turtle.Turtle()

    s_goto(fred, 0, -100)
    
    FredFace(fred, 150)
    s_goto(fred, -200, -50)
    square(fred, 250)
    s_goto(fred, -100, 250)
    iso_trap(fred, 450, 100, 120)
    s_goto(fred, 150, 90)
    iso_trap(fred, 150, 150, 100)
    s_goto(fred, -15, 20)
    fred.lt(100)
    flutes(fred, 5, 110, 90)
    fred.lt(180)
    s_goto(fred, 192, 0)
    fred.lt(4)
    flutes(fred, 5, 110, 90)
    fred.rt(84)
    s_goto(fred, -275, -100)
    LOF_Title(fred, 20)
    s_goto(fred, 0, 275) #Move turtle out of way

    turtle.mainloop()
    
    
    
