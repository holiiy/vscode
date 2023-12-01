def find_first_unique_char(s):
    char_counts = {}

    # 第一次遍历字符串，统计字符出现次数
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # 第二次遍历字符串，找到第一个出现次数为 1 的字符
    for char in s:
        if char_counts[char] == 1:
            return char

    return ""

# 测试示例
s = "ababcde"
result = find_first_unique_char(s)
print(result)  
