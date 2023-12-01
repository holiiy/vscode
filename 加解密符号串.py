from cryptography.fernet import Fernet
from itertools import cycle

# 生成随机对称密钥
def generate_key():
    key = Fernet.generate_key()
    return key

# 使用对称密钥加密符号串
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# 使用对称密钥解密符号串
def decrypt_message(encrypted_message, key): 
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# 示例使用
message = "Hello, World!"
key = generate_key()

key_cycle = cycle([key])  # 创建密钥的无限迭代器

encrypted_message = encrypt_message(message, next(key_cycle))  # 使用迭代器的下一个密钥
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, next(key_cycle))  # 使用迭代器的下一个密钥
print("Decrypted Message:", decrypted_message)
