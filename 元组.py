'''
python 内置的数据结构之一，是一个不可变序列
不可变序列有元组和字符串
不可变序列没有增删改操作
可变序列：列表、字典
可变序列对序列进行增删改 对象地址不发生改变，不可变序列(字符串 元组)改变id
'''

#第一种使用(),可以写成t2='Python','world',98 省略小括号
t=('Python','world',98)
t2='Python','world',98 
print(t,type(t))
print(t2,type(t2))

#第二种创建方式，使用内置函数tuple()
t1=tuple(('Python','world',98))
print(t1,type(t1))

#如果元组中只有一个元素，逗号不能少否者为字符串
t3=('Python',)
print(t3,type(t3))

#空列表
lst=[]
lst1=list()

#空字典
d={}
d2=dict()

#空元组
t4=()
t5=tuple()

print(t4,t5,lst,lst1,d,d2)
print(type(t4))
'''
如果元组中对象本身为不可变对象，则不能再引用其他对象
如果元组中的对象是可变对像，则可变对象的引用不允许改变，但数据可以改变(可变序列)
'''