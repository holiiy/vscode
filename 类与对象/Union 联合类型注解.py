from __future__ import annotations
from typing import Union

def add(x:int,y:int) ->None: #对形参进行类型注解   返回值类型注解
    pass

my_list: list[Union[int, str]] = [1,2,"hhh"] #使用Union进行联合注解

def fun(date: Union[str,int]) ->Union[str,int]:
    pass

print(type(my_list))
add()
