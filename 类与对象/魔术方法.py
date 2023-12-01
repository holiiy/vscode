class student:
# ___init__  构造方法，创建类对象的时候设置初始化行为
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
#__str__ 魔术方法
    def __str__(self) -> str:#控制类转换字符串的行为
        return f"name= {self.name},age = {self.age}"
#__lt__  魔术方法  使类之间可以比较大小 （大于 小于比较）
    def __lt__(self,other): 
        return self.age < other.age
#__le__ 魔术方法  小于等于 大于等于比较
    def __le__(self,other):
        return self.age <= other.age
#__eq__ 魔术方法 比较类对象是否相等
    def __eq__(self,other) -> bool:
        return self.age == other.age
    

stu1=student('胡',11)
stu2=student('周',20)
print(stu1)
print(str(stu1))
#print(stu1<=stu2) #not supported between instances of 'student' and 'student'
print(stu1==stu2)
#如果没用__eq__ 使用类之间==比较 则默认比较内存地址