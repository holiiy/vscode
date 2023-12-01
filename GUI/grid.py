from tkinter import *
import tkinter as tk
 
 #grid表格布局，采用表格结构组织组件，子组件的位置由行和列的单元格确定，并且可以跨行和跨列，从而实现复杂的布局。 
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.pack()
 
        self.createWidget()
 
    def createWidget(self):
        '''通过grid布局实现登录界面'''
        self.label01 = Label(self, text='用户名')
        self.label01.grid(row=0, column=0)
        self.entry01 = Entry(self)
        self.entry01.grid(row=0, column=1)
        Label(self, text='用户名为手机号').grid(row=0, column=2)
 
        Label(self, text='密码').grid(row=1, column=0)
        Entry(self, show='*').grid(row=1, column=1)
 
        Button(self, text='登录').grid(row=2, column=1, stick=EW)
        Button(self, text='取消').grid(row=2, column=2, ipady=6)
 
if __name__ == '__main__':
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width -300)/2
    y = (screen_height -100)/2
    root.geometry('300x100+%d+%d'%(x,y)) 
   # root.geometry('300x100+200+300')
    root.title('登录系统')
    app = Application(root)
    root.mainloop()