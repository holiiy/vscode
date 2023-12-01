a=int(input("请输入一个数"))
b=int(input("请输入一个数"))
'''if a>=b:
    print("a大于等于b")
else:
    print("a小于b")
'''

print( (a,"大于等于",b) if a >= b else ( a,"小于",b))
print( (str(a)+"大于等于"+str(b)) if a >= b else ( str(a)+"小于"+str(b)))
