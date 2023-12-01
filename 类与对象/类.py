class student:
    name = None
    gender = None
    age = None
    def Sayhi(self): 
        print('hello')
    
    def __init__(self) -> None:#构造方法
        pass
'''
每个与类相关联的方法调用都自动传递实参self 
它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
'''
stu_1 = student()
stu_1.age=1
student.age
stu_1.Sayhi()


import winsound
class clock:
    id = None
    price = None
    def ring(self):
        winsound.Beep(2000,3000) #频率 时间
clock_1 = clock()
#clock_1.ring()