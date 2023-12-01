import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

start_time = time.time()

result = 0
for i in range(1, 101):
    result += factorial(i)

end_time = time.time()
execution_time = end_time - start_time


print(f"计算时间：{execution_time} 秒")
