a = [1,2,3,4,5,6,7,1,1,2,3,4,5]
print(max(set(a),key=a.count))

from collections   import Counter
cnt = Counter(a)
print(cnt.most_common(1))
'''函数most.common()是python内建模块collections中的counter类的函数，用来计算列表中元素出现的频数，返回的结果是元组列表，不是字典.'''
d = {'a':1,'b':2}
print(d.get('c',3)) # 3

items = ['foot','eye','leg']
print(' '.join(items))

date = [2,'heloo',3,4,3.4] #   join()：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
print(','.join(map(str,date)))

import os
a5 = os.path.join('/hello/','good /boy/','xiaoming')
print(a5)
#输出/hello/good /boy/xiaoming