import tkinter as tk
'''
pack按照组件的创建顺序将子组件添加到父组件中，按照垂直或者水平的方向自然排布，如果不指定任何选项，默认在父组件中自顶向下垂直添加组件。

pack是代码量最少，最简单的一种，可以用于快速生成界面。
'''
#from tkinter import *
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width -200)/2
y = (screen_height -100)/2
window.geometry('200x100+%d+%d'%(x,y)) 
#geometry() 宽度 x 高度+屏幕x坐标 + 屏幕x坐标

configs = {'font':('Arial','12','bold'),'fg':'red','bg':'white'}
tk.Label(window,cnf=configs,text='abc').pack()

window.title('login')
window.mainloop()
