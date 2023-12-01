scores={'张三':100,'李四':98,'王五':45}
#key 的判断
print('张三'in scores)
print('张三' not in scores)

del scores['张三'] #删除指定的key-value对
scores.clear() #清空字典的元素
print(scores)
#在末尾增加
scores["a"]=5
#修改
scores["a"]=7
'''
字典中的所有元素都是一个键值对 key-value对,key不允许重复,value可以
字典中的元素是无序的
字典中的key必须是不可变对象
字典也可以根据需要动态地伸缩
字典会浪费较大的内存，是一种利用空间换时间的数据结构
'''
