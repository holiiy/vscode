def fun():
    '''
    show docstring
    这是文档字符串
    '''
    print('this is outer')
    def fun1():
        print('this is inner')
    
print(fun.__doc__)


def func1(obj): #外部闭包函数的参数是被装饰的函数对象
    def func2():
        print('aaaabbbb')
        return obj() #返回了外部函数接收的被装饰函数的调用
    return func2

@func1
def myprint():
    print('你好，我是print')

myprint()

myprint()

