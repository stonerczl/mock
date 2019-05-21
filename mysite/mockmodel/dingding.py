import requests
import json
import random


def doPost(url, params):
    headers = {"Content-Type": "application/json;charset=utf-8"}
    response = requests.post(url, data=json.dumps(params), headers=headers)
    return json.loads(response.text)


def random_person():
    name = ['15398088151', '17621068954', '18326948099', '15136252363']
    random_name = random.sample(name, 1)[0]
    return random_name


def order_dinner():
    random_name = random_person()
    url = 'https://oapi.dingtalk.com/robot/send?access_token=2193be7a742d556b240e07f57971c96c8ab99e77cc1b2f823e2d9cc53428738f'
    content = "(测试一下)今天随机到你@" + random_name + "帮忙给大家拿饭，谢谢啦！"
    params = {
                "msgtype": "text",
                "text": {
                        "content": content
                        },
                "at": {
                    "atMobiles": [random_name],
                        "isAtAll": False
                        }
                }
    resp_str = doPost(url, params)
    return resp_str

def booking_dinner():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=2193be7a742d556b240e07f57971c96c8ab99e77cc1b2f823e2d9cc53428738f'
    content = "https://blackfish.jinshuju.com/f/53HDTq 订餐提醒"
    params = {
                "msgtype": "text",
                "text": {
                        "content": content
                        },
                "at": {
                    "atMobiles": [],
                        "isAtAll": True
                        }
                }
    resp_str = doPost(url, params)
    return resp_str


if __name__ == '__main__':
    order_dinner()