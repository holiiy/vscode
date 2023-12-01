
import random

# 生成 N 个随机整数
N = 1000
random_numbers = [random.randint(1, 1000) for _ in range(N)]

# 去重，只保留一个相同的数字
unique_numbers = list(set(random_numbers))

# 排序，从大到小
sorted_numbers = sorted(unique_numbers, reverse=True)

print(sorted_numbers)

