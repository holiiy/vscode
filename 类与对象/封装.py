#现实世界中的属性与行为描述为程序世界中类的成员变量与成员方法 对现实世界的描述
#私有的成员变量与私有的成员方法无法被外部 ---类对象无法访问，可以通过内部方法使用 ---类中的其他成员
class phone :
    __current_voltage  = 0.5 #当前电压 私有变量

    def __keep_single_core(self):  #私有方法
        print("让cpu单核模式运行") 


    def call_by_5g(self):
        if self.__current_voltage >=1:
            print('5g通话已开启')
        else:
            self.__keep_single_core()
            print('电量不足，无法使用5g通话')

phone1 = phone()
phone1.call_by_5g()