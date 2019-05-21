import requests,base64,json
from threading import Thread
from time import sleep
from mock import Mock
from common.LoggingOutput import MyLog

def async1(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper

# book
@async1
def callback(data,callbackurl):
    sleep(2)
    data = json.dumps(data,ensure_ascii=False)

    data_str = ("data=" + data).encode("utf-8")
    print("模拟回调:%s" % data_str)
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    r = requests.post(callbackurl, data=data_str, headers = headers)
   # res = base64.b64decode(r.text).decode('utf8')
    res = r.text
    print("回调结果：%s" % res)
    # return res
# confirm
@async1
def confirmcallback(data,callbackurl):
    sleep(2)
    print(type(data))
    data_str = data.encode("utf-8")
    print("模拟回调:%s" % data_str)
    r = requests.post(callbackurl, data=data_str)
   # res = base64.b64decode(r.text).decode('utf8')
    res = r.text
    print("回调结果：%s" % res)
# train_request_change
@async1
def callback2(data,callbackurl):
    sleep(2)
    data = json.dumps(data,ensure_ascii=False)
    data_str = ("backjson=" + data).encode("utf-8")
    print("模拟回调:%s" % data_str)
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    r = requests.post(callbackurl, data=data_str, headers = headers)
   # res = base64.b64decode(r.text).decode('utf8')
    res = r.text
    print("回调结果：%s" % res)

@async1
def paycallback(data,callbackurl):
    sleep(2)
    data = json.dumps(data,ensure_ascii=False)
    data_str = data.encode("utf-8")
    print("模拟回调:%s" % data_str)
    headers = {"Content-Type":"application/json"}
    r = requests.post(callbackurl, data=data_str, headers = headers)
    res = r.text
    print("回调结果：%s" % res)


#  模拟供应商状态变更--企业管家
def doPostcallback(url, params):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=params, headers = headers)
    response = base64.b64decode(response.text).decode('utf8')
    return json.loads(response)

# 异步模拟调用发起供应商接单通知--企业管家
@async1
def doPostcallback_async1(url, params):
    print("15秒后接单~~~")
    sleep(15)
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=params, headers=headers)
    response = base64.b64decode(response.text).decode('utf8')
    print("回调结果：%s" % response)




#  模拟供应商状态变更--智行
def doPostcallback2(url, params):
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=params, headers = headers)
    response = response.text
    return json.loads(response)

# 异步模拟调用发起供应商接单通知--智行
@async1
def doPostcallback_async2(url, params):
    print("15秒后接单~~~")
    sleep(15)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=params, headers=headers)
    response = response.text
    print("回调结果：%s" % response)