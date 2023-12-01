lst=[20,40,10,98,11]
print(lst)
lst.sort()
print("排序后：",lst)
 # 列表对象的sort()方法       原地操作直接修改列表 不会返回任何结果
lst.sort(reverse=False)
print(lst)#从小到大 升序
lst.sort(reverse=True)
print(lst)#从大到小 降序
print("-----------使用内置函数sorted()排序，将生成一个新的列表对象-------------")
new_lst=sorted(lst) #False 升序
print(new_lst)
new_lst=sorted(lst,reverse=True)#降序
print(new_lst) 