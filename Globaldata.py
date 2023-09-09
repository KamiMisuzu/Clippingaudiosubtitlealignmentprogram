import json
import os

class Globaldata:
    
    _instance = None # 定义一个类变量_instance
    workDirectory=[]
    directory=None  #路径
    directorycild=None #选择的项目
    
    def __new__(cls, *args, **kwargs): # 重写__new__方法
        if cls._instance is None: # 如果_instance不存在
            cls._instance = super().__new__(cls) # 调用父类的__new__方法创建一个新对象，只传递cls参数
        return cls._instance # 返回_instance
    
    def __init__(self, json_path) -> None: # 在构造函数中添加json_path参数
        self.data=None
        self.outputData(json_path) # 把json_path传递给outputData方法
        self.setworkDirectory()
    def outputData(self,json_path): # 在outputData方法中添加json_path参数
        with open(json_path,'r') as json_file: # 用json_path作为路径
            self.data = json.load(json_file) # 把json数据赋值给Globaldata.data
            self.dircel=self.data["config_directory"] #获取默认路径
            # 不需要再调用json_file.close()
    def setworkDirectory(self):
        self.workDirectory = next(os.walk(self.dircel))[1]