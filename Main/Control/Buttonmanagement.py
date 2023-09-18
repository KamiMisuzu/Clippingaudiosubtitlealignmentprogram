# import tkinter
import ttkbootstrap as ttk
class Buttonmanagement(ttk.Button):
    
    def __init__(self,master,x=None,y=None,bg=None,font=None,width=None,height=None,
                 text=None,fg=None,style=None,configname=None,ys=None,masterCanve=None
                 ,Mwidth=None,Mheight=None,types=None,pady=None):
        super().__init__(master)
        self.master=master
        self.ys=ys
        self.x = x
        self.y = y
        self.bg = bg
        self.font = font
        self.width= width
        self.height= height
        self.text= text
        self.fg=fg
        self.style=style
        self.configname=configname
        self.types=types
        self.pady=pady
        self.configure(width=self.width, text=self.text)


        
        # self.place(x=self.x,y=self.y)
    
    def display(self,):
        if self.types =="place":
            self.place(x=self.x,y=self.y,width=self.width,height=self.height)   
            return
        if self.types=='grid':
            self.grid(row=self.x, column=self.y,pady=self.pady)
            return
        