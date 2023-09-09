import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from Control.Buttonmanagement import *
from Control.Lablemanagement import *

class childWindow(ttk.Toplevel):

    def __init__(self,master,sizey=None,width=None,height=None):
        super().__init__(master=master)

        self.iconbitmap("image/favicon.ico")
        self.title('设置页面')
        self.geometry(sizey)
        self.resizable(False,False)
        self.transient(master)  # 设置子窗口为父窗口的模态对话框
        self.grab_set()  # 阻止用户与父窗口进行交互
        window_width = width
        window_height = height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
       

    def addFrame(self,frame,id):#添加Frame对象
        
        self.frame.update({f"{id}": frame})
    def addFrame(self,childwindow,id):#添加Frame对象
        self.childwindow.update({f"{id}": childwindow})
        
    def getFrame(self,id:str):#返回Frame对象

        return self.frame[f"{id}"]
    # def addclidButton(self):
    #     button = Buttonmanagement(self, text="选择目录")
    #     button.pack()
    # def addclidlabel(self):
    #     # # 创建一个标签来显示目录结构
    #     self.label = Lablemanagement(self, text="目录结构")
    #     self.label.pack()
    #     #   def select_directory(self):
    #     # # 弹出文件选择对话框，获取用户选择的目录
    #     #     directory = filedialog.askdirectory()

    #     # # 更新标签显示的目录结构
    #     #     self.label.config(text=f"目录结构：{directory}"