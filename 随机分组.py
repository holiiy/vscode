import random

students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack",
            "Kelly", "Liam", "Mia", "Nathan", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tom",'ss','s','a','b','c','d','e','f',]

# 首先，对同学进行随机排序
random.shuffle(students)

# 计算每组的人数
group_size = len(students) // 5

# 检查是否有剩余的人，若有则增加人数到每组至少五人
remainder = len(students) % 5
if remainder > 0:
    group_size += 1

# 分组
groups = [students[i:i+group_size] for i in range(0, len(students), group_size)]

# 输出结果
for i, group in enumerate(groups):
    print(f"Group {i+1}: {', '.join(group)}")
