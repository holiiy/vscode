#列表名[start: stop :step] 切片范围[start,stop) 
#step默认为一 简写为[start:stop]
lst=[10,20,30,40,50,60,70,80]
#print(lst[1:6:1])
print(lst[1:6])
lst2=lst[1:6]
print('原列表',id(lst))
print('hou列表',id(lst2))
print('原列表',type(lst))
'''两个列表id不同 type() value() id()'''
print(lst[1::2]) #省略 stop
print("-----------step步长为负数情况------------")
print("原列表：",lst)
print(lst[::-1])
#start=7 stop=0 包括0 step=-1 从后往前
print(lst[7:0:-1]) 
#[7,0)