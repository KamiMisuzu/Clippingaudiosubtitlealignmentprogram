# 界面类的方法
from Control.childWindow import *
from tkinter import messagebox
from MainFunction.Trackalignment import *
import os


class ControlFun:
    methodSetof = {}

    def __init__(self, Oj=None, label=None, canvas=None, dirdata=None, lable2=None) -> None:
        self.Oj = Oj  # 绑定对象
        for attr in dir(ControlFun):  # 遍历类的所有属性和方法
            if not attr.startswith("__"):  # 过滤掉内置的属性和方法
                value = getattr(ControlFun, attr)  # 获取属性或方法的值
                self.methodSetof[attr] = value  # 将键值对存储到字典中
        self.label = label
        self.canvas = canvas
        self.dirdata = dirdata
        self.label2 = lable2

    def update_scrollregion(self, event):

        self.Oj.config(scrollregion=self.Oj.bbox("all"))

    def select_directory(self, event):
        # 弹出文件选择对话框，获取用户选择的目录
        self.dirdata.directory = filedialog.askdirectory()
        # 更新标签显示的目录结构
        self.label.config(text=f"当前目录:{self.dirdata.directory}")
        self.canvas.delButton()
        self.dirdata.dircel = self.dirdata.directory
        self.dirdata.setworkDirectory()
        self.canvas.addButton(g1=self.dirdata, eventOne="pili", label=self.label2)
        file_path = "profile.json"
        key = "config_directory"
        value = self.dirdata.directory
        with open(file_path, 'r') as file:
            data = json.load(file)  # 读取JSON数据
            data[key] = value  # 更新指定键的值

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def change_label_text(self, event):

        self.dirdata.directorycild = self.Oj.configname
        # print(self.dirdata.dircel+"/"+self.dirdata.directorycild)
        self.label.config(text="当前选择项目:" + self.Oj.configname)

    def start_Trackali(self, event):
        if self.dirdata.directorycild == None:
            messagebox.showerror("失败",
                                 "请选择一个项目!")
            return
        file_path = self.dirdata.dircel + "/" + self.dirdata.directorycild + "/" + "draft_content.json"
        if not os.path.exists(file_path):
            messagebox.showerror("失败",
                                 "执行失败该文件夹下没有找到您的工程文件！\n请检查点击文件夹中是否有draft_content.json文件")
            return
        result = start(path=file_path)
        if result:
            messagebox.showinfo("成功", "执行成功！")
            return
        elif result is False:
            messagebox.showinfo("失败", "请确认是否同时拥有音频轨道和字幕轨道\n也可能是未知错误很抱歉给你带来失败的作品请期待更新或者联系作者反馈")
            return
        messagebox.showinfo("未知错误", "执行失败！")

    def statement_Trackali(self, event):
        project_declaration = """
                                                        项目声明
            我的项目是开源免费的

            感谢您对我的项目感兴趣！我的项目是一个开源项目，旨在为开发者提供免费的解决方案。我相信开源软件的力量，通过共享代码和知识，我可以共同推动技术的发展。

            以下是我项目的一些关键特点：

            开源性质：我的项目完全开源，您可以自由地查看、修改和分发我的代码。这意味着您可以根据自己的需求进行定制和改进。

            免费使用：我的项目是免费提供给所有用户使用的。您不需要支付任何费用就可以使用我的软件，并且没有任何隐藏费用或限制。

            持续更新：由于本人正在读书，时间不算多，我会有机会就发布更新版本，修复漏洞、改进功能并提供新的功能。您可以随时获取最新的版本并享受最佳的使用体验,如果有什么想法可以联系我。

            我欢迎您加入我的项目，并为您提供一个开放、自由和免费的开发环境。如果您对我的项目有任何疑问或建议，请随时与我联系。

            """

        messagebox.showinfo("项目声明", project_declaration)
