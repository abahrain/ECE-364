#! /usr/bin/env python2.6
#
#$Author:
#$Date:
#$HeadURL:
#$Revision:

import sys
import os
import random
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
import shutil

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
if len(config) != 11:
    print "Error: Configuration files has an incorrect number of inputs"
    sys.exit(1)
Configure.close()
f=open("SaveData.txt", 'w+')

root = Tk()
root.title("Pong")

class Pong:
    def move(self):
        global x1, y1, dx, dy, playing, cwidth, cheight, ballsize, rfb, min, max, game, type, holdtime
        global lplay, rplay, nextplayer, counter, rpos,lpos,rs, pa, pause, record, win, playtime
        if record == 1:
            line=self.file.readline()
            file=line.split()
            if len(file) == 7:
                lpos=int(file[0])
                rpos=int(file[1])
                x1=int(file[2])
                y1=int(file[3])
                lplay=int(file[4])
                rplay=int(file[5])
                game=int(file[6])
            else:
                p=self.end()
        if playing > 0 and record != 1:
            x1=x1+dx
            y1=y1+dy
        elif record!=1:
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
        if y1>(cheight-ballsize) and record!=1:
            y1=cheight-ballsize
            dy=-dy
        if y1<0 and record!=1:
            y1=0
            dy=-dy
        if x1 > (cwidth-ballsize) and record!=1:
            lplay=lplay+1
            x1=rfb
            y1=(cheight/2)
            nextplayer=0
            playing=0
        if x1 < 0 and record!=1:
            rplay=rplay+1
            x1=cwidth-rfb
            y1=(cheight/2)
            nextplayer=1
            playing=0
        if x1 <= rfb and record!=1:
            if y1>lpos and y1 < (lpos+rs):
                x1=rfb+5
                print "\007"
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
        if x1 >= (cwidth-rfb-ballsize) and record!=1:
            if y1 >= rpos and y1 <= (rpos+rs):
                x1=(cwidth-rfb-ballsize-10)
                print "\007"
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

	if game==0:
            w.itemconfigure(mode,text="Unlimited")
            w.itemconfigure(ltime, text="")
            w.itemconfigure(rtime, text="")
            playtime=config["playing"]*50
	if game==1:
            w.itemconfigure(mode,text="Timed")
            if (playtime/50)/60 >=1:
                if (playtime/50)%60 >= 10:
                    time=str((playtime/50)/60)+":"+str((playtime/50)%60)
                else:
                    time=str((playtime/50)/60)+":0"+str((playtime/50)%60)
                w.itemconfigure(ltime, text=time, fill="black")
                w.itemconfigure(rtime, text=time, fill="black")
            elif (playtime/50)/60 < 1 and (playtime/50)>10:
                time=str(playtime/50)
                w.itemconfigure(ltime, text=time, fill="black")
                w.itemconfigure(rtime, text=time, fill="black")
            else:
                time=str(playtime/50)
                w.itemconfigure(ltime, text=time, fill="red")
                w.itemconfigure(rtime, text=time, fill="red")
            if playtime == 0:
                if lplay>rplay:
                    w.itemconfigure(winner,text="Player 1 Wins!")
                    playtime=config["playing"]*50
                    p=self.end()
                if rplay>lplay:
                    w.itemconfigure(winner,text="Player 2 Wins!")
                    playtime=config["playing"]*50
                    p=self.end()
                if rplay==lplay:
                    w.itemconfigure(winner, text="Tied")
                    playtime=config["playing"]*50
                    p=self.end()
            elif pause == 0:
                playtime=playtime-1
	if game==2:
            w.itemconfigure(mode,text="Scored")
            w.itemconfigure(ltime, text="")
            w.itemconfigure(rtime, text="")
            playtime=config["playing"]*50
            if lplay>=win:
                w.itemconfigure(winner,text="Player 1 Wins!")
		p=self.end()
	    if rplay>=win:
		w.itemconfigure(winner,text="Player 2 Wins!")
		p=self.end()
        if game==3:
            w.itemconfigure(mode, text="Demonstation")
            if holdtime == 0:
                playing=1
                holdtime=config["holding"]*50
            else:
                holdtime=holdtime-1
            if (playtime/50)/60 >=1:
                if (playtime/50)%60 >= 10:
                    time=str((playtime/50)/60)+":"+str((playtime/50)%60)
                else:
                    time=str((playtime/50)/60)+":0"+str((playtime/50)%60)
                w.itemconfigure(ltime, text=time, fill="black")
                w.itemconfigure(rtime, text=time, fill="black")
            elif (playtime/50)/60 < 1 and (playtime/50)>10:
                time=str(playtime/50)
                w.itemconfigure(ltime, text=time, fill="black")
                w.itemconfigure(rtime, text=time, fill="black")
            else:
                time=str(playtime/50)
                w.itemconfigure(ltime, text=time, fill="red")
                w.itemconfigure(rtime, text=time, fill="red")
            if playtime == 0:
                if lplay>rplay:
                    w.itemconfigure(winner,text="Player 1 Wins!")
                    playtime=config["playing"]*50
                    p=self.end()
                if rplay>lplay:
                    w.itemconfigure(winner,text="Player 2 Wins!")
                    playtime=config["playing"]*50
                    p=self.end()
                if rplay==lplay:
                    w.itemconfigure(winner, text="Tied")
                    playtime=config["playing"]*50
                    p=self.end()
            elif pause == 0:
                playtime=playtime-1
                lpos=y1 - (rs/2)
                rpos=y1 - (rs/2)
        
        if player==1 and record!=1:
            if holdtime == 0:
                playing=1
                holdtime=config["holding"]*50
            elif nextplayer == 0:
                holdtime=holdtime-1
            if type==1:
                if lpos > y1-(rs/2):
                    lpos=lpos-pspeed
                elif lpos < y1-(rs/2):
                    lpos=lpos+pspeed
            if type==2:
                if lpos > y1-(rs/2):
                    lpos=lpos-pspeed+random.randint(min,max)
                elif lpos < y1-(rs/2):
                    lpos=lpos+pspeed+random.randint(min,max)

        w.coords(oval1,x1,y1,x1+ballsize,y1+ballsize)
        score=str(lplay)+":"+str(rplay)
        w.itemconfigure(counter,text=score)
        w.itemconfigure(paused, text=pa)
        w.coords(rpaddle, cwidth-rfb, rpos, cwidth-rfb, rpos+rs)
        w.coords(lpaddle, rfb, lpos, rfb, lpos+rs)
        if save != 1:
            f.write("%d %d %d %d %d %d %d\n" % (lpos, rpos, x1, y1, lplay, rplay, game))
        root.after(20,self.move)

    def lUp(self,event):
        global lpos, pspeed, pause, player
        if pause==0 and player==0:
            if lpos > 1:
                lpos=lpos-pspeed

    def lDown(self,event):
        global lpos, cheight, pspeed, rs, pause, player
        if pause ==0 and player==0:
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
        global playing, pauses
        if pause ==0:
            playing=1

    def focus(self,event):
        w.focus_force()

    def quit(self,event):
        root.destroy()

    def restart(self,event):
        global pause, lplay, rplay, pa, playing, nextplayer, player, playtime
        pause=0
        lplay=0
        rplay=0
        pa=""
        nextplayer=0
        player=0
        playing=0
        playtime=config["playing"]*50
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
        global pause, lplay, rplay, pa, playing, nextplayer, player, playtime
        pause=0
        lplay=0
        rplay=0
        pa=""
        nextplayer=0
        player=0
        playing=0
        playtime=config["playing"]*50
        w.itemconfigure(winner,text="")
    def paused(self):
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
    def display(self):
        global record
        file=tkFileDialog.askopenfilename()
        self.file=open(file,'r')
        record=1
    def record(self):
        global save
        save=1
        f.close()
        file=tkFileDialog.asksaveasfilename()
        shutil.copy2('SaveData.txt', file)
    def end(self):
        global pause, dx, dy, pa, record
        pause=1
        pa="Game Over"
        record=0
        dx=0
        dy=0
    def aie(self):
        global player, pause, type
        self.resturt()
        if pause==0:
            player=1
            type=2
    def aih(self):
        global player, pause, type
        self.resturt()
        if pause==0:
            player=1
            type=1
    def mode0(self):
        global game
        self.resturt()
        game = 0
    def mode1(self):
        global game
	self.resturt()
        game = 1
    def mode2(self):
        global game
        self.resturt()
	game = 2
    def mode3(self):
        global game
        self.resturt()
	game = 3
    def twice(self):
        global player
        self.resturt()
        player=0
    


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
lpos=(cheight-rs)/2 #left player position('courier',20)
nextplayer=0 # used to determine who gets the ball 0=right and 1=left
playing=0 #determine whether we are playing or not 0=NO 1=YES
pause=0 #pause indicater
pa="" #pause phrase
min=config["minbs"] #min ball speed
max=config["maxbs"] #max ball speed 
win=config["winning"]
holdtime=config["holding"]
playtime=config["playing"]*50
game=0
ai=0
record=2
save=0
type=0
player=0
fields = 'Ball Speed', 'Paddle Speed', 'Play time', 'Max Score'

pongGame=Pong()
w=Canvas(root,bg="white", width=cwidth, height=cheight)
w.pack(side=LEFT)
oval1=w.create_oval(x1,y1,x1+ballsize,y1+ballsize,width=2,fill="red") #generate ball
line = w.create_line(cwidth/2, 45, cwidth/2, cheight, width=4, fill="black", dash=(4,8)) #generate center line
lpaddle = w.create_line(rfb, lpos, rfb, lpos+rs, width=10, fill="black") #generate left paddle 
rpaddle = w.create_line(cwidth-rfb, rpos, cwidth-rfb, rpos+rs, width=10, fill="black") #generate right paddle
counter=w.create_text(cwidth/2,30,text='0:0',font=('courier',20),fill="black")
paused=w.create_text(cwidth/2,50,text='',font=('courier',40),fill="black")
winner=w.create_text(cwidth/2,cheight/2,text="",font=('courier',40,'bold'),fill="red")
mode=w.create_text(cwidth/2,10,text="",font=('courier',15),fill="black")
ltime=w.create_text(20,20,text="",font=('courier',15),fill="black")
rtime=w.create_text(cwidth-20,20,text="",font=('courier',15),fill="black")
w.bind("<Enter>", pongGame.focus) #bring focus to GUI window
w.bind("w", pongGame.lUp) #Left paddle up
w.bind("s", pongGame.lDown) #Left paddle down
w.bind("<Up>", pongGame.rUp) #Right paddle up
w.bind("<Down>", pongGame.rDown) #Right paddle down
w.bind("<Return>", pongGame.restart) #Restart
w.bind("q",pongGame.quit) #Exit game
w.bind("<space>", pongGame.launchBall) #Launch Ball
w.bind("p", pongGame.info) #Pause
w.bind("<Escape>", pongGame.quit)

p = Button(root, text="Pause",command= pongGame.paused).pack(fill=BOTH, expand=1)
s = Button(root, text="Restart", command= pongGame.resturt).pack(fill=BOTH, expand=1)
q = Button(root, text="Exit", command= pongGame.quiet).pack(fill=BOTH, expand=1)

u = Button(root, text="Unlimited Play", command= pongGame.mode0).pack(fill=BOTH, expand=1)
t = Button(root, text="Timed play", command= pongGame.mode1).pack(fill=BOTH, expand=1)
c = Button(root, text="Scored play", command= pongGame.mode2).pack(fill=BOTH, expand=1)

b = Button(root, text="Two Player", command= pongGame.twice).pack(fill=BOTH, expand=1)
e = Button(root, text="Easy AI", command= pongGame.aie).pack(fill=BOTH, expand=1)
h = Button(root, text="Hard AI", command= pongGame.aih).pack(fill=BOTH, expand=1)

l=Button(root, text="Load Recording", command= pongGame.display).pack(fill=BOTH, expand=1)
s=Button(root, text="Save Recording", command= pongGame.record).pack(fill=BOTH, expand=1)

d = Button(root, text="Demo", command= pongGame.mode3).pack(fill=BOTH, expand=1)

root.after(20,pongGame.move)
root.mainloop()
f.close()

sys.exit(0)
