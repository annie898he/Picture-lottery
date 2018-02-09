#################################################################################
# Author: Annie He
#hea-A7
#02/05/16
# Purpose: To very demonstrate the turtle library the use of functions 
# with conditionals and loops and A7
######################################################################
# Acknowledgements:
# Dr. Jan Pearce and Xhafer Rama
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle
import random

def cloud(wn, bk, x, y):
    '''Creates a cloud for scenery
    parameter wn is a screen object
    parameter bk is a turtle object
    parameter x are the x coordinates
    parameter y are the y coordinates'''
    counter=0
    for i in range(3):
        counter=counter+50      #this is to help move the circle along in a row
        bk.penup()
        bk.penup()
        bk.setpos((counter+x), y)   #this is to help move the circle along in a row to create a cloud
        bk.pendown()
        bk.color("white")
        bk.begin_fill()
        bk.fillcolor("white")        
        bk.circle(50)
        bk.end_fill()

def tree(wn, bk, x, y): #this code for the tree is altered from a previous assignment
    '''Creates trees and multiplies for a forest
    parameter wn is a screen object
    parameter bk is a turtle object
    parameter x are the x coordinates
    parameter y are the y coordinates'''
    counter=0
    for i in range(4):
        counter=counter+120 #this is to help move the trees along in a row
        bk.penup()
        bk.setpos((counter+x), y)   #this is to help move the trees along in a row
        bk.pendown()
        bk.color("black")
        bk.begin_fill()
        bk.fillcolor(random.choice(["darkgreen", "yellowgreen", "#228B22", "#008000" ]))   #randomly chooses a color choice for the leaves of the trees     
        bk.circle(70)
        bk.end_fill()
        bk.color("#401408") #hexidecimal color for the tree trunk
        bk.pensize(20)
        bk.right(90)
        bk.forward(120)
        bk.right(270)
        bk.pensize(1)
        bk.penup()
        bk.setpos(0,150)
        bk.pendown()
        bk.write("It is said that it is only in nature do you attain true serenity!",move=False,align='center',font=("Arial",13,("bold","normal")))
    

def sun(wn, nt, x, y):
    '''Creates a sun
    parameter wn is a screen object
    parameter nt is a turtle object
    parameter x are the x coordinates
    parameter y are the y coordinates'''
    nt.penup()
    nt.setpos(x,y)
    nt.pendown()    
    nt.begin_fill()
    nt.fillcolor("yellow")
    nt.circle(55)
    nt.end_fill()
    nt.hideturtle()

    
def main():
    ''' This program creates a forest or simple sky scenery using the turtle library'''
    wn = turtle.Screen()
    wn.bgcolor("skyblue")
    bk = turtle.Turtle()
    nt = turtle.Turtle()
    bk.hideturtle
    nt.hideturtle
    bk.speed(100)
    for i in range(1):
        color1=random.choice(['pink','grey','purple'])              #these are just to generate
        color2=random.choice(['yellow', 'green', 'red', "blue"])    #something random
        
        if (color1=='pink') or (color2=='yellow') or (color1=='grey'):  #this will only show if the randomly generated color is pink or yellow
            sun(wn, nt, 199, 170) 
            cloud(wn,bk, -199, 170)
            bk.penup()
            bk.setpos(0,0)
            bk.pendown()
            bk.color("black")
            bk.write("Enjoy the beauty of the simple sun and this single cloud.",move=False,align='center',font=("Arial",13,("bold","normal")))
            bk.hideturtle()

        else:   #this will show up if the randomly generated color is not pink or yellow
            sun(wn, nt, 199, 180)
            tree(wn, bk, -350, -32)
            tree(wn, bk, -270, -80)
            tree(wn, bk, -325,-120)
            bk.hideturtle()


    wn.exitonclick()    # wait for a user click on the canvas
    
    
main()