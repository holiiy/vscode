a = int(input('请输入第一个数: '))
b = int(input('请输入第二个数: '))
Min = min(a,b)
Gys = 16
for i in range(1,Min+1):
    if a%i == 0 and b%i == 0:
        Gys = i
print('最大公约数为：%d' %Gys)          
Gbs = a*b / Gys
print('最小公倍数为:%d' %Gbs)
