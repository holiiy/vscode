#使用{}创建字典
scores={'张三':100,'李四':98,'王五':45}
for key, value in scores.items():
    print(key, value, sep=": " )
scores["a"]=5
print(scores, type(scores))

#第二种创建 使用内置函数dict()
student=dict(name='jack',age=20)
print(student)

#第三种 空字典
d={}
print(d)

