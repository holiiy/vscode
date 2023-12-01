print(chr(0b100111001011000)) #ascii
print(ord("乘"))
print(chr(20056))
import keyword #关键字
print (keyword.kwlist)
#匿名函数 lambda   lambda[参数列表]：表达式
#压缩内存
sum = lambda arg1,arg2,arg3: arg1+arg2+arg3
print(sum(1,2,3))
import math
print(math.cos(30))

def bar(x):
    print(x)
    
print(bar(5)) # 输出 5 和 None

def Info(name,country='中国'):

    print('%s,%s'%(name,country))

Info('美国','大垵')