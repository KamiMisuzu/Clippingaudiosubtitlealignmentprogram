from bindFunction.ControlFun import *
class Bindmethod:
    Bindingobjects=None #捆绑对象
    TriggerMode=None #触发方法
    def __init__(self,Bindingobjects,TriggerMode) -> None:
        self.Bindingobjects=Bindingobjects
        self.TriggerMode=TriggerMode

    def startBind(self,Bindingmethodname):
        self.Bindingobjects.Oj.bind(self.TriggerMode, getattr(self.Bindingobjects, Bindingmethodname)) # 使用 getattr 函数来获取已绑定的方法对象
    
    