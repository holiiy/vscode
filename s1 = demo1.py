a =open('D:/aaa.txt','a+')
print("hhh",file=a) #如果文件不存在则创建，如果存在则追加
a.close()