
import tkinter as tk

class Scrollbarmanagement(tk.Scrollbar):
    def __init__(self,master,orient=None,command=None,side=None,fill=None):
        super().__init__(master)
        
        self.configure(orient=orient,command=command)
    def display(self):
        self.pack(side="right", fill="y")