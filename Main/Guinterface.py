from Control import *
from Abstractintermediary.Bindmethod import *
from bindFunction.ControlFun import *
import os
from Globaldata import *


def start():
    g1 = Globaldata("profile.json")
    win = mainWindow()
    style = ttk.Style()

    statementFrame = FrameContain(win, width=500, height=25, style="My.TFrame")
    defFrame = FrameContain(win, width=500, height=200)
    selectFrame = FrameContain(win, width=500, height=46)
    dataFrame = FrameContain(win, width=500, height=270)

    # text1 = Textmangement(statementFrame,text="测试窗口")
    # 添加容器
    win.addFrame(id="声明", frame=statementFrame)
    win.addFrame(id="功能窗口", frame=defFrame)
    win.addFrame(id="选项窗口", frame=selectFrame)
    win.addFrame(id="信息窗口", frame=dataFrame)

    informationWindow = win.getFrame(id="信息窗口")
    button4 = Buttonmanagement(informationWindow, x=5, y=2, text="设置目录", width=10, height=20, font="黑体", fg="red",
                               types='grid')
    data1 = Lablemanagement(informationWindow, text="当前目录:" + g1.data["config_directory"], types='grid', x=1, y=2,
                            foreground="red", pady=20)
    data2 = Lablemanagement(informationWindow, text="当前选择项目:", types='grid', x=0, y=2, foreground="red", pady=10)


    informationWindow.addLablesetof(lable=data1, id="路径")
    informationWindow.addLablesetof(lable=data2, id="项目")
    informationWindow.addButtonsetof(button4, id="设置目录")
    

    defWindows = win.getFrame(id="功能窗口")
    defcanvase = Canvasmanagement(defWindows, width=500, height=10000, x=0, y=0, relwidth=1, relheight=1, style=style)
    defscrollbar = Scrollbarmanagement(defWindows, orient="vertical", command=defcanvase.yview)
    defWindows.addCanvasetof(id="底板", canv=defcanvase)
    defWindows.addScrollbarofsetof(id="滚动条", scrollbar=defscrollbar)
    defcanvase.config(yscrollcommand=defscrollbar.set)


    defcanvase.addButton(g1, eventOne="pili", label=data2)


    button1 = Buttonmanagement(selectFrame,x=0,text="设置",width=100,height=46,font="黑体",fg="red",types="place")
    button2 = Buttonmanagement(selectFrame, x=145, text="启动", width=100, height=46., font="黑体", fg="red",
                               types="place")
    button3 = Buttonmanagement(selectFrame, x=290, text="关于", width=100, height=46., font="黑体", fg="red",
                               types="place")

    selectionWindow = win.getFrame(id="选项窗口")
    selectionWindow.addButtonsetof(button=button1,id="设置")
    selectionWindow.addButtonsetof(button=button2, id="启动")
    selectionWindow.addButtonsetof(button=button3, id="关于")

    statementWindow = win.getFrame(id="声明")
    lable1 = Lablemanagement(statementWindow, text="本程序完全开源免费 作者b站UID:398204337", x=0.20, foreground="red",
                             types='place')
    statementFrame.addLablesetof(lable=lable1, id="测试")

    
    Bindmethod(Bindingobjects=ControlFun(button4, label=data1, lable2=data2, canvas=defcanvase, dirdata=g1),
               TriggerMode="<Button-1>").startBind("select_directory")  # 绑定事件
    Bindmethod(Bindingobjects=ControlFun(defcanvase), TriggerMode="<Configure>").startBind(
        "update_scrollregion")  # 绑定事件
    Bindmethod(Bindingobjects=ControlFun(button2, dirdata=g1), TriggerMode="<Button-1>").startBind(
        "start_Trackali")  # 绑定事件
    Bindmethod(Bindingobjects=ControlFun(button3), TriggerMode="<Button-1>").startBind("statement_Trackali")  # 绑定事件
    Bindmethod(Bindingobjects=ControlFun(button1, dirdata=g1,master=win), TriggerMode="<Button-1>").startBind("pop_up_settings_window")



    win.mainloop()
