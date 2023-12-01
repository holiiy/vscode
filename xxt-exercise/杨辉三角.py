def generate_pascal_triangle(num_rows):
    triangle = []
    
    for i in range(num_rows):
        row = [1] * (i + 1)
        
        if i > 1:
            prev_row = triangle[i - 1]
            
            
            for j in range(1, i):
                row[j] = prev_row[j - 1] + prev_row[j]
        

        triangle.append(row)
    
    return triangle

# 输入要生成的行数
num_rows = int(input("请输入要生成杨辉三角的行数："))

triangle = generate_pascal_triangle(num_rows)
print( generate_pascal_triangle(num_rows))

# 打印杨辉三角
for row in triangle:
    # 空格连接字符串 ' '.join
    #map(str,row) 将row 转换为字符串
    print(' '.join(map(str, row)).center(num_rows*2)) # 居中对齐 占据宽度为num_rows * 2
