#append() 在列表末尾添加一个元素
lst=[10,20,30]
print("添加元素之前",lst,id(lst))
lst.append(100)
print("添加元素之后",lst,id(lst))
lst2=["hello","world"]
lst.append(lst2)
print(lst)
#将lst2作为一个元素添加到列表末尾
 
#向列表末尾一次性添加多个元素
lst.extend(lst2)
print(lst)
print("--------------------")
#向任意位置上添加一个元素
lst.insert(1,90)# insert()在元素之前插入
print(lst)

#切片 在任意位置上添加N多个元素
lst3=[True,False,"hello"]
lst[1:]=lst3
print(lst,id(lst))