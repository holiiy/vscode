import re

s='xaabcabbay'
m=re.findall(r'e',s)
#print(m)
#re.findall匹配的时候，会把结果放到list返回，如果没有匹配到返回空list不会报错

reg=r'ab?'
m=re.findall(reg,"acabbc")
#print(m)
#  ？ 零或一次 ['a', 'ab']

reg=r'[a-z]+\b'
m=re.search(reg,"the bike is black")
#print(m)  <re.Match object; span=(0, 3), match='the'>

reg=r'ab*'
m=re.search(reg,"bbacabbc")
print(m.group(1))

'''
正则表达式中的三组括号把匹配结果分成三组

m.group() == m.group(0) == 所有匹配的字符(即匹配正则表达式整体结果)
group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
m.groups() 返回所有括号匹配的字符，以tuple格式。m.groups() == (m.group(0), m.group(1), …)

没有匹配成功的，re.search（）返回None

当然郑则表达式中没有括号，group(1)肯定不对了。'''
