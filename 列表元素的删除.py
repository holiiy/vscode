'''
remove() 一次删除一个元素，重复元素删除第一个，元素不存在抛出ValueError
pop() 删除一个指定索引位置上的元素，指定元素不存在抛出IndexError
切片 一次至少删除一个元素
clear() 清空列表
del obj 删除列表
'''
lst=[10,20,30,30,40,50,60]
lst.remove(30)
print(lst)

lst.pop(1)
print(lst)
 
new_lst=lst[1:3]
#产生新的id

lst[1:3]=[]
print(lst)

lst.clear()
print(lst)

del lst