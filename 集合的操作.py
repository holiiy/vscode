'''
集合元素的新增操作
调用add()方法，一次添加一个元素
调用update()方法至少添加一个元素
集合元素的删除操作
调用remove()方法 一次删除一个指定元素，如果指定元素不存在则抛出KeyError
调用discard()方法 一次删除一个指定元素，如果指定元素不存在不抛出异常
调用pop()方法 一次删除一个任意元素
调用clear()方法 清空集合
'''
#新增
s={10,20,30,40,50,60}
s.add(80)  #一次添加一个
print(s)
s.update({200,400,300}) #一次添加多个
print(s)
s.update((78,45,66)) #添加元组
print(s)
#删除
s.remove(200)
print(s)
#s.remove(500)  抛出异常
s.discard(500) #不抛出异常
print(s)

s.pop()
#s.pop(400) #pop函数不能添加参数

s.clear()
print(s)
