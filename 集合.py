'''
与列表字典一样属于可变类型的序列
集合是没有value的字典 (key,value) 键值对
集合中元素是无序的
'''

#第一种创建方式使用 {}  ..... 与字典一样集合中的元素不能重复
s={2,3,4,5,5,6,7,7}
print(s)

#第二种 使用内置函数 set()
s1=set(range(6)) #[0,6)
print(s1,type(s1))

s2=set([1,2,3,3,4,5,6,7]) #列表转集合
print(s2,type(s2))
s3=set((1,2,3,4,5,66)) #元组转集合
print(s3,type(s3))
s4=set('python') #字符串转集合
print(s4,type(s4))
s5=set({12,4,34,66,55,6}) #集合转集合
print(s5,type(s5))

#定义一个空集合
s6={}  #dict字典类型
print(s6,type(s6))

s7=set() #这才是空集合
print(s7,type(s7))