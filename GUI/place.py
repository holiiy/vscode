 #place 布局管理器可以通过坐标精确控制组件的位置，适用于一些布局更加灵活的场景。
import tkinter as tk
win = tk.Tk()
win.geometry("300x300")

lab1 = tk.Label(win, text="pack布局1", width=10, height=2, bg="pink")
lab1.place(x=20, y=20)
lab2 = tk.Label(win, text="pack布局2", width=10, height=2, bg="blue")
lab2.place(x=50, y=80)
lab3 = tk.Label(win, text="pack布局3", width=10, height=2, bg="pink")
lab3.place(x=120, y=120)


win.mainloop()
