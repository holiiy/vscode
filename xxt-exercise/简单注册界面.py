def register():
    # 获取用户输入的基本信息
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    email = input("请输入邮箱: ")

    # 将信息写入文件
    with open('user_info.txt', 'a',encoding='utf-8') as file:
        file.write(f"用户名: {username}, 密码: {password}, 邮箱: {email}\n")
    print("注册成功！")

if __name__ == "__main__":
    register()
