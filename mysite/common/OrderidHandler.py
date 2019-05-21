import random

def trainorderid(num):
    list = [chr(i) for i in range(65,91)]+[ str(i) for i in range(10)]
    num = random.sample(list, num)
    str1 = ''
    value = str1.join(num)
    return value

if __name__ == '__main__':
    trainorderid(5)