import webbrowser
import urllib.request
import threading
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk
 
def open_website():
    suffix = e1.get()
    url = 'https://woecn.com/vodsearch/'+ suffix +'-------------.html'
    webbrowser.open(url)
 
def download_file():
    try:
        url = "https://www.xn--rsst22a0xx.cn/down.php/94cf820cfb0d2854026aaea9da162dd4.apk"  # 将这里的URL替换为你的固定链接
        filename = url.split("/")[-1]
        download_dir = filedialog.askdirectory()  # 让用户选择一个下载位置
        full_path = download_dir + '/' + filename
 
        # 创建一个新的进度条
        progress = ttk.Progressbar(frame, length=400, mode='determinate')
        progress.pack(pady=10)
 
        # 定义一个函数来更新进度条
        def reporthook(blocknum, blocksize, totalsize):
            readsofar = blocknum * blocksize
            if totalsize > 0:
                percent = readsofar * 1e2 / totalsize
                progress['value'] = percent
                master.update()
 
        urllib.request.urlretrieve(url, full_path, reporthook)
        messagebox.showinfo("提示", "下载完成")
    except Exception as e:
        messagebox.showerror("错误", str(e))
 
def generate_qrcode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data('https://wwxm.lanzouy.com/iWUVq150fauh')
    qr.make(fit=True)
 
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label = Label(frame, image=img)
    label.image = img
    label.pack()
 
 
master = Tk()
master.title("影视大全")
master.geometry("500x400+500+300")  # 设置窗口大小和位置
master.configure(bg='lightblue')  # 更改背景颜色
 
frame = Frame(master, bg='lightblue')
frame.pack(expand=True)
 
Label(frame, text="APP.educlub.icu", bg='lightgreen', font=("Helvetica", 16)).pack()  # 更改字体
 
Label(frame, text="输入影视名称", bg='lightblue', font=("Helvetica", 14)).pack()
 
e1 = Entry(frame, font=("Helvetica", 12))
e1.pack()
 
Button(frame, text='点击搜索', command=open_website, font=("Helvetica", 12), bg='lightgreen').pack(pady=10)  # 更改按钮样式
 
Button(frame, text='点击下载影视APP', command=lambda: threading.Thread(target=download_file).start(), font=("Helvetica", 12), bg='lightgreen').pack(pady=10)  # 添加下载文件按钮
 
Button(frame, text='点击扫码下载(密码8888)', command=generate_qrcode, font=("Helvetica", 12), bg='lightgreen').pack(pady=10)  # 添加生成二维码按钮
 
master.mainloop()