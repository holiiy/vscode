class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #age不希望在类的外部被使用，使用两个— —
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
#在类的外部使用name与age
print(stu.name)
#print(stu.__age)
print(dir(stu))
print(stu._Student__age)#在类的外部通过_Student__age访问

class a(object):
    pass
class b(object):
    pass
class c(a,b):
    pass
#调用父类使用super()方法