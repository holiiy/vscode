def func1(func):
    def func2(x,y):
        print(x,y)
        x +=5
        y +=5
        return func(x,y)
    return func2

@func1
def mysum(a,b):
    print(a+b)

mysum(1,2)