import hashlib
from common import TimeHandler

def sign(order_id, timestamp, token):
    order_id = order_id
    timestamp = timestamp
    token = token
    zhenghe = order_id + timestamp + token
    # 创建md5对象
    m2 = hashlib.md5()
    # 生成加密字符串
    m2.update(zhenghe.encode("utf8"))
    # 获取加密后的字符串
    return m2.hexdigest()


if __name__ == '__main__':
    timestamp = 1551166666592
    token = 'bc4998016bb2df0764e8f247847509fa'
    result = sign('201902271409470328', str(timestamp), token)
    print(result)