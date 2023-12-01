# 打开文件
import io
file_path = "d:/a.txt"
file = open(file_path, "w")
# 循环输入字符并写入文件
while True:
    char = input("请输入一个字符：")
    if char == "#":
        break
    file.write(char)

# 关闭文件
file.close()
