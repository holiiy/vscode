class Car:
    warning="喝酒不开车，开车不喝酒!"

    def __init__(self,cno,brand,cost,color):
        self.cno=cno
        self.brand=brand
        self.cost=cost
        self.color=color

    def print_info(self):
        print('车牌{}是{}，价格{}，颜色为{}'.format(self.cno,self.brand,self.cost,self.color))

    def drive(self,dest):
        print(self.warning)
        print(self.cno,'开往',dest)

    @classmethod
    def set_warning(self,warning):
        self.warning=warning


if __name__=='__main__':
    c=Car('鄂A888888','奔驰','1888888','红色')
    c.print_info()
    c.drive('海南岛')
    Car.set_warning("快乐出行，安全回家！")
    c.drive('北京')