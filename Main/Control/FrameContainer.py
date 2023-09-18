import Control.Buttonmanagement
import Control.Lablemanagement
import Control.Canvasmanagement
import Control.Scrollbarmanagement


from tkinter import ttk

class FrameContain(ttk.Frame):
    Buttonsetof={}
    Lablesetof={}
    Canvasetof={}
    Scrollbarofsetof={}
    
    def __init__(self,master,width=None,height=None,bd=None,bg=None,x=None,y=None,style=None):
        super().__init__(master)
        self["padx"]=x
        self["pady"]=y
        self["width"]=width
        self["height"]=height
        
        self.configure(relief='flat',borderwidth=1,style=style)
        # self["highlightthickness"]=1
        # self["highlightbackground"]="black"
        self.pack(padx=x,pady=y)
        self.pack_propagate(0)
        
    def addButtonsetof(self,button: Control.Buttonmanagement.Buttonmanagement,id): #添加按钮对象到字典中
        self.Buttonsetof.update({f"{id}":button})
        button.display()
    def addLablesetof(self,lable: Control.Lablemanagement.Lablemanagement,id): #添加文本对象到字典中
        self.Lablesetof.update({f"{id}":lable})
        lable.display()
    def addCanvasetof(self,canv: Control.Canvasmanagement.Canvasmanagement,id): #添加画布对象到字典中
        self.Canvasetof.update({f"{id}":canv})
        canv.display()  
    def addScrollbarofsetof(self,scrollbar: Control.Scrollbarmanagement.Scrollbarmanagement,id): #添加菜单栏对象到字典中
        self.Scrollbarofsetof.update({f"{id}":scrollbar})
        scrollbar.display()  

