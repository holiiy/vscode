scores={'张三':100,'李四':98,'王五':45}

#第一种，使用[]
print(scores['张三'])
#print(scores['陈六']) #  输出KeyError:'陈六'

#第二种，使用get()方法
print(scores.get('张三'))
print(scores.get('陈六')) #None
print(scores.get('麻七',99)) #如果麻七存在字典中则输出值 如果不存在则输出提供的默认值