import matplotlib.pyplot as plt
import openpyxl as xlsx
from turtle import *
import math
import tkinter as tk
import time

scale = 5
height = 3

x = []
y = []
c = []

d = []

ux = 0
uy = 0
uc = ''

w1 = []
w2 = []
w3 = []

i1 = []
i2 = []
i3 = []
w_color =''
book = xlsx.open("table.xlsx", read_only=True)
def read_xlsx():
    for row in book.active.values:
        if isinstance(row[0], str):
            plt.xlabel(row[0])
            plt.ylabel(row[1])
            continue
        elif row[2] == 'Perviy':
            x.append(row[0])
            y.append(row[1])
            c.append(row[2])
        elif row[2] == 'Vtoroy':
            x.append(row[0])
            y.append(row[1])
            c.append(row[2])
        elif row[2] == 'Tretiy':
            x.append(row[0])
            y.append(row[1])
            c.append(row[2])
        elif row[2] == 'Unknown':
            global ux,uy,uc
            ux = row[0]
            uy = row[1]
            uc = row[2]
def draw_plot(scale):
    speed(0)
    penup()
    goto(-350,300)
    write('Window height is: ' + height.__str__())
    goto(-350,280)
    write('Scale is: ' + scale.__str__())
    penup()
    goto(0,0)
    pendown()
    color('black')
    forward(200 * scale)
    back(200 * scale)
    left(90)
    forward(200 * scale)
    penup()
    for i in range(20):
        i += 1
        goto(10 * i * scale,-10 * scale)
        write(i, font=('Arial', 5 * scale, 'normal'))
        goto(10 * i * scale,0)
        pendown()
        goto(10 * i * scale,200 * scale)
        penup()
        goto(-10 * scale,10 * i * scale)
        write(i, font=('Arial', 5 * scale, 'normal'))
        goto(0,10 * i * scale)
        pendown()
        goto(200 * scale, i * 10 * scale)
        penup()
def draw_objects(scale):
    p_color = ''
    p_size = ''
    for i in range(x.__len__()):
        penup()
        d.append(distance(ux ,x[i] ,uy ,y[i] ))
        print(i, d[i])
        if c[i] == "Perviy":
            p_color = 'red'
            p_size = 10
        if c[i] == "Vtoroy":
            p_color = 'blue'
            p_size = 7
        if c[i] == "Tretiy":
            p_color = 'green'
            p_size = 5
        goto(x[i] * 10 * scale,y[i] * 10 * scale)
        dot(p_size * scale,p_color)
    goto(ux * 10 * scale,uy * 10 * scale)
    dot(3 * scale,parzen_method())
    goto((ux + (1.5/10)) * 10 * scale,uy * 10 * scale)
    pendown()
    color('yellow')
    circle(1.5  * scale)
    pensize(2)
    color('purple')
    penup()
    goto((ux + height) * 10 * scale ,uy * 10 * scale)
    pendown()
    circle(height * scale *10)
def distance(x1,x2,y1,y2):
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
def draw_net(win, collor):
    for i in win:
        penup()
        color(collor)
        goto(ux* 10 * scale,uy* 10 * scale)
        pendown()
        goto(x[i]* 10 * scale,y[i]* 10 * scale)
        penup()
    goto(ux * 10 * scale,uy * 10 * scale)
def win_condition(w1,w2,c1,c2):
    a_w1 = 0
    a_w2 = 0
    for i in range(w1.__len__()):
        a_w1 += w1[i]
        a_w2 += w2[i]
    a_w1 /= w1.__len__()
    a_w2 /= w1.__len__()
    print("w12:",a_w1,a_w2)
    w_number = min([a_w1, a_w2])
    if w_number == a_w1:
        draw_net(i1,c1)
        return c1
    if w_number == a_w2:
        draw_net(i2,c2)
        return c2
def draw_nearest_heighbor(i,c):
    pendown()
    color(c)
    goto(x[i]*10*scale,y[i]*10*scale)
    penup()
    goto(ux*10*scale,uy*10*scale)
def parzen_method():
    w1.clear()
    w2.clear()
    w3.clear()
    i1.clear()
    i2.clear()
    i3.clear()
    for i in range(x.__len__()):
        if d[i] <= height:
            if c[i] == "Perviy":
                w1.append(d[i])
                i1.append(i)
            if c[i] == "Vtoroy":
                w2.append(d[i])
                i2.append(i)
            if c[i] == "Tretiy":
                w3.append(d[i])
                i3.append(i)
    print(w1.__len__(), w2.__len__(), w3.__len__())
    if w1.__len__() == w2.__len__() == w3.__len__():
        if w1.__len__() > 0:
            a_w1 = 0
            a_w2 = 0
            a_w3 = 0
            for i in range(w1.__len__()):
                a_w1 += w1[i]
                a_w2 += w2[i]
                a_w3 += w3[i]
            a_w1 /= w1.__len__()
            a_w2 /= w1.__len__()
            a_w3 /= w1.__len__()
            w_number = min([a_w1, a_w2, a_w3])
            if w_number == a_w1:
                return 'red'
            if w_number == a_w2:
                return 'blue'
            if w_number == a_w3:
                return 'green'
    if w1.__len__() == w2.__len__():
        if w1. __len__() > w3.__len__():
            return win_condition(w1,w2,'red','blue')
    if w3.__len__() == w2.__len__():
        if w3.__len__() > w1.__len__():
            return win_condition(w3,w2,'green','blue')
    if w1.__len__() == w3.__len__():
        if w1.__len__() > w2.__len__():
            return win_condition(w2,w3,'blue','green')
    w_number = max([w1.__len__(),w2.__len__(),w3.__len__()])
    if w_number == 0:
        for i in range(d.__len__()):
            if d[i] == min(d):
                if c[i] == "Perviy":
                    draw_nearest_heighbor(i,'red')
                    return "red"
                if c[i] == "Vtoroy":
                    draw_nearest_heighbor(i, 'blue')
                    return 'blue'
                if c[i] == "Tretiy":
                    draw_nearest_heighbor(i, 'green')
                    return "green"
    if w_number == w1.__len__():
        draw_net(i1,'red')
        return 'red'
    if w_number == w2.__len__():
        draw_net(i2,'blue')
        return 'blue'
    if w_number == w3.__len__():
        draw_net(i3,'green')
        return 'green'
    return 'black'
def fup():
   global height
   height += .1
   reset()
   draw_plot(scale)
   draw_objects(scale)
def fdown():
    global height
    height -= .1
    reset()
    draw_plot(scale)
    draw_objects(scale)
def f_right():
    global scale
    scale += 1
    reset()
    draw_plot(scale)
    draw_objects(scale)
def f_left():
    global scale
    if scale > 1:
        scale -= 1
        reset()
        draw_plot(scale)
        draw_objects(scale)


if __name__ == '__main__':
    read_xlsx()
    screen = Screen()
    screen
    draw_plot(scale)
    draw_objects(scale)
    screen.onkey(fup, "Up")
    screen.onkey(fdown, "Down")
    screen.onkey(f_left, "Left")
    screen.onkey(f_right, "Right")
    screen.listen()
    screen.mainloop()



