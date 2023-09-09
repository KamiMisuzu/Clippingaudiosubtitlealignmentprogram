import tkinter as tk
from Control.Buttonmanagement import *
from Abstractintermediary.Bindmethod import * 
from bindFunction.ControlFun import *


class Canvasmanagement(tk.Canvas):
    buttons=[]
    def __init__(self,master,width=None,height=None,x=None,y=None,fill=None, relwidth=None, relheight=None,yscrollcmmand=None,style=None) -> None:
        super().__init__(master)
        self.x=x
        self.y=y
        self.width=width   
        self.height=height
        self.fill=fill
        self.relwidth=relwidth
        self.relheight=relheight
        self.style=style
        self.configure(width=self.width,height=self.height,yscrollcommand=yscrollcmmand)
    def display(self):
        self.place(relx=self.x,rely=self.y,relwidth=self.relwidth,relheight=self.relheight)

    def addButton(self,g1,eventOne=None,label=None):
        if eventOne=="pili":
            i=0
            for folder in g1.workDirectory:
                y = 20 + i * 30
                button = Buttonmanagement(self, text=f"{folder}",width=500,style=self.style,configname=folder,ys=y,masterCanve=self)
                Bindmethod(Bindingobjects=ControlFun(button,label=label,dirdata=g1),TriggerMode="<Button-1>").startBind("change_label_text") 
                self.create_window(200, y, window=button)
                self.buttons.append(button)
                i+=1
    def delButton(self):
        for button in self.buttons:
            button.destroy()
        self.buttons = []
    def GradientButtonOn(self,select):
        pass