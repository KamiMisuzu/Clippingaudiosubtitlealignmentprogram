import ttkbootstrap as ttk

class Lablemanagement(ttk.Label):

    def __init__(self,master,text=None,y=None,x=None,foreground=None,background=None,types=None,pady=None):
        super().__init__(master=master)
        self.x=x
        self.y=y
        self.text=text
        self.foreground=foreground
        self.types=types
        self.pady=pady
        self.configure(text=self.text,background=background,foreground=self.foreground)
        
    def display(self):
        if self.types =="place":
            self.place(relx=self.x,rely=self.y)
            return
        if self.types=='grid':
            self.grid(row=self.x, column=self.y,pady=self.pady)
            return