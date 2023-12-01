
#用蒙特卡搈方法计算圆周率π
#正方形内搉有一搋搊切的圆，在这搋正方形内搉，随机产生10000搋点，计算它们与中心点的距离，从而判断是否落在圆的内搉，如果这些点均匀分布，那么圆内的点应该占到搌有点的 π/4

import time
import random
hits=0
pi=0
DARTS=10000*10000
start=time.perf_counter()
for i in range(DARTS):
    x,y=random.random(),random.random()
    dist=pow(x ** 2+y**2,0.5)
    if dist <= 1.0:
        hits+=1
pi=4*(hits/DARTS)
print("圆周率的值是{:.10f}".format(pi))
print("程序运行时间为{}s".format(time.perf_counter()-start))
