class Car:
    def __init__(self,cno,brand,cost,color):
        self.cno=cno
        self.brand=brand
        self.cost=cost
        self.color=color

    def print_info(self):
        print('车牌{}是{}，价格{}，颜色为{}'.format(self.cno,self.brand,self.cost,self.color))

    def drive(self,dest):
        print(self.cno,'开往',dest)
        
if __name__=='__main__':
    c=Car('鄂A888888','奔驰','1888888','红色')
    c.print_info()
    c.drive('鄂州')