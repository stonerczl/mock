from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import mocktrain,mockcar
import json,time,random,re
from common.RequestHandler import callback,confirmcallback,callback2,paycallback,doPostcallback,doPostcallback_async1,doPostcallback_async2,doPostcallback2
from common.Connectmysql import mysql_query
from common.LoggingOutput import MyLog
from common import MD5Handler,TimeHandler

# Create your views here.
# 样例
# def queryHotelLowestPrice1(request):
#     supplier,server = url_deal.url_split(request.path)
#     response_url= models.Mocktest.objects.filter(url=server)
#     #print(response_url)
#     #try:
#     if request.method == "POST":
#         request_data = request.body.decode()
#         #print(request_data)
#         res = mocktrain.ora_mock_queryHotelLowestPrice(request_data)
#         print(res)
#         return JsonResponse(res, safe=False)
#     # except:
#     #     return HttpResponse("无该url，请检查！")

# 火车业务mock
# 航天——询价
def trainsupplier_search(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        res = mocktrain.mock_trainsearch(request_json)
        # return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
        response = HttpResponse(json.dumps(res,ensure_ascii=False), content_type="text/html", charset="UTF-8")
        # response['connection'] = 'close'
        # print(HttpResponse.has_header(header=content_))
        return response
# 航天——业务，根据接口中method值判断
def trainsupplier(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        print("用户请求:%s" % request_json)
        mocklog = '{}请求，内容：{}'.format(request_json['method'], request_json)
        MyLog.info(mocklog)
        if request_json['method'] == "train_order":
            # 火车票订单提交（占座申请）
            res, res_call, callbackurl, passengersename= mocktrain.mock_trainbook(request_json)
            # 夜间票
            if passengersename != "测试夜间":
            # 订单提交回调（占座结果回调）,等待2秒异步处理
                callback(res_call, callbackurl)
        elif request_json['method'] == "train_confirm":
            # 确认出票接口
            res, res_call, callbackurl = mocktrain.mock_trainconfirm(request_json)
            # 确认出票回调接口,等待2秒异步处理
            confirmcallback(res_call, callbackurl)
        elif request_json['method'] == "train_cancel":
            # 取消订单接口
            res = mocktrain.mock_traincancel(request_json)
        elif request_json['method'] == "train_request_change":
            # 火车票请求改签接口
            res, res_call, callbackurl = mocktrain.mock_trainchange(request_json)
            # 改签占座回调接口,等待2秒异步处理
            callback2(res_call, callbackurl)
        elif request_json['method'] == "train_cancel_change":
            # 取消改签接口
            res = mocktrain.mock_traincancelchange(request_json)
        elif request_json['method'] == "train_confirm_change":
            # 火车票确认改签接口
            res, res_call, callbackurl = mocktrain.mock_trainconfirmchange(request_json)
            # 改签占座回调接口,等待2秒异步处理
            callback2(res_call, callbackurl)
        elif request_json['method'] == 'qiang_piao_order':
            # 抢票下单
            res, res_call, callbackurl = mocktrain.mock_qiangpiaoorder(request_json)
            # 异步回调,等待2秒异步处理
            callback(res_call, callbackurl)
        elif request_json['method'] == '':
            # 取消抢票
            res = mocktrain.mock_qiangpiaocancel(request_json)
        elif request_json['method'] == 'train_night_cancel':
            # 取消夜间票
            res = mocktrain.mock_nightcancel(request_json)
        elif request_json['method'] == 'return_ticket':
            # 退票
            res, res_call, callbackurl = mocktrain.mock_returnticket(request_json)
            # 异步回调,等待2秒异步处理
            callback(res_call, callbackurl)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii':False})
# 支付
def trainprepay(request):
    if request.method == "POST":
        request_data = request.body.decode()
        request_json = json.loads(request_data)
        print("用户请求:%s" % request_json)
        res, res_call, callbackurl = mocktrain.mock_trainprepay(request_json)
        paycallback(res_call, callbackurl)
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 极淼——询价
def train_search_jimiao(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        res = mocktrain.mock_trainsearch(request_json)
        # return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
        response = HttpResponse(json.dumps(res,ensure_ascii=False), content_type="text/html", charset="UTF-8")
        return response
# 极淼——订票
def train_book_jimiao(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        print("用户请求:%s" % request_json)
        mocklog = '{}请求，内容：{}'.format(request_json['method'], request_json)
        MyLog.info(mocklog)
        # 火车票订单提交（占座申请）
        res, res_call, callbackurl, passengersename = mocktrain.mock_trainbook(request_json)
        # 夜间票
        if passengersename != "测试夜间":
            # 订单提交回调（占座结果回调）,等待2秒异步处理
            callback(res_call, callbackurl)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 极淼——取消
def train_cancel_jimiao(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        res = mocktrain.mock_traincancel(request_json)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 极淼——确认出票
def train_confirm_jimiao(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        res, res_call, callbackurl = mocktrain.mock_trainconfirm(request_json)
        # 确认出票回调接口,等待2秒异步处理
        callback(res_call, callbackurl)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 极淼——退票
def train_returnTicket_jimiao(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        res, res_call, callbackurl = mocktrain.mock_returnticket(request_json)
        # 异步回调,等待2秒异步处理
        callback(res_call, callbackurl)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 极淼——取消改签
def train_cancleChange_jimiao(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        res = mocktrain.mock_traincancelchange(request_json)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 极淼——确认改签
def train_confirmChange_jimiao(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        res, res_call, callbackurl = mocktrain.mock_trainconfirmchange(request_json)
        # 改签占座回调接口,等待2秒异步处理
        callback(res_call, callbackurl)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 极淼——请求改签
def train_requestChange_jimiao(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        res, res_call, callbackurl = mocktrain.mock_trainchange(request_json)
        # 改签占座回调接口,等待2秒异步处理
        callback(res_call, callbackurl)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 极淼——取消夜间票
def train_nightCancle_jimiao(request):
    if request.method == "POST":
        request_data = request.body.decode()
        # 字符串转json  str-->dict
        request_json = json.loads(request_data[8:])
        res = mocktrain.mock_nightcancel(request_json)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})







# 打车业务mock
# 公共参数
cars = {}
car_param = {"out_source_no":"1125902188720645","cap_uid":"102420190117174818994331655000","dlat":30.982883111,"dlng":121.23012111,"strive_time":"2019-01-16 09:27:36",'passenger_clat':30.982883111,'passenger_clng':121.23012111,"booking_time":"2019-01-16 09:27:36"}
counter = {"num":0, "wait":3, "arrive":6, "drive":9}

# 企业管家
# 企业管家——滴滴安全业务
def car_passenger(cas_orderDetail_url, business_order_id):
    # 关联滴滴业务，passenger位置
    global cars
    passenger = cas_orderDetail_url
    pattern_clat = re.compile('passenger_clat=([\s\S]*?)&passenger_clng')
    passenger_clat = re.findall(pattern_clat, passenger)[0]
    pattern_clng = re.compile('&passenger_clng=(.*)')
    passenger_clng = re.findall(pattern_clng, passenger)[0]
    emergency_help_url = "https://page.udache.com/public-biz/call-alarm/index.html?openid=MTAwMDUwMDE4bcJmAO4A4pY66Az07pDxjBY%2BHQM%3D&third_token=6B1610B4168BAA945C9D6416E4A958147F278AAD9954CD99CEFF88F553316D67D019DC48396795EA65E6DB4DF63A6AD4A90FE6A3950241BE00BFEB7D388952FA&webapp_channel=es_openapi&product=258&appid=52015&oid=TWpnNE56SXpNRFEzTnpRME1qYzRNRGsy"
    emergency_help_url = emergency_help_url + "&lat=" + passenger_clat + "&lng=" + passenger_clng
    cars[business_order_id]['passenger_clat'] = passenger_clat
    cars[business_order_id]['passenger_clng'] = passenger_clng
    cars[business_order_id]['emergency_help_url'] = emergency_help_url

# 企业管家——下单
def carsuppliercreate(request):
    global cars
    if request.method == "POST":
        # ran_num可以模拟下单超时
        ran_num = random.randint(1, 2)
        time.sleep(ran_num)
        request_create_body = request.body.decode()
        request_create_body = json.loads(request_create_body)
        source = request_create_body['source']
        if request_create_body['source'] == 'didi' and request_create_body['app_version'] == '1.0.0':
            # 模拟didi授权录音
            res = mockcar.mock_create_ex(source)
        else:
            res = mockcar.mock_create(source)
            # business_order_id字段
            no = res['data']['no']
            cars[no] = {"out_source_no":"1125902188720645","cap_uid":"102420190117174818994331655000","dlat":30.982883111,"dlng":121.23012111,"strive_time":"2019-01-16 09:27:36",'passenger_clat':30.982883111,'passenger_clng':121.23012111,"booking_time":"2019-01-16 09:27:36"}
            # 模拟供应商触发回调
            cars[no]['out_source_no'] = res['data']['out_source_no']
            cars[no]['cap_uid'] = request_create_body['capId']
            cars[no]['source'] = request_create_body['source']
            url = 'http://10.33.16.55:10950/cas/callback/eh/state/notice'
            params = 'no=' + no + '&out_source_no=' + cars[no]['out_source_no'] + '&state=' + ''
            counter[no] = 0
            doPostcallback_async1(url, params)
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})

# 企业管家
# 订单详情、取消、询价等
def carsupplier(request):
    global cars,counter
    url_path = request.get_full_path().split('/')
    print(url_path)
    if request.method == "GET":

        if len(url_path) == 5 and url_path[4].split('?')[0] == 'cancel':
            business_order_id_cancel = url_path[3].split('?')[0]
            # 违约金判断
            if counter[business_order_id_cancel] == 0:
                res = mockcar.mock_carcannel1()
            else:
                res = mockcar.mock_carcannel()
            if business_order_id_cancel in cars.keys():
                del cars[business_order_id_cancel]
                del counter[business_order_id_cancel]
        elif len(url_path) == 4 and url_path[3].split('?')[0] == 'BO07330273260319902':
            business_order_id_no = url_path[3].split('?')[0]
            # 此处模拟供应商取消
            print("----------------cancel-----------------")
            res = mockcar.mock_carcannel_supplier(business_order_id_no, cars[business_order_id_no])
            # 此处模拟超时
            # print("----------------timeout-----------------")
            # res = mockcar.mock_cartimeout(business_order_id_no, cars[business_order_id_no])
        elif len(url_path) == 4 and url_path[3].split('?')[0] in cars.keys():
        # elif len(url_path) == 4 and url_path[3].split('?')[0] == 'BO04284368100366609':
            business_order_id = url_path[3].split('?')[0]
            print("%s的carparam参数：%s" % (business_order_id, cars[business_order_id]))
            print("调用第%d次" % counter[business_order_id])
            mocklog = '{}的carparam参数：{}，调用第{}次'.format(business_order_id, cars[business_order_id], counter[business_order_id])
            MyLog.info(mocklog)

            url = 'http://10.33.16.55:10950/cas/callback/eh/state/notice'
            params = 'no=' + business_order_id + '&out_source_no=' + cars[business_order_id]['out_source_no'] + '&state=' + ''

            if counter[business_order_id] >= 0 and counter[business_order_id] <= counter['wait'] :
            # if counter[business_order_id] >= 0 :
                car_passenger(url_path[3].split('?')[1], business_order_id)
                print("----------------wait-----------------")
                cars[business_order_id]["dlat"] += 0.03
                cars[business_order_id]["dlng"] += 0.03
                # res = mockcar.mock_carcannel_supplier(business_order_id, cars[business_order_id])   # 模拟供应商主动取消
                res, strive_time = mockcar.mock_carwait_ex(business_order_id, cars[business_order_id])
                cars[business_order_id]['strive_time'] = strive_time
                counter[business_order_id] += 1
            elif counter[business_order_id] == counter['wait']+1:
                car_passenger(url_path[3].split('?')[1], business_order_id)
                print("----------------arrive-----------------")
                res = mockcar.mock_cararrive(business_order_id, cars[business_order_id])
                doPostcallback(url, params)
                counter[business_order_id] += 1
            # if counter[business_order_id] >= 0 and counter[business_order_id] <= 16:
            # elif counter[business_order_id] >= 12:
            elif counter[business_order_id] >= counter['wait']+2 and counter[business_order_id] <= counter['arrive'] :
                car_passenger(url_path[3].split('?')[1], business_order_id)
                print("----------------arrive-----------------")
                res = mockcar.mock_cararrive(business_order_id, cars[business_order_id])
                counter[business_order_id] += 1
            elif counter[business_order_id] == counter['arrive']+1:
                car_passenger(url_path[3].split('?')[1], business_order_id)
                print("----------------drive-----------------")
                res, begin_charge_time = mockcar.mock_cardrive(business_order_id, cars[business_order_id])
                cars[business_order_id]['begin_charge_time'] = begin_charge_time
                doPostcallback(url, params)
                counter[business_order_id] += 1
            # if counter[business_order_id] >= 0 and counter[business_order_id] <= 27:
            elif counter[business_order_id] >= counter['arrive']+2 and counter[business_order_id] <= counter['drive']:
                car_passenger(url_path[3].split('?')[1], business_order_id)
                print("----------------drive-----------------")
                cars[business_order_id]["dlat"] -= 0.03
                cars[business_order_id]["dlng"] -= 0.03
                res, begin_charge_time = mockcar.mock_cardrive(business_order_id, cars[business_order_id])
                counter[business_order_id] += 1
            # 非嘀嗒——待支付
            elif counter[business_order_id] == counter['drive']+1 and cars[business_order_id]["source"] != 'dida':
                car_passenger(url_path[3].split('?')[1], business_order_id)
                print("----------------prepay-----------------")
                res, finish_time = mockcar.mock_carprepay(business_order_id, cars[business_order_id])
                cars[business_order_id]['finish_time'] = finish_time
                doPostcallback(url, params)
                counter[business_order_id] += 1
            elif counter[business_order_id] == counter['drive']+2 and cars[business_order_id]["source"] != 'dida':
                car_passenger(url_path[3].split('?')[1], business_order_id)
                print("----------------prepay-----------------")
                res = mockcar.mock_carprepay1(business_order_id, cars[business_order_id])
                counter[business_order_id] += 1
            elif counter[business_order_id] > counter['drive']+2 and cars[business_order_id]["source"] != 'dida':
                car_passenger(url_path[3].split('?')[1], business_order_id)
                # res, begin_charge_time = mockcar.mock_cardrive(business_order_id, cars[business_order_id])
                res = mockcar.mock_carprepay1(business_order_id, cars[business_order_id])
                # res = mockcar.mock_carcompleted_online(business_order_id, cars[business_order_id])
                # 检查状态state = '6'清空内存数据
                sql = "select state from car_child_order where business_order_id = '" + business_order_id + "'"
                if mysql_query(sql, 'car')[0] in ['6', '8', '9', '10', '11'] or mysql_query(sql, 'car')[0] == '':
                    del cars[business_order_id]
                    del counter[business_order_id]
            # 嘀嗒（线上、线下支付）
            elif counter[business_order_id] == counter['drive']+1 and cars[business_order_id]["source"] == 'dida':
                car_passenger(url_path[3].split('?')[1], business_order_id)
                print("----------------completed_underline-----------------")
                res, finish_time = mockcar.mock_carcompleted_underline(business_order_id, cars[business_order_id])
                # res, finish_time = mockcar.mock_carcompleted_online(business_order_id, cars[business_order_id])
                cars[business_order_id]['finish_time'] = finish_time
                doPostcallback(url, params)
                counter[business_order_id] += 1
            elif counter[business_order_id] == counter['drive']+2 and cars[business_order_id]["source"] == 'dida':
                car_passenger(url_path[3].split('?')[1], business_order_id)
                print("----------------completed_underline-----------------")
                res = mockcar.mock_carcompleted_underline1(business_order_id, cars[business_order_id])
                # res = mockcar.mock_carcompleted_online1(business_order_id, cars[business_order_id])
                counter[business_order_id] += 1
            elif counter[business_order_id] > counter['drive']+2 and cars[business_order_id]["source"] == 'dida':
                car_passenger(url_path[3].split('?')[1], business_order_id)
                res = mockcar.mock_carcompleted_underline1(business_order_id, cars[business_order_id])
                # res = mockcar.mock_carcompleted_online1(business_order_id, cars[business_order_id])
                # 检查状态state = '6'清空内存数据
                sql = "select state from car_child_order where business_order_id = '" + business_order_id + "'"
                if mysql_query(sql, 'car')[0] in ['6', '8', '9', '10', '11'] or mysql_query(sql, 'car')[0] == '':
                    del cars[business_order_id]
                    del counter[business_order_id]

            mocklog1 = '{}返回，内容：{}'.format(business_order_id, res)
            MyLog.info(mocklog1)
        elif len(url_path) == 4 and url_path[3].split('?')[0] == 'city_price':
            res = mockcar.mock_carcityprice()
        elif len(url_path) == 4 and url_path[3].split('?')[0] == 'estimate_price':
            res = mockcar.mock_carestimateprice()
        elif len(url_path) == 4:
            business_order_id = url_path[3].split('?')[0]
            print("other orderid")
            res = mockcar.mock_carelse(business_order_id,car_param)
        else:
            res = {"code":"9999"}

    else:
        if len(url_path) == 5 and url_path[4].split('?')[0] == 'pay':
            business_order_id_cancel = url_path[3].split('?')[0]
            res = mockcar.mock_carpay()
            if business_order_id_cancel in cars.keys():
                del cars[business_order_id_cancel]
                del counter[business_order_id_cancel]

    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})


# 智行
# 智行——下单
def carsuppliercreate_zhixing(request):
    global cars
    if request.method == "POST":
        # ran_num可以模拟下单超时
        ran_num = random.randint(1, 4)
        time.sleep(ran_num)
        request_create_body = request.body.decode()
        request_create_body = json.loads(request_create_body)
        res = mockcar.mock_create_zhixing()
        # business_order_id字段
        no = res['data']['orderNo']
        cars[no] = {"out_source_no":"1125902188720645","cap_uid":"102420190117174818994331655000","dlat":30.982883111,"dlng":121.23012111,"strive_time":"2019-01-16 09:27:36",'passenger_clat':30.982883111,'passenger_clng':121.23012111,"booking_time":"2019-01-16 09:27:36"}
        # 模拟供应商触发回调
        booking_time = TimeHandler.mockcar_bookingtime_zhixing()
        cars[no]["booking_time"] = booking_time
        cars[no]['cap_uid'] = request_create_body['ext_order_id']
        url = 'http://10.33.16.55:10950/cas/callback/cm/state/notice'
        timestamp = str(TimeHandler.time_stamp())
        token = 'bc4998016bb2df0764e8f247847509fa'
        sign = MD5Handler.sign(no, timestamp, token)
        params = '{"order_id":"' + no + '","ext_order_id":"102420190227140946944010259000","event":"3","client_id":"10001","timestamp":' + timestamp + ',"sign":"' + sign + '"}'
        print("下单回调:%s" % params)
        counter[no] = 0
        doPostcallback_async2(url, params)
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 智行——订单详情状态流转
def carsupplier_zhixing(request):
    global cars,counter,car_param
    if request.method == "POST":
        request_data = request.body.decode()
        request_json = json.loads(request_data)
        print(request_json)
        business_order_id = request_json['order_id']

        if business_order_id == '2019030710015849220639':
            print("----------------16取消-----------------")
            cars[business_order_id] = car_param
            cars[business_order_id]['cap_uid'] = '102420190307115155688331655000'
            res = mockcar.mock_carcannel_supplier_zhixing(business_order_id, cars[business_order_id])
            del cars[business_order_id]
        elif business_order_id in cars.keys():

            if counter[business_order_id] >= 0 and counter[business_order_id] <= counter['wait'] :
            # if counter[business_order_id] >= 0 :
                print("----------------wait-----------------")
                # 模拟供应商主动取消
                # res = mockcar.mock_carcannel_supplier_zhixing(business_order_id, cars[business_order_id])
                res, strive_time = mockcar.mock_carwait_zhixing(business_order_id, cars[business_order_id])
                cars[business_order_id]['strive_time'] = strive_time
                # +1违约金需求
                if counter[business_order_id] == 0:
                    counter[business_order_id] += 1
            # elif counter[business_order_id] >= counter['wait']+1:
            #     # 此处模拟供应商取消
            #     print("----------------cancel-----------------")
            #     res = mockcar.mock_carcannel_supplier_zhixing(business_order_id, cars[business_order_id])
            elif counter[business_order_id] == counter['wait']+1:
                print("----------------arrive-----------------")
                res = mockcar.mock_cararrive_zhixing(business_order_id, cars[business_order_id])
                counter[business_order_id] += 1
            elif counter[business_order_id] >= counter['wait']+2 and counter[business_order_id] <= counter['arrive'] :
                print("----------------arrive-----------------")
                res = mockcar.mock_cararrive_zhixing(business_order_id, cars[business_order_id])
            elif counter[business_order_id] == counter['arrive']+1:
                print("----------------drive-----------------")
                res, begin_charge_time = mockcar.mock_cardrive_zhixing(business_order_id, cars[business_order_id])
                cars[business_order_id]['begin_charge_time'] = begin_charge_time
                counter[business_order_id] += 1
            # if counter[business_order_id] >= 0 and counter[business_order_id] <= 27:
            elif counter[business_order_id] >= counter['arrive']+2 and counter[business_order_id] <= counter['drive']:
                print("----------------drive-----------------")
                res, begin_charge_time = mockcar.mock_cardrive_zhixing(business_order_id, cars[business_order_id])
            elif counter[business_order_id] == counter['drive']+1:
                print("----------------prepay-----------------")
                res, finish_time = mockcar.mock_carprepay_zhixing(business_order_id, cars[business_order_id])
                cars[business_order_id]['finish_time'] = finish_time
                counter[business_order_id] += 1
            elif counter[business_order_id] == counter['drive']+2:
                print("----------------prepay-----------------")
                res = mockcar.mock_carprepay1_zhixing(business_order_id, cars[business_order_id])
                counter[business_order_id] += 1
            else:
                # res, begin_charge_time = mockcar.mock_cardrive(business_order_id, cars[business_order_id])
                res = mockcar.mock_carprepay1_zhixing(business_order_id, cars[business_order_id])
                # 检查状态state = '6'清空内存数据
                sql = "select state from car_child_order where business_order_id = '" + business_order_id + "'"
                if mysql_query(sql, 'car')[0] in ['6', '8', '9', '10', '11'] or mysql_query(sql, 'car')[0] == '':
                    del cars[business_order_id]
                    del counter[business_order_id]
        else:
            print("other orderid")
            res = mockcar.mock_carelse_zhixing(business_order_id, car_param)
        mocklog1 = '{}返回，内容：{}'.format(business_order_id, res)
        MyLog.info(mocklog1)
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 智行——取消
def carsuppliercannel_zhixing(request):
    global cars,car_param,counter
    if request.method == "POST":
        request_data = request.body.decode()
        request_json = json.loads(request_data)
        business_order_id = request_json['order_id']
        # 违约金判断
        if counter[business_order_id] == 0:
            res = mockcar.mock_carcannel1_zhixing()
        else:
            res = mockcar.mock_carcannel_zhixing()
        if business_order_id in cars.keys():
            del cars[business_order_id]
            del counter[business_order_id]
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 智行——预估价
def carestimateprice_zhixing(request):
    if request.method == "POST":
        res = mockcar.mock_carestimateprice_zhixing()
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 智行——取消费用
def cancelorderfee_zhixing(request):
    if request.method == "POST":
        res = mockcar.mock_cancelorderfee_zhixing()
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 智行——确认费用
def paynotice_zhixing(request):
    if request.method == "POST":
        res = mockcar.mock_carpaynotice_supplier_zhixing()
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
# 智行——司机位置
def cardriverlocation_zhixing(request):
    if request.method == "POST":
        request_data = request.body.decode()
        request_json = json.loads(request_data)
        business_order_id = request_json['order_id']

        url = 'http://10.33.16.55:10950/cas/callback/cm/state/notice'
        timestamp = str(TimeHandler.time_stamp())
        token = 'bc4998016bb2df0764e8f247847509fa'
        sign = MD5Handler.sign(business_order_id, timestamp, token)
        params = '{"order_id":"' + business_order_id + '","ext_order_id":"102420190227140946944010259000","event":"3","client_id":"10001","timestamp":' + timestamp + ',"sign":"' + sign + '"}'

        if counter[business_order_id] >= 0 and counter[business_order_id] <= counter['wait']:
            print("----------------wait-----------------")
            cars[business_order_id]["dlat"] += 0.03
            cars[business_order_id]["dlng"] += 0.03
            res = mockcar.mock_cardriverlocation_zhixing(business_order_id, cars[business_order_id])
            counter[business_order_id] += 1
        elif counter[business_order_id] == counter['wait']+1:
            print("----------------arrive-----------------")
            res = mockcar.mock_cardriverlocation_zhixing(business_order_id, cars[business_order_id])
            doPostcallback2(url, params)
        elif counter[business_order_id] >= counter['wait']+2 and counter[business_order_id] <= counter['arrive'] :
            print("----------------arrive-----------------")
            res = mockcar.mock_cardriverlocation_zhixing(business_order_id, cars[business_order_id])
            counter[business_order_id] += 1
        elif counter[business_order_id] == counter['arrive']+1:
            print("----------------drive-----------------")
            res = mockcar.mock_cardriverlocation_zhixing(business_order_id, cars[business_order_id])
            doPostcallback2(url, params)
        # if counter[business_order_id] >= 0 and counter[business_order_id] <= 27:
        elif counter[business_order_id] >= counter['arrive']+2 and counter[business_order_id] <= counter['drive']:
            print("----------------drive-----------------")
            cars[business_order_id]["dlat"] -= 0.03
            cars[business_order_id]["dlng"] -= 0.03
            res = mockcar.mock_cardriverlocation_zhixing(business_order_id, cars[business_order_id])
            counter[business_order_id] += 1
        elif counter[business_order_id] == counter['drive']+1:
            print("----------------prepay-----------------")
            res = mockcar.mock_cardriverlocation_zhixing(business_order_id, cars[business_order_id])
            doPostcallback2(url, params)
        else:
            print("----------------prepay-----------------")
            res = mockcar.mock_cardriverlocation_zhixing(business_order_id, cars[business_order_id])
            counter[business_order_id] += 1
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})