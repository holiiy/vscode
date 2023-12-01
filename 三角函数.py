import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


pi = np.pi
# 设置字体
font = FontProperties(fname=r'C:\Windows\Fonts\simkai.ttf', size=15)

#font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=15)
# matplotlib绘制多图-2X2 4个子图
x1 = np.arange(- pi, pi, 0.01)
y1 = np.sin(x1)
x2 = x1
y2 = np.cos(x2)
x3 = np.arange(-0.5 * pi + 0.01, 0.5 * pi - 0.01, 0.01)
y3 = np.tan(x3)
x4 = np.arange(0.01, pi - 0.01, 0.01)
y4 = np.divide(1, np.tan(x4))

# 子图1-正弦函数
plt.subplot(2, 2, 1)
plt.title('y=sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x1, y1, '-r')
plt.grid()

# 子图2-余弦函数
plt.subplot(2, 2, 2)
plt.title('y=cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x2, y2, '-g')
plt.grid()

# 子图3-正切函数
plt.subplot(2, 2, 3)
plt.title('y=tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x3, y3, '-b')
plt.grid()
# 子图4-余切函数
plt.subplot(2, 2, 4)
plt.title('y=cot(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x4, y4, '-y')
plt.grid()


plt.suptitle('三角函数图像', color='k', fontproperties=font)
plt.show()