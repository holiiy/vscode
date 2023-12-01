class FileReader(): #抽象类

    def read_date(self):
        pass

class TextFileReader(FileReader): #继承父类
    def __init__(self,path): #构造器
        self.path = path

    def read_date(self):
        f=open(self.path,'r',encoding='utf-8')
        for line in f.readlines():
            line = line.strip()
              
