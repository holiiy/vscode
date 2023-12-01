import os

def count_file_types(directory):
    file_counts = {}
    
    # 遍历目录及其子目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 获取文件扩展名
            ext = os.path.splitext(file)[1].lower()
            
            # 统计不同类型文件的个数
            if ext in file_counts:
                file_counts[ext] += 1
            else:
                file_counts[ext] = 1
    
    return file_counts

# 指定要统计的目录路径
directory_path = 'D:\code\py code'

# 调用函数进行统计
result = count_file_types(directory_path)

# 输出统计结果
for ext, count in result.items():
    print(f'{ext}: {count}')
