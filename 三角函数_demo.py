import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=12)

# 生成 x 值，范围从 0 到 2π，间隔为 0.1
x = np.arange(0, 2 * np.pi, 0.1)

# 计算正弦函数值
sin_values = np.sin(x)

# 计算余弦函数值
cos_values = np.cos(x)

# 计算正切函数值
tan_values = np.tan(x)

# 计算余切函数值
cot_values = 1 / np.tan(x)

# 创建图形窗口
fig, ax = plt.subplots()

# 绘制正弦函数曲线
ax.plot(x, sin_values, label='正弦')
# 绘制余弦函数曲线
ax.plot(x, cos_values, label='余弦')
# 绘制正切函数曲线
ax.plot(x, tan_values, label='正切')
# 绘制余切函数曲线
ax.plot(x, cot_values, label='余切')

# 添加图例
ax.legend(prop=font)

# 添加标题和轴标签（使用中文）
ax.set_title('三角函数曲线图', fontproperties=font)
ax.set_xlabel('x', fontproperties=font)
ax.set_ylabel('y', fontproperties=font)

# 显示图形
plt.show()
