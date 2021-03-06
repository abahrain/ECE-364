#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-04-11 11:40:13 -0400 (Thu, 11 Apr 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab13/Pong.py $
#$Revision: 55576 $

import sys
import os
import random
from Tkinter import *

n=sys.argv[1:]
config={}
if len(sys.argv) != 2:
    print "Error: Pong.py <config>"
    sys.exit(1)
if not os.access(n[0],os.R_OK):
    print "%s is not readable" % (n[0],)
    sys.exit(1)
Configure=open(n[0], "r")
for line in Configure:
    line=line.split()
    config[line[0]]=int(line[1])
if len(config) != 8:
    print "Error: Configuration files has an incorrect number of inputs"
    sys.exit(1)

root = Tk()
root.title("Pong")

class Pong:
    def move(self):
        global x1, y1, dx, dy, playing, cwidth, cheight, ballsize, rfb, min, max
        global lplay, rplay, nextplayer, counter, rpos,lpos,rs, pa, pause
        if playing > 0:
            x1=x1+dx
            y1=y1+dy
        else:
            if nextplayer == 0:
                x1=rfb+10
                y1=lpos+(rs-ballsize)/2
                dx=config["dx"]
                dy=config["dy"]
            else:
                x1=cwidth-rfb-ballsize-10
                y1=rpos+(rs-ballsize)/2
                dx=-1*config["dx"]
                dy=-1*config["dy"]
        if y1>(cheight-ballsize):
            y1=cheight-ballsize
            dy=-dy
        if y1<0:
            y1=0
            dy=-dy
        if x1 > (cwidth-ballsize):
            lplay=lplay+1
            x1=rfb
            y1=(cheight/2)
            nextplayer=0
            playing=0
            pause=1
            w.itemconfigure(winner,text="Player 1 Wins!")
        if x1 < 0:
            rplay=rplay+1
            x1=cwidth-rfb
            y1=(cheight/2)
            nextplayer=1
            playing=0
            pause=1
            w.itemconfigure(winner, text="Player 2 Wins!")
        if x1 <= rfb:
            if y1>lpos and y1 < (lpos+rs):
                x1=rfb+5
                if dx > 0:
                    dx=random.randint(min,max)
                else:
                    dx=random.randint(min,max)
                    dx=-dx
                if dx > 0:
                    dy=random.randint(min,max)
                else:
                    dy=random.randint(min,max)
                    dy=-dy
                dx=-dx
        if x1 >= (cwidth-rfb-ballsize):
            if y1 >= rpos and y1 <= (rpos+rs):
                x1=(cwidth-rfb-ballsize-10)
                if dx > 0:
                    dx=random.randint(min,max)
                else:
                    dx=random.randint(min,max)
                    dx=-dx
                if dy > 0:
                    dy=random.randint(min,max)
                else:
                    dy=random.randint(min,max)
                    dy=-dy
                dx=-dx

        w.coords(oval1,x1,y1,x1+ballsize,y1+ballsize)
        score=str(lplay)+":"+str(rplay)
        w.itemconfigure(counter,text=score)
        w.itemconfigure(paused, text=pa)
        w.coords(rpaddle, cwidth-rfb, rpos, cwidth-rfb, rpos+rs)
        w.coords(lpaddle, rfb, lpos, rfb, lpos+rs)
        root.after(20,self.move)

    def lUp(self,event):
        global lpos, pspeed, pause
        if pause==0:
            if lpos > 1:
                lpos=lpos-pspeed

    def lDown(self,event):
        global lpos, cheight, pspeed, rs, pause
        if pause ==0:
            if lpos < (cheight-rs-1):
                lpos=lpos+pspeed

    def rUp(self,event):
        global rpos, pspeed, pause
        if pause ==0:
            if rpos > 1:
                rpos=rpos-pspeed

    def rDown(self,event):
        global rpos, cheight, pspeed, rs, pause
        if pause ==0:
            if rpos < (cheight-rs-1):
                rpos=rpos+pspeed

    def launchBall(self,event):
        global playing, pause
        if pause ==0:
            playing=1

    def focus(self,event):
        w.focus_force()

    def quit(self,event):
        root.destroy()

    def restart(self,event):
        global pause
        pause=0
        w.itemconfigure(winner,text="")

    def info(self,event):
        global pause, dx, dy, dx2, dy2, pa
        if pause == 1:
            pause=0
            pa=""
            dx=dx2
            dy=dy2
        elif pause == 0:
            pause=1
            pa="Paused"
            dx2=dx
            dy2=dy
            dx=0
            dy=0
    def quiet(self):
        root.destroy()
    def resturt(self):
        global pause
        pause=0
        w.configure(winner,text="")
    def paused(self):
        global pause, dx, dy, dx2, dy2, pa, pspeed
        if pause == 1:
            pause=0
            pa=""
            dx=dx2
            dy=dy2
        elif pause == 0:
            pause=1
            pa="Paused"
            dx2=dx
            dy2=dy
            dx=0
            dy=0

lplay=0 #left player score
rplay=0 #right player score
rfb=20 # space between wall and paddle
rs=60 #paddle size
cwidth = config["cwidth"] #court width
cheight = config["cheight"] #court height
ballsize= config["ballsize"] #ballsize
pspeed=config["pspeed"] #paddle speed
x1=rfb                   
y1=(cheight-ballsize)/2  
dx=config["dx"] # these control the
dy=config["dy"] # ball speed in each direction
dx2=0 #poause hold variable
dy2=0 #pause hold variable
rpos=(cheight-rs)/2 #right player position
lpos=(cheight-rs)/2 #left player position
nextplayer=0 # used to determine who gets the ball 0=right and 1=left
playing=0 #determine whether we are playing or not 0=NO 1=YES
pause=0 #pause indicater
pa="" #pause phrase
min=config["minbs"] #min ball speed
max=config["maxbs"] #max ball speed 

pongGame=Pong()
w= Canvas(root,bg="white", width=cwidth, height=cheight)
w.pack(side=LEFT)
oval1=w.create_oval(x1,y1,x1+ballsize,y1+ballsize,width=2,fill="red") #generate ball
line = w.create_line(cwidth/2, 0, cwidth/2, cheight, width=4, fill="black", dash=(4,8)) #generate center line
lpaddle = w.create_line(rfb, lpos, rfb, lpos+rs, width=10, fill="black") #generate left paddle 
rpaddle = w.create_line(cwidth-rfb, rpos, cwidth-rfb, rpos+rs, width=10, fill="black") #generate right paddle
font=('courier',20)
counter=w.create_text(cwidth/2,20,text='0:0',font=font,fill="black")
paused=w.create_text(cwidth/2,40,text='',font=font,fill="black")
winner=w.create_text(cwidth/2,cheight/2,text="",font=font,fill="red")


w.bind("<Enter>", pongGame.focus) #bring focus to GUI window
w.bind("w", pongGame.lUp) #Left paddle up
w.bind("s", pongGame.lDown) #Left paddle down
w.bind("<Up>", pongGame.rUp) #Right paddle up
w.bind("<Down>", pongGame.rDown) #Right paddle down
w.bind("<Return>", pongGame.restart) #Restart
w.bind("q",pongGame.quit) #Exit game
w.bind("<space>", pongGame.launchBall) #Launch Ball
w.bind("p", pongGame.info) #Pause

p = Button(root, text="Pause",command= pongGame.paused)
s = Button(root, text="Restart", command= pongGame.resturt)
q = Button(root, text="Exit", command= pongGame.quiet)
p.pack(fill=BOTH, expand=1)
s.pack(fill=BOTH, expand=1)
q.pack(fill=BOTH, expand=1)

root.after(20,pongGame.move)
root.mainloop()

sys.exit(0)
