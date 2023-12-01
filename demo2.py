print("hello\nworld")
print("hello\tworld") #四个bit 四位
print("helloo\tworld")

print("hello\bworld")   #back 退格 将前一个字符推掉
print("hello\rworldsss")  #回车 return  覆盖之前的

print("http:\\\\baidu.com")
print("老师说：\"大家好\"")

#不希望字符串中的转义字符起作用使用原字符 r or R
#字符串最后不能是转义字符反斜杠 \ 两个可以
print (r"hello \n world..\\")
#反斜杠与回车\n连用表示跨行 （事情还没完）使用三个单引号 或三个双引号来表示字符串很长 需要跨行
print("     i love py    \n\
      i love c  \n\
      i love coding")

print("""i love py! 
i love c
i love coding """)