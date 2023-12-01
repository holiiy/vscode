lst=[i for i in range(1,10)]
print(lst)

items=['Fruits','Books','Others']
prices=[96,78,85]
#使用zip()内置函数 用可迭代的对象作为参数，将对象中对应的元素打包成元组
d={item.title():price  for item,price in zip(items,prices)}
print(d)
#首字母大写 title() 全体字母大写upper()