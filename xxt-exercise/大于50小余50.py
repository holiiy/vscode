import random

# 生成随机数列表
random_numbers = [random.randint(1, 100) for _ in range(50)]

# 初始化字典，用于统计结果
result_dict = {'大于50': [], '小于50': []}

# 分组统计
for num in random_numbers:
    if num > 50:
        result_dict['大于50'].append(num)
    elif num < 50:
        result_dict['小于50'].append(num)

# 输出统计结果
print(result_dict)
