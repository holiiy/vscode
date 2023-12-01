scores={'张三':100,'李四':98,'王五':45}
#获取所有key
keys=scores.keys()
print(keys,type(keys))
print(list(keys)) #将所有的key组成的视图转成列表

#获取所有的value
values=scores.values()
print(values,type(values))
print(list(values))

#获取所有的key-value对
items=scores.items()
print(items)
print(list(items)) #列表元素由元组组成