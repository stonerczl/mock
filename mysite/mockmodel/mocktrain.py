# from . import models
from mock import Mock
import json
import time
import random
from common.TimeHandler import clear_time,req_time,time_stamp,mockcar_bookingtime_zhixing
from common.OrderidHandler import trainorderid

# 样例
# def ora_mock_queryHotelLowestPrice(request_data):
#     # 字符串转json  str-->dict
#     request_json = json.loads(request_data)
#     # 根据请求报文,处理响应结果
#     hotelIds = request_json['businessRequest']['hotelIds'][0]
#     response_data = models.Mocktest.objects.filter(server="has").values("response_body")[0]['response_body']
#     # 会使用JsonResponse，必须为字典类型
#     response_json=json.loads(response_data)
#     # 设置响应延时
#     time.sleep(1)
#     mock_method = Mock(return_value=response_json)
#     return mock_method()

# 火车票查询mock 平凉-->平凉南 1.4
def mock_trainsearch(request_json):
    hotcity_train = {"BJP":"北京","SHH":"上海","GZQ":"广州","SZQ":"深圳","CDW":"成都","HZH":"杭州","WHN":"武汉","XAY":"西安","QDK":"青岛","CSQ":"长沙","NJH":"南京","XMS":"厦门","KMM":"昆明","DLT":"大连","TJP":"天津"}
    print("收到请求:%s" % request_json)
    train_date = request_json['train_date']
    from_station = request_json['from_station']
    to_station = request_json['to_station']
    if to_station in hotcity_train.keys() and from_station in hotcity_train.keys():
        to_station_name = hotcity_train[to_station]
        from_station_name = hotcity_train[from_station]
    else:
        from_station = "SHH"
        to_station = "BJP"
        to_station_name = "北京"
        from_station_name = "上海"
    searchekey = from_station + to_station + train_date
    response_json = {
                      "success": True,
                      "code": 200,
                      "searchkey": searchekey,
                      "msg": "正常获得结果",
                      "data": [
                        {
                          "rwx_price": 0,
                          "end_station_name": "宝鸡",
                          "swz_price": 0,
                          "swz_num": "--",
                          "to_station_name": to_station_name,
                          "ydz_num": "--",
                          "yz_num": "184",
                          "rw_num": "--",
                          "arrive_days": "0",
                          "rz_num": "--",
                          "access_byidcard": "0",
                          "yz_price": 1,
                          "ywz_price": 0,
                          "dw_price": 0,
                          "from_station_code": from_station,
                          "rz_price": 0,
                          "gjrw_num": "--",
                          "to_station_code": to_station,
                          "ydz_price": 0,
                          "wz_price": 1,
                          "tdz_price": 0,
                          "run_time": "00:15",
                          "dwx_price": 0,
                          "yw_num": "--",
                          "distance": 0,
                          "edz_price": 0,
                          "qtxb_price": 0,
                          "can_buy_now": "Y",
                          "yw_price": 0,
                          "train_type": "6",
                          "rw_price": 0,
                          "train_code": "6074",
                          "train_no": "870000607404",
                          "note": "",
                          "from_station_name": from_station_name,
                          "run_time_minute": "15",
                          "ywx_price": 0,
                          "dw_num": "--",
                          "gjrws_price": 0,
                          "arrive_time": "13:25",
                          "start_station_name": "平凉",
                          "start_time": "13:10",
                          "wz_num": "668",
                          "edz_num": "--",
                          "qtxb_num": "--",
                          "gjrw_price": 0,
                          "tdz_num": "--"
                        },
                        {
                          "rwx_price": 0,
                          "end_station_name": "长庆桥",
                          "swz_price": 0,
                          "swz_num": "--",
                          "to_station_name": to_station_name,
                          "ydz_num": "--",
                          "yz_num": "0",
                          "rw_num": "--",
                          "arrive_days": "0",
                          "rz_num": "--",
                          "access_byidcard": "0",
                          "yz_price": 4,
                          "ywz_price": 0,
                          "dw_price": 0,
                          "from_station_code": from_station,
                          "rz_price": 0,
                          "gjrw_num": "--",
                          "to_station_code": to_station,
                          "ydz_price": 0,
                          "wz_price": 4,
                          "tdz_price": 0,
                          "run_time": "00:15",
                          "dwx_price": 0,
                          "yw_num": "--",
                          "distance": 0,
                          "edz_price": 0,
                          "qtxb_price": 0,
                          "can_buy_now": "N",
                          "yw_price": 0,
                          "train_type": "7",
                          "rw_price": 0,
                          "train_code": "7514",
                          "train_no": "870000751121",
                          "note": "12月21日9点起售",
                          "from_station_name": from_station_name,
                          "run_time_minute": "15",
                          "ywx_price": 0,
                          "dw_num": "--",
                          "gjrws_price": 0,
                          "arrive_time": "17:46",
                          "start_station_name": "银川",
                          "start_time": "17:31",
                          "wz_num": "0",
                          "edz_num": "--",
                          "qtxb_num": "--",
                          "gjrw_price": 0,
                          "tdz_num": "--"
                        }
                      ]
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()


# 火车票订单提交mock
def mock_trainbook(request_json):
    print("收到请求:%s" % request_json)
    passengersename = request_json['passengers'][0]['passengersename']
    if passengersename == "测试夜间":
        transactionid = request_json['orderid']
        response_json = {
            "orderid": transactionid,
            "isNight": True,
            "code": "802",
            "msg": "收单请求已接收",
            "success": True
        }
    else:
        transactionid = "T103316561" + trainorderid(23)
        response_json = {
                      "orderid": transactionid,
                      "code": "802",
                      "msg": "创建订单成功",
                      "success": True
                    }

    checi = request_json['checi']
    from_station_code = request_json['from_station_code']
    from_station_name = request_json['from_station_name']
    orderid = request_json['orderid']
    passengerid = request_json['passengers'][0]['passengerid']
    passengersename = request_json['passengers'][0]['passengersename']
    passportseno = request_json['passengers'][0]['passportseno']
    passporttypeseid = request_json['passengers'][0]['passporttypeseid']
    passporttypeseidname = request_json['passengers'][0]['passporttypeseidname']
    piaotype = request_json['passengers'][0]['piaotype']
    price = request_json['passengers'][0]['price']
    zwcode = request_json['passengers'][0]['zwcode']
    zwname = request_json['passengers'][0]['zwname']
    to_station_code = request_json['to_station_code']
    to_station_name = request_json['to_station_name']
    cleartime = clear_time()
    ordernumber = "F"+orderid[-9:]
    orderamount = str('{:.2f}'.format(float(price)))
    train_date = request_json['train_date']
    start_time = train_date + " 08:51:00"
    arrive_time = train_date + " 09:54:00"
    ticket_no = ordernumber+"1070074"
    callbackurl = request_json['callbackurl']

    response_call = {
                      "reqtoken": "",
                      "clear_time": cleartime,
                      "runtime": "00:03",
                      "ordernumber": ordernumber,
                      "from_station_name": from_station_name,
                      "checi": checi,
                      "code": 100,
                      "msg": "处理或操作成功",
                      "from_station_code": from_station_code,
                      "orderamount": orderamount,
                      "to_station_name": to_station_name,
                      "arrive_time": arrive_time,
                      "passengers": [
                        {
                          "reason": 0,
                          "piaotype": piaotype,
                          "passporttypeseidname": passporttypeseidname,
                          "passporttypeseid": passporttypeseid,
                          "zwname": zwname,
                          "price": price,
                          "piaotypename": "成人票",
                          "ticket_no": ticket_no,
                          "passengersename": passengersename,
                          "zwcode": zwcode,
                          "passportseno": passportseno,
                          "passengerid": passengerid,
                          "cxin": "07车厢,074座"
                        }
                      ],
                      "to_station_code": to_station_code,
                      "accountlist": [
                        {
                          "accountstatusid": 5,
                          "accountstatusname": "其他",
                          "accountname": "0"
                        }
                      ],
                      "train_date": train_date,
                      "ordersuccess": True,
                      "ticket_entrance": "",
                      "transactionid": transactionid,
                      "start_time": start_time,
                      "orderid": orderid,
                      "success": True
                    }

    mock_response = Mock(return_value=response_json)
    mock_call = Mock(return_value=response_call)
    print("返回:%s" % mock_response())
    print("请求处理:%s" % mock_call())
    return mock_response(),mock_call(),callbackurl,passengersename

# 火车票确认出票mock
def mock_trainconfirm(request_json):
    print("收到请求:%s" % request_json)
    orderid = request_json['orderid']
    ordernumber = "F"+orderid[-9:]
    response_json = {
                      "changeserial": "",
                      "ordernumber": ordernumber,
                      "orderid": orderid,
                      "code": "100",
                      "msg": "出票请求已接收",
                      "success": True
                    }

    reqtime=req_time()
    transactionid = request_json['transactionid']
    callbackurl = request_json['callbackurl']
    response_call_str = "reqtime="+reqtime+"&sign=fa2324464675c02d159568011981d173&orderid="+orderid+"&transactionid="+transactionid+"&isSuccess=Y&code=100&msg=%E6%94%AF%E4%BB%98%E6%88%90%E5%8A%9F&ticketEntrances=%5B%7B%22trainNum%22%3A%22G264%22%2C%22stationName%22%3A%22%E5%90%88%E8%82%A5%E5%8D%97%22%2C%22entrance%22%3A%22%E6%A3%80%E7%A5%A8%E5%8F%A321B%22%7D%5D"
    mock_response = Mock(return_value=response_json)
    mock_call = Mock(return_value=response_call_str)
    print("返回:%s" % mock_response())
    print("请求处理:%s" % mock_call())
    return mock_response(),mock_call(),callbackurl

# 火车票取消订单mock
def mock_traincancel(request_json):
    print("收到请求:%s" % request_json)
    orderid = request_json['orderid']
    response_json = {
                      "orderid": orderid,
                      "code": "100",
                      "msg": "取消订单成功",
                      "success": True
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()

# 火车票请求改签mock
def mock_trainchange(request_json):
    print("收到请求:%s" % request_json)
    reqtoken = request_json['reqtoken']
    transactionid = request_json['transactionid']
    orderid = request_json['orderid']
    response_json = {
                      "reqtoken": reqtoken,
                      "help_info": "改签请求已接受",
                      "transactionid": transactionid,
                      "orderid": orderid,
                      "code": "100",
                      "msg": "改签请求已接受",
                      "success": True
                    }
    callbackurl = request_json['callbackurl']
    zwcode = request_json['change_zwcode']
    passportseno = request_json['ticketinfo'][0]['passportseno']
    old_ticket_no = request_json['ticketinfo'][0]['old_ticket_no']
    piaotype = request_json['ticketinfo'][0]['piaotype']
    passengerid = request_json['ticketinfo'][0]['passengerid']
    to_station_name = request_json['to_station_name']
    transactionid = request_json['transactionid']
    from_station_name = request_json['from_station_name']
    change_checi = request_json['change_checi']
    from_station_code = request_json['from_station_code']
    to_station_code = request_json['to_station_code']
    train_date = request_json['change_datetime'].split(" ")[0]
    cleartime = clear_time()
    reqtime = req_time()
    new_ticket_no = "F" + orderid[-9:] + "1070075"
    response_call = {
                      "reqtoken": reqtoken,
                      "runtime": "00:02",
                      "pricedifference": 1.5,
                      "newtickets": [
                        {
                          "zwname": "硬座",
                          "new_ticket_no": new_ticket_no,
                          "price": "12.5",
                          "piaotype": piaotype,
                          "zwcode": zwcode,
                          "passportseno": passportseno,
                          "old_ticket_no": old_ticket_no,
                          "flagmsg": "改签成功",
                          "flagid": "100",
                          "passengerid": passengerid,
                          "cxin": "02车厢,029号"
                        }
                      ],
                      "priceinfotype": 1,
                      "to_station_name": to_station_name,
                      "partnerid": "xiaoheiyuceshi",
                      "help_info": "改签占座成功",
                      "transactionid": transactionid,
                      "priceinfo": "收取新票款：12.5元，退还原票款：11.0元",
                      "diffrate": "0",
                      "clear_time": cleartime,
                      "reqtime": reqtime,
                      "from_station_name": from_station_name,
                      "checi": change_checi,
                      "totalpricediff": 11,
                      "code": "100",
                      "msg": "改签占座成功",
                      "from_station_code": from_station_code,
                      "sign": "d23242087fb281323d07ba5b63c06276",
                      "fee": 0,
                      "arrive_time": "17:26",
                      "to_station_code": to_station_code,
                      "train_date": train_date,
                      "refund_online": 0,
                      "ticket_entrance": "",
                      "start_time": "16:34",
                      "method": "train_request_change",
                      "orderid": orderid,
                      "success": True
                    }
    mock_response = Mock(return_value=response_json)
    mock_call = Mock(return_value=response_call)
    print("返回:%s" % mock_response())
    print("请求处理:%s" % mock_call())
    return mock_response(), mock_call(), callbackurl

# 火车票取消改签mock
def mock_traincancelchange(request_json):
    print("收到请求:%s" % request_json)
    orderid = request_json['orderid']
    transactionid = request_json['transactionid']
    response_json = {
                      "changeTickets": [
                        {
                          "passengerid": "5354"
                        }
                      ],
                      "transactionid": transactionid,
                      "code": "100",
                      "orderid": orderid,
                      "msg": "取消改签成功",
                      "success": True
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()

# 火车票确认改签mock
def mock_trainconfirmchange(request_json):
    print("收到请求:%s" % request_json)
    reqtoken = request_json['reqtoken']
    transactionid = request_json['transactionid']
    orderid = request_json['orderid']
    response_json = {
                      "reqtoken": reqtoken,
                      "transactionid": transactionid,
                      "orderid": orderid,
                      "code": "100",
                      "msg": "确认请求已接受",
                      "success": True
                    }
    callbackurl = request_json['callbackurl']
    reqtime = req_time()
    old_ticket_no = "F" + orderid[-9:] + "1070074"
    new_ticket_no = "F" + orderid[-9:] + "1070075"
    response_call = {
                      "sign": "ba9248094ba7cf22c7951b3b966f083c",
                      "partnerid": "xiaoheiyuceshi",
                      "reqtoken": reqtoken,
                      "oldticketchangeserial": "",
                      "ticket_entrance": "",
                      "reqtime": reqtime,
                      "ticketpricediffchangeserial": "",
                      "newticketcxins": [
                        {
                          "new_ticket_no": new_ticket_no,
                          "old_ticket_no": old_ticket_no,
                          "cxin": "02车厢,029号"
                        }
                      ],
                      "method": "train_confirm_change",
                      "orderid": orderid,
                      "newticketchangeserial": "",
                      "code": "100",
                      "msg": "确认改签成功",
                      "success": True
                    }
    mock_response = Mock(return_value=response_json)
    mock_call = Mock(return_value=response_call)
    print("返回:%s" % mock_response())
    print("请求处理:%s" % mock_call())
    return mock_response(), mock_call(), callbackurl

# 火车票预支付mock
def mock_trainprepay(request_json):
    print("收到请求:%s" % request_json)
    clearTime = time_stamp()
    prePayOrderId = str(clearTime)[-8:]
    response_json = {
                    "success": True,
                    "msg": "操作成功",
                    "errorCode": 0,
                    "data": {
                    "prePayOrderId": prePayOrderId,
                    "clearTime": clearTime,
                    "cashierUrl": "pay.blackfish.cn"
                    }
                    }
    paidAmount = str(request_json['paiedAmount'])
    bizOrderId = request_json['bizOrderId']
    successPaidTime = clearTime + 2000
    bizId = request_json['bizId']
    callbackurl = "http://10.33.16.13:10914/tos/PaymentApi/payResultCallback"  #替换性能IP
    response_call = {
                    "outTradeNo": "10160005362210418110168460007850",
                    "methodCode": 1,
                    "paidAmount": paidAmount,
                    "offsetAmount": "0.00",
                    "bizOrderId": bizOrderId,
                    "successPaidTime": successPaidTime,
                    "bizId": bizId,
                    "payChannel": 119,
                    "parternerId": "100000276",
                    "status": "S",
                    "channelSerialNo": None,
                    "cardId": 453240
                    }
    mock_response = Mock(return_value=response_json)
    mock_call = Mock(return_value=response_call)
    print("返回:%s" % mock_response())
    print("请求处理:%s" % mock_call())
    return mock_response(), mock_call(), callbackurl

# 火车票抢票mock
def mock_qiangpiaoorder(request_json):
    print("收到请求:%s" % request_json)
    transactionid = "T103316561" + trainorderid(23)
    response_json = {
                      "orderid": transactionid,
                      "code": "100",
                      "msg": "业务参数已获取",
                      "success": True
                    }

    train_codes = request_json['train_codes'].split(",")[0]
    from_station_code = request_json['from_station_code']
    from_station_name = request_json['from_station_name']
    orderid = request_json['qorderid']
    passengerid = request_json['passengers'][0]['passengerid']
    passengersename = request_json['passengers'][0]['passengersename']
    passportseno = request_json['passengers'][0]['passportseno']
    passporttypeseid = request_json['passengers'][0]['passporttypeseid']
    passporttypeseidname = request_json['passengers'][0]['passporttypeidname']
    piaotype = request_json['passengers'][0]['piaotype']
    #price = request_json['passengers'][0]['price']
    #zwcode = request_json['passengers'][0]['zwcode']
    #zwname = request_json['passengers'][0]['zwname']
    to_station_code = request_json['to_station_code']
    to_station_name = request_json['to_station_name']
    #cleartime = clear_time()
    ordernumber = "EH"+orderid[-8:]
    #orderamount = str('{:.2f}'.format(float(price)))
    train_date_temp = request_json['start_date']
    train_date = train_date_temp[0:4]+"-"+train_date_temp[4:6]+"-"+train_date_temp[6:8]
    start_time_temp = request_json['start_begin_time']
    start_time = train_date + " "+start_time_temp+":00"
    arrive_time_temp = request_json['start_end_time']
    arrive_time = train_date + " "+arrive_time_temp+":00"
    ticket_no = ordernumber+"1070074"
    callbackurl = request_json['callback_url']
    # 正常回调
    response_call = {
                      "reqtoken": "",
                   #   "clear_time": cleartime,
                      "runtime": "00:03",
                      "ordernumber": ordernumber,
                      "from_station_name": from_station_name,
                      "checi": train_codes,
                      "code": 100,
                      "msg": "处理或操作成功",
                      "from_station_code": from_station_code,
                      "orderamount": "1.0",
                      "to_station_name": to_station_name,
                      "arrive_time": arrive_time,
                      "passengers": [
                        {
                          "reason": 0,
                          "piaotype": piaotype,
                          "passporttypeseidname": passporttypeseidname,
                          "passporttypeseid": passporttypeseid,
                          "zwname": "硬座",
                          "price": "1.0",
                          "piaotypename": "成人票",
                          "ticket_no": ticket_no,
                          "passengersename": passengersename,
                          "zwcode": "1",
                          "passportseno": passportseno,
                          "passengerid": passengerid,
                          "cxin": "07车厢,074座"
                        }
                      ],
                      "to_station_code": to_station_code,
                      "accountlist": [
                        {
                          "accountstatusid": 5,
                          "accountstatusname": "其他",
                          "accountname": "0"
                        }
                      ],
                      "train_date": train_date,
                      "refund_online": "0",
                      "ordersuccess": True,
                      "ticket_entrance": "",
                      "transactionid": transactionid,
                      "start_time": start_time,
                      "orderid": orderid,
                      "success": True
                    }
    # 异常回调
    # response_call = {
    #                     "Msg": "没有足够的票",
    #                     "orderid": orderid,
    #                     "success": False,
    #                     "AgentId": 181
    #                 }
    mock_response = Mock(return_value=response_json)
    mock_call = Mock(return_value=response_call)
    print("返回:%s" % mock_response())
    print("请求处理:%s" % mock_call())
    return mock_response(),mock_call(),callbackurl

# 火车票取消抢票mock
def mock_qiangpiaocancel(request_json):
    print("收到请求:%s" % request_json)
    orderid = request_json['qorderid']
    response_json = {
                        "msg": "订单取消成功",
                        "code": "100",
                        "isSuccess":True
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()

# 火车票夜间取消mock
def mock_nightcancel(request_json):
    print("收到请求:%s" % request_json)
    # orderid = request_json['qorderid']
    response_json = {
                    "code":600,
                     "msg":"夜间单取消成功",
                     "success":True
                     }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()

# 火车票退票mock
def mock_returnticket(request_json):
    print("收到请求:%s" % request_json)
    reqtoken = request_json['reqtoken']
    ordernumber = request_json['ordernumber']
    orderid = request_json['orderid']
    response_json = {
                      "reqtoken": reqtoken,
                      "ordernumber": ordernumber,
                      "orderid": orderid,
                      "code": "802",
                      "msg": "退票请求已接收",
                      "success": True,
                      "tooltip": "退票请求已接收，正在处理"
                    }

    passengername = request_json['tickets'][0]['passengername']
    ticket_no = request_json['tickets'][0]['ticket_no']
    passportseno = request_json['tickets'][0]['passportseno']
    passporttypeseid = request_json['tickets'][0]['passporttypeseid']
    callbackurl = request_json['callbackurl']
    response_call = {
                        "timestamp": "147441607",
                        "sign": "03b4daa84784708d546b3fc356485df",
                        "reqtoken": reqtoken,
                        "returntickets": [
                            {
                                "returnsuccess": True,
                                "returnfailid": "",
                                "passengername": passengername,
                                "ticket_no": ticket_no,
                                "returnmoney": "1000",
                                "returnfailmsg": "",
                                "passportseno": passportseno,
                                "passporttypeseid": passporttypeseid,
                                "returntime": mockcar_bookingtime_zhixing()
                            }
                        ],
                        "apiorderid": orderid,
                        "token": reqtoken,
                        "returnmoney": "1000",
                        "trainorderid": ticket_no,
                        "returnmsg": "",
                        "returnstate": True,
                        "returntype": "1"
                    }
    mock_response = Mock(return_value=response_json)
    mock_call = Mock(return_value=response_call)
    print("返回:%s" % mock_response())
    print("请求处理:%s" % mock_call())
    return mock_response(),mock_call(),callbackurl





if __name__ == '__main__':
    # res = mock_queryHotelLowestPrice(
    #     '{"businessRequest":{ "hotelIds":[ 179440, 198180 ] }, "header":{ "partnerCode":"P10000001", "requestType":"queryHotelLowestPrice", "timestamp":1511866697711, "signature":"D688B356FD982227E505586C74E06B50", "version":"1.0.0" }}')
    data = '{"callbackurl":"http://180.169.94.19/oai/hthyTrainCb/bookTrain","checi":"K290","from_station_code":"SHH","from_station_name":"上海","is_accept_standing":false,"method":"train_order","orderid":"1016201811051417596561101191295","partnerid":"xiaoheiyuceshi",' \
           '"passengers":[{"passengerid":"5455","passengersename":"王思凯","passportseno":"H12360089","passporttypeseid":"C","passporttypeseidname":"港澳通行证","piaotype":"1","price":14.5,"zwcode":"1","zwname":"硬座"}],' \
           '"reqtime":"20181105141759","sign":"8af6a0cbbabf838992a202eeaf116663","to_station_code":"SZH","to_station_name":"苏州","train_date":"2018-11-28"}'
    res = mock_trainbook(data)
