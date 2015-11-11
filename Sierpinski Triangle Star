# Author: Pajama Programmer
# Date: 8-Nov-2015
# 
# Program: Sierpinski Triangle Star
# Discription: Fun program to play with the turtle module and recursive functions (functions that call themselves).
# This program creates a series of sierpinski triangles to build either a 5 or 6 pointed star
# More information about Sierpinski Triangles can be found here - https://en.wikipedia.org/wiki/Sierpinski_triangle, 
#

from __future__ import print_function, division

import turtle
#import math


"""
t - turtle
x - length to move in x direction
y - length to move in y direction
""" 
def goto(t, x, y):
    tot.pu()
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.rt(90)
    tot.pd()

"""
t - turtle
x - size
n - iterations
a - angle (should be 60)
"""   
def boogie(t,x,angle):
    t.fd(x)
    t.rt(angle)
    t.fd(x)
    t.rt(angle)
    t.fd(x)
   
def arrowhead_curve (t, n, x, a):
    m = x/2
    
    if (n <= 1):
        boogie(t, m, a)
        return

    tot.lt(-a)
    arrowhead_curve(t,n-1, m,-a)
    tot.lt(-a)
    arrowhead_curve(t,n-1, m,a)
    tot.lt(-a)
    arrowhead_curve(t,n-1, m,-a)
    tot.lt(-a)
    
def star_6 (t, n, x):
    for i in range(6):
        arrowhead_curve(t,n, x/3, 60)
        t.lt(60)

def star_5 (t, n, x):
    for i in range(5):
        arrowhead_curve(t,n, x/3, 60)
        t.lt(48)
    

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':

    tot = turtle.Turtle()
    n = 5
    x = 300
    a = 60
#    h = x*math.tan(60*math.pi/180)/2

    goto(tot, -x, x/3)
    
    tot.lt(a)
    star_5(tot, n, x)

    tot.rt(a)
    goto(tot, 2*x, 0)

    star_6(tot, n, x)

    turtle.mainloop()
