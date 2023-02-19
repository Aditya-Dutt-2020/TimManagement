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

class Timmy:
    def __init__(self):
        self.window = tk.Tk()
        #self.idle=[tk.PhotoImage(file=f'Assets/dog/dog_sprite{str(x).zfill(2)}.png').resize for x in range(11)]
        self.idle = [ImageTk.PhotoImage(Image.open(f'Assets/dog/dog_sprite{str(x).zfill(2)}.png').resize((100,100), Image.ANTIALIAS)) for x in range(11)]
        self.xPos=int(screen_width*0.8)
        self.yPos=work_height-70

        self.initFrame= 0
        self.state = 1
        self.eventNumber = 1

        self.frame = idle[0]
        self.window.config(highlightbackground='black')
        self.label = tk.Label(self.window,bd=0,bg='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor','black')
        self.label.pack()
        
        self.window.after(1, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
        self.window.mainloop()
    def event(self, initFrame, state, eventNumber, xPos):
        
        if self.eventNumber in idle:
            self.state = 1
            self.window.after(83, self.updateFrame, self.initFrame, self.state, self.eventNumber, self.xPos)
    def animate(self, initFrame, animation, eventNumber, x, y):
        if self.initFrame<len(animation)-1:
            self.initFrame+=1
        else:
            self.initFrame = 0
            self.eventNumber=randint(x,y)
        return self.initFrame, self.eventNumber
    
    def updateFrame(self, initFrame, state, eventNumber, xPos):
        
        if state == 1:
            self.frame = self.idle[self.initFrame]
            self.initFrame, self.eventNumber=self.animate(self.initFrame, self.idle, self.eventNumber, 1, 1)

        self.window.geometry('100x100+'+str(self.xPos)+'+'+str(self.yPos))
        self.label.configure(image=self.frame)
        self.window.after(1, self.event, self.initFrame, self.state, self.eventNumber, self.xPos)


    
timmy = Timmy()