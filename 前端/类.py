class Student:
    native_place='湖北'  #类属性
    def __init__(self,name,age):
        self.name=name    #self.name 为实体属性 将局部变量name赋值给self.name
        self.age=age

#实例方法
    def eat(self):
        print('吃饭')

#静态方法
    @staticmethod
    def method():
        print('静态方法')
#类方法
    @classmethod
    def cm(cls):   #与self一样都是默认参数
        print('类方法')

#在类之外的定义称为函数 类之内的称为方法、
def drink():
    print('喝水')

#创建Student类对象
stu1 = Student('张三',20)
#类的实例方法的两种使用方式
stu1.eat()         
     #对象名.方法名()
Student.eat(stu1)       #类名.方法名.(类的对象)  --->方法定义的self
drink()

#类属性的使用方式
print(stu1.native_place)
Student.native_place='湖南'
print(stu1.native_place)
#类方法的使用方式
Student.cm()
Student.method()
stu1.method()
stu1.cm()

print(stu1.name)
#动态的绑定属性和方法 只在stu1对象中存在 类对象中并没有
stu1.gender='男' #动态绑定属性 
stu1.drink=drink #动态绑定方法 drink没绑定之前是函数绑定之后为方法
stu1.drink()
print(stu1.name,stu1.age,stu1.gender)