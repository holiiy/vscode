try :
    n1=int(input('请输入一个整数:'))
    n2=int(input('请输入一个整数:'))
    result=n1/n2
except ValueError :
    print("hhhh")
except Exception as e :
    print('出错了')
    print(e)

else:

    print("输入正确",result)
finally:
    print("程序结束")
