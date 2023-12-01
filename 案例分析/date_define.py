from typing import Any


class record():
    
    def __init__(self,date,order_id,money,province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province  
        #方法中的参数传给成员变量
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
    def add(a,b):
       return a+b
