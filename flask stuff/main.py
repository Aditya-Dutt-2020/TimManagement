import tkinter as tk
from PIL import Image,ImageTk
import time
import random
from random import randint
from win32api import GetMonitorInfo, MonitorFromPoint

monitor_info=GetMonitorInfo(MonitorFromPoint((0, 0)))
work_area=monitor_info.get('Work')
screen_width=work_area[2]
work_height=work_area[3]

idle = range(1,11)
heart = range(12,15)
walk = range(16,25)
log = range(26,28)
class Timmy:
    def __init__(self):
        self.window = tk.Tk()
        #self.idle=[tk.PhotoImage(file=f'Assets/dog/dog_sprite{str(x).zfill(2)}.png').resize for x in range(11)]
        #self.idle = [ImageTk.PhotoImage(Image.open(f'Assets/tim/tim_hearts/tim_hearts_fixed{str(x).zfill(1)}.png').resize((500,500))) for x in range(3)]
        self.idle = []
        for x in range(38):
            img = Image.open(f'Assets/tim/tim_long_idle/sprite_{str(x).zfill(2)}.png')
            self.idle.append(ImageTk.PhotoImage(Image.merge('RGBA', [b.resize((250,250), Image.LINEAR) for b in img.split()])))

        self.heart = []
        for x in range(1,4):
            img = Image.open(f'Assets/tim/tim_hearts/tim_hearts_fixed{str(x).zfill(1)}.png')
            self.heart.append(ImageTk.PhotoImage(Image.merge('RGBA', [b.resize((250,250), Image.LINEAR) for b in img.split()])))

        self.walk = []
        for x in range(0,2):
            img = Image.open(f'Assets/tim/tim_walking/sprite_{str(x).zfill(1)}.png')
            self.walk.append(ImageTk.PhotoImage(Image.merge('RGBA', [b.resize((250,250), Image.LINEAR) for b in img.split()])))
            
        self.walkBack = []
        for x in range(0,2):
            img = Image.open(f'Assets/tim/tim_walking/sprite_{str(x).zfill(1)}.png')
            self.walkBack.append(ImageTk.PhotoImage(Image.merge('RGBA', [b.resize((250,250), Image.LINEAR) for b in img.split()]).transpose(Image.FLIP_LEFT_RIGHT)))
        self.logWalk = []
        for x in range(1,3):
            img = Image.open(f'Assets/tim/tim_log/tim_log{str(x).zfill(1)}.png')
            self.logWalk.append(ImageTk.PhotoImage(Image.merge('RGBA', [b.resize((300,300), Image.LINEAR) for b in img.split()])))
        self.dam = []
        for x in range(0,10):
            img = Image.open(f'Assets/tim/tim_dam/sprite_{str(x).zfill(1)}.png')
            self.dam.append(ImageTk.PhotoImage(Image.merge('RGBA', [b.resize((200,200), Image.LINEAR) for b in img.split()])))
        self.xPos=int(screen_width*0.8)
        self.yPos=work_height-130
        self.doingSomething = False
        self.initFrame= 0
        self.state = 1
        self.eventNumber = 1

        self.frame = self.idle[0]

        self.window.config(highlightbackground='black')
        self.label = tk.Label(self.window,bd=0,bg='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor','black')
        self.label.pack()
        self.window.bind('<Button-1>', self.testing)
        self.window.after(1, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
        self.window.mainloop()

    def testing(self, event):
        self.initFrame = 0
        self.doingSomething = True
        self.eventNumber = 40

    def backlog(self, event):
        self.initFrame = 0
        self.doingSomething = True
        self.eventNumber = 17
        self.window.after(6000, self.transToLog)

    def pet(self,event):
        self.initFrame = 0
        self.doingSomething = True
        self.eventNumber = 12

    def transToLog(self):
        print("transed")
        self.initFrame = 0
        self.eventNumber = 26
        self.window.after(6000, self.freeze)
    
    def freeze(self):
        print("froze")
        self.initFrame = 0
        self.eventNumber = 30
        self.window.after(3000, self.logWalkBack)

    def logWalkBack(self):
        print("walking off")
        self.initFrame = 0
        self.eventNumber = 31
        self.window.after(6500, self.transToWalk)

    def transToWalk(self):
        print("walking on")
        self.initFrame = 0
        self.eventNumber = 32
        self.window.after(6000, self.backToIdle)

    def backToIdle(self):
        print("idle")
        self.doingSomething = False
        self.initFrame = 0
        self.eventNumber=1
        
    def event(self, initFrame, state, eventNumber, xPos):        
        if self.eventNumber in idle and not self.doingSomething:
            self.state = 1
            self.yPos = work_height-self.frame.height()
            self.window.after(700, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
        if self.eventNumber in heart:
            self.state = 2
            self.yPos = work_height-self.frame.height()
            self.window.after(300, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
        if self.eventNumber == 40:
            self.state = 7
            self.yPos = work_height-self.frame.height()
            self.window.after(1000, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
        if self.eventNumber in walk:
            self.state = 3
            self.yPos = work_height-self.frame.height()
            self.window.after(200, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
        if self.eventNumber in log:
            self.state = 4
            self.yPos = work_height-self.frame.height()
            self.window.after(200, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
        if self.eventNumber==30:
            print("event is 30")
            self.state = -10
            self.window.after(1, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
        if self.eventNumber == 31:
            print("event is 31")
            self.state = 5
            self.yPos = work_height-self.frame.height()
            self.window.after(200, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
        if self.eventNumber == 32:
            print("event is 32")
            self.state = 6
            self.yPos = work_height-self.frame.height()
            self.window.after(200, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
            
    def animate(self, initFrame, animation, eventNumber, x, y):
        print(f"animating with initFrame={self.initFrame}")
        if self.initFrame<len(animation)-1:
            self.initFrame+=1
        else:
            if not(eventNumber in idle):
                self.doingSomething = False
            self.initFrame = 0
            if self.eventNumber in [1,12, 40]:
                self.eventNumber=1
        if self.eventNumber==17 or self.eventNumber==31 and self.xPos <= screen_width:
            self.xPos+=10
        if self.eventNumber==26 or self.eventNumber==32 and self.xPos >= int(screen_width*0.8):
            self.xPos-=10
        return self.initFrame, self.eventNumber
    
    def updateFrame(self, initFrame, state, eventNumber, xPos):
        
        if state == 1 and not self.doingSomething:
            self.frame = self.idle[self.initFrame]
            self.initFrame, self.eventNumber=self.animate(self.initFrame, self.idle, self.eventNumber, 1, 1)
        if state == 2:
            self.frame = self.heart[self.initFrame]
            self.initFrame, self.eventNumber=self.animate(self.initFrame, self.heart, self.eventNumber, 1, 1)
        if state == 3:
            self.frame = self.walk[self.initFrame]
            self.initFrame, self.eventNumber=self.animate(self.initFrame, self.walk, self.eventNumber, 1,1)
        if state == 4:
            self.frame = self.logWalk[self.initFrame]
            self.initFrame, self.eventNumber = self.animate(self.initFrame, self.logWalk, self.eventNumber, 1,1)
        if state == 5:
            self.frame = self.logWalk[self.initFrame]
            self.initFrame, self.eventNumber = self.animate(self.initFrame, self.logWalk, self.eventNumber, 1,1)
        if state == 6:
            self.frame = self.walkBack[self.initFrame]
            self.initFrame, self.eventNumber = self.animate(self.initFrame, self.walkBack, self.eventNumber, 1, 1)
        if state == 7:
            self.frame = self.dam[self.initFrame]
            self.initFrame, self.eventNumber = self.animate(self.initFrame, self.dam, self.eventNumber, 1,1)
        self.window.geometry(f'{self.frame.width()}x{self.frame.height()}+'+str(self.xPos)+'+'+str(self.yPos))
        #self.window.geometry('72x64+'+str(self.xPos)+'+'+str(self.yPos))
        self.label.configure(image=self.frame)
        print("running event with eventnumber=", self.eventNumber)
        self.window.after(1, self.event, self.initFrame, self.state, self.eventNumber, self.xPos)

    
timmy = Timmy()