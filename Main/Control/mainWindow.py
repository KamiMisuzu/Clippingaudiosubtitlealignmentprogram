import tkinter as tk
import Control.FrameContainer
import ttkbootstrap as ttk
class mainWindow(tk.Tk):
    frame = {}
    childwindowsetof={}
    def __init__(self):
        super().__init__()
        self.title('铃芽剪映辅助程序')
        self.geometry('390x540')
        self.resizable(False,False)
        self.iconbitmap("image\\favicon.ico")
    def addFrame(self,frame:Control.FrameContainer,id):#添加Frame对象
        
        self.frame.update({f"{id}": frame})
    def addchildwindow(self,childwindow,id):#添加Frame对象
        self.childwindowsetof.update({f"{id}": childwindow})

    def getFrame(self,id:str) -> Control.FrameContainer:#返回Frame对象

        return self.frame[f"{id}"]