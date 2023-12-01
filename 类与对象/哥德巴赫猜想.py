import math

# 判断是否为素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 获取素数列表
def get_prime_list(limit):
    prime_list = []
    for i in range(2, limit):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

# 验证哥德巴赫猜想
def verify_goldbach_conjecture(num):
    if num <= 6 or num % 2 != 0:
        return False
    prime_list = get_prime_list(num)
    for prime in prime_list:
        if is_prime(num - prime):
            return True
    return False

# 模块化方式测试
if __name__=="__main__":
    test_numbers = [8, 10, 12, 14, 16, 18, 20]
    for number in test_numbers:
        if verify_goldbach_conjecture(number):
            print(f"{number} 可以被表示为两个素数之和")
        else:
            print(f"{number} 不能被表示为两个素数之和")
