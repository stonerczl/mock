from mock import Mock
import datetime
import random
from common import TimeHandler

# 企业管家
# 企业管家——接单
def mock_carwait_ex(param,car_param):
    no = param
    strive_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": car_param['out_source_no'],
                        "state": "waiting",
                        "state_name": "等待接驾",
                        "amount": "1.00",
                        "cap_uid": car_param['cap_uid'],
                        "created_at": "2019-01-17 15:50:17",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "李师傅",
                        "driver_phone": "13482405154",
                        "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
                        "driver_order_count": "59",
                        "driver_level": "4.27",
                        "driver_card": "京I11011",
                        "driver_car_color": "红",
                        "driver_car_type": "奥迪A6（进口）",
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": car_param['dlat'],
                        "dlng": car_param['dlng'],
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": strive_time,
                        "begin_charge_time": None,
                        "finish_time": None,
                        "is_emergency_help":"0",
                        "emergency_help_url":car_param['emergency_help_url'],
                          "emergency_help_time": None,
                          "passenger_clat": car_param['passenger_clat'],
                          "passenger_clng": car_param['passenger_clng'],
                        #   "is_emergency_help": "0",
                        #   "emergency_help_url": None,
                        "source": car_param['source']
                          # departure_time": "2019 - 01 - 17 15:50: 17",
                          # insured": false,
                          #        "insured_name": "出行意外险, 一元保100万",
                          #                        "order_and_strive_time_diff": 87
                      }
                    }
    # time.sleep(2.5)
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response(),strive_time
# 企业管家——接单
def mock_carwait(param,car_param):
    no = param
    strive_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": car_param['out_source_no'],
                          "cap_uid": car_param['cap_uid'],
                        "state": "waiting",
                        "state_name": "等待接驾",
                        "amount": "0",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "李师傅",
                        "driver_phone": "13482405154",
                        "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
                        "driver_order_count": "59",
                        "driver_level": "4.27",
                        "driver_card": "京I11011",
                        "driver_car_color": "红",
                        "driver_car_type": "奥迪A6（进口）",
                        "flat": 31.181364,
                        "flng": 121.48687,
                        "tlat": 30.982883,
                        "tlng": 121.23012,
                        "dlat": car_param['dlat'],
                        "dlng": car_param['dlng'],
                          # "flat": None,
                          # "flng": None,
                          # "tlat": None,
                          # "tlng": None,
                          # "dlat": None,
                          # "dlng": None,
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": strive_time,
                        "begin_charge_time": None,
                        "finish_time": None,
                          "is_emergency_help":"0",
                          "emergency_help_url":car_param['emergency_help_url'],
                          "emergency_help_time": None,
                          "passenger_clat": car_param['passenger_clat'],
                          "passenger_clng": car_param['passenger_clng'],
                        "source": car_param['source']
                      }
                    }
    # time.sleep(2.5)
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response(),strive_time
# 企业管家——到达
def mock_cararrive(param,car_param):
    no = param
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": car_param['out_source_no'],
                          "cap_uid": car_param['cap_uid'],
                        "state": "arrived",
                        "state_name": "已到达",
                        "amount": "0",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "李师傅",
                        "driver_phone": "13482405154",
                        "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
                        "driver_order_count": "59",
                        "driver_level": "4.27",
                        "driver_card": "京I11011",
                        "driver_car_color": "红",
                        "driver_car_type": "奥迪A6（进口）",
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": 31.181364111,
                        "dlng": 121.48687111,
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": car_param['strive_time'],
                        # "strive_time": "2019-01-08 09:27:36",
                        "begin_charge_time": None,
                        "finish_time": None,
                          "is_emergency_help":"0",
                          "emergency_help_url":car_param['emergency_help_url'],
                          "emergency_help_time": None,
                          "passenger_clat": car_param['passenger_clat'],
                          "passenger_clng": car_param['passenger_clng'],
                        "source": car_param['source']
                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——行程中
def mock_cardrive(param,car_param):
    no = param
    begin_charge_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    flat = 31.181364
    flng = 121.48687
    tlat = 30.982883
    tlng = 121.23012

    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": car_param['out_source_no'],
                          "cap_uid": car_param['cap_uid'],
                        "state": "processing",
                        "state_name": "行程中",
                        "amount": "0",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "李师傅",
                        "driver_phone": "13482405154",
                        "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
                        "driver_order_count": "59",
                        "driver_level": "4.27",
                        "driver_card": "京I11011",
                        "driver_car_color": "红",
                        "driver_car_type": "奥迪A6（进口）",
                        "flat": flat,
                        "flng": flng,
                        "tlat": tlat,
                        "tlng": tlng,
                        "dlat": car_param['dlat'],
                        "dlng": car_param['dlng'],
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": car_param['strive_time'],
                        "begin_charge_time": begin_charge_time,
                        "finish_time": None,
                          "is_emergency_help":"0",
                          "emergency_help_url":car_param['emergency_help_url'],
                          "emergency_help_time": None,
                          "passenger_clat": car_param['passenger_clat'],
                          "passenger_clng": car_param['passenger_clng'],
                        "source": car_param['source']

                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response(), begin_charge_time
# 企业管家——待支付
def mock_carprepay(param,car_param):
    no = param
    finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": car_param['out_source_no'],
                          "cap_uid": car_param['cap_uid'],
                        "state": "pending_pay",
                        "state_name": "待支付",
                        "amount": "10.01",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "陈师傅",
                        "driver_phone": "13482405154",
                        "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
                        "driver_order_count": "60",
                        "driver_level": "4.27",
                        "driver_card": "京I11011",
                        "driver_car_color": "红",
                        "driver_car_type": "奥迪A6（进口）",
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": 30.982883111,
                        "dlng": 121.23012111,
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": car_param['strive_time'],
                        "begin_charge_time": car_param['begin_charge_time'],
                        "finish_time": finish_time,
                          # "begin_charge_time": None,
                          # "finish_time": None,
                          "is_emergency_help": "0",
                          "emergency_help_url": car_param['emergency_help_url'],
                          "emergency_help_time": None,
                          "passenger_clat": car_param['passenger_clat'],
                          "passenger_clng": car_param['passenger_clng'],
                        "source": car_param['source']
                      }
                    }

    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response(),finish_time
# 企业管家——待支付（因为finishtime值）
def mock_carprepay1(param,car_param):
    no = param
    finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": car_param['out_source_no'],
                        "state": "pending_pay",
                        "state_name": "待支付",
                          "cap_uid": car_param['cap_uid'],
                        "amount": "10.01",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "李师傅",
                        "driver_phone": "13482405154",
                        "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
                        "driver_order_count": "60",
                        "driver_level": "4.27",
                        "driver_card": "京I11011",
                        "driver_car_color": "红",
                        "driver_car_type": "奥迪A6（进口）",
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": 30.982883111,
                        "dlng": 121.23012111,
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": car_param['strive_time'],
                          # "begin_charge_time": None,
                          # "finish_time": None,
                        "begin_charge_time": car_param['begin_charge_time'],
                        "finish_time": car_param['finish_time'],
                          "is_emergency_help": "0",
                          "emergency_help_url": car_param['emergency_help_url'],
                          "emergency_help_time": None,
                          "passenger_clat": car_param['passenger_clat'],
                          "passenger_clng": car_param['passenger_clng'],
                        "source": car_param['source']
                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()

# 嘀嗒 已完成
# 企业管家——线上待支付
def mock_carcompleted_online(param,car_param):
    no = param
    finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": car_param['out_source_no'],
                        "state": "completed",
                          "sub_state": "6",
                        "state_name": "已完成",
                          "cap_uid": car_param['cap_uid'],
                        "amount": "2.01",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "李师傅",
                        "driver_phone": "13482405154",
                        "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
                        "driver_order_count": "60",
                        "driver_level": "4.27",
                        "driver_card": "京I11011",
                        "driver_car_color": "红",
                        "driver_car_type": "奥迪A6（进口）",
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": 30.982883111,
                        "dlng": 121.23012111,
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": car_param['strive_time'],
                          # "begin_charge_time": None,
                          # "finish_time": None,
                        "begin_charge_time": car_param['begin_charge_time'],
                        "finish_time": finish_time,
                          "is_emergency_help": "0",
                          "emergency_help_url": car_param['emergency_help_url'],
                          "emergency_help_time": None,
                          "passenger_clat": car_param['passenger_clat'],
                          "passenger_clng": car_param['passenger_clng'],
                        "source": car_param['source']
                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response(),finish_time
# 企业管家——线上待支付（因为finishtime值）
def mock_carcompleted_online1(param, car_param):
  no = param
  finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  response_json = {
    "code": "0",
    "message": "success",
    "data": {
      "no": no,
      "out_source_no": car_param['out_source_no'],
      "state": "completed",
      "sub_state": "6",
      "state_name": "已完成",
      "cap_uid": car_param['cap_uid'],
      "amount": "2.01",
      "call_together_no": None,
      "call_together_result_no": None,
      "order_type": 0,
      "instead_call": None,
      "from": "鲁能国际中心C座",
      "from_detail": "",
      "to": "松江南站",
      "to_detail": "盐仓路",
      "level": 600,
      "driver_name": "李师傅",
      "driver_phone": "13482405154",
      "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
      "driver_order_count": "60",
      "driver_level": "4.27",
      "driver_card": "京I11011",
      "driver_car_color": "红",
      "driver_car_type": "奥迪A6（进口）",
      "flat": 31.181364111,
      "flng": 121.48687111,
      "tlat": 30.982883111,
      "tlng": 121.23012111,
      "dlat": 30.982883111,
      "dlng": 121.23012111,
      "clat": None,
      "clng": None,
      "estimate_price": "148.6",
      "passenger_name": "苍伟",
      "passenger_phone": "11046248696",
      "common_level": None,
      "common_comment": None,
      "strive_time": car_param['strive_time'],
      # "begin_charge_time": None,
      # "finish_time": None,
      "begin_charge_time": car_param['begin_charge_time'],
      "finish_time": car_param['finish_time'],
      "is_emergency_help": "0",
      "emergency_help_url": car_param['emergency_help_url'],
      "emergency_help_time": None,
      "passenger_clat": car_param['passenger_clat'],
      "passenger_clng": car_param['passenger_clng'],
      "source": car_param['source']
    }
  }
  mock_response = Mock(return_value=response_json)
  print("返回:%s" % mock_response())
  return mock_response()
# 企业管家——线下支付
def mock_carcompleted_underline(param, car_param):
  no = param
  finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  response_json = {
                    "code": "0",
                    "message": "success",
                    "data": {
                      "no": no,
                      "out_source_no": car_param['out_source_no'],
                      "state": "completed",
                      "sub_state": "7",
                      "state_name": "已完成",
                      "cap_uid": car_param['cap_uid'],
                      "amount": "0",
                      "call_together_no": None,
                      "call_together_result_no": None,
                      "order_type": 0,
                      "instead_call": None,
                      "from": "鲁能国际中心C座",
                      "from_detail": "",
                      "to": "松江南站",
                      "to_detail": "盐仓路",
                      "level": 600,
                      "driver_name": "李师傅",
                      "driver_phone": "13482405154",
                      "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
                      "driver_order_count": "60",
                      "driver_level": "4.27",
                      "driver_card": "京I11011",
                      "driver_car_color": "红",
                      "driver_car_type": "奥迪A6（进口）",
                      "flat": 31.181364111,
                      "flng": 121.48687111,
                      "tlat": 30.982883111,
                      "tlng": 121.23012111,
                      "dlat": 30.982883111,
                      "dlng": 121.23012111,
                      "clat": None,
                      "clng": None,
                      "estimate_price": "148.6",
                      "passenger_name": "苍伟",
                      "passenger_phone": "11046248696",
                      "common_level": None,
                      "common_comment": None,
                      "strive_time": car_param['strive_time'],
                      # "begin_charge_time": None,
                      # "finish_time": None,
                      "begin_charge_time": car_param['begin_charge_time'],
                      "finish_time": finish_time,
                      "is_emergency_help": "0",
                      "emergency_help_url": car_param['emergency_help_url'],
                      "emergency_help_time": None,
                      "passenger_clat": car_param['passenger_clat'],
                      "passenger_clng": car_param['passenger_clng'],
                      "source": car_param['source']
                    }
                  }
  mock_response = Mock(return_value=response_json)
  print("返回:%s" % mock_response())
  return mock_response(),finish_time
# 企业管家——线下支付（因为finishtime值）
def mock_carcompleted_underline1(param, car_param):
  no = param
  finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  response_json = {
                    "code": "0",
                    "message": "success",
                    "data": {
                      "no": no,
                      "out_source_no": car_param['out_source_no'],
                      "state": "completed",
                      "sub_state": "7",
                      "state_name": "已完成",
                      "cap_uid": car_param['cap_uid'],
                      "amount": "0",
                      "call_together_no": None,
                      "call_together_result_no": None,
                      "order_type": 0,
                      "instead_call": None,
                      "from": "鲁能国际中心C座",
                      "from_detail": "",
                      "to": "松江南站",
                      "to_detail": "盐仓路",
                      "level": 600,
                      "driver_name": "李师傅",
                      "driver_phone": "13482405154",
                      "driver_avatar": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548923671633&di=e8ff07f747aee726373df3063a5aaddf&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D125214459%2C1834054163%26fm%3D214%26gp%3D0.jpg",
                      "driver_order_count": "60",
                      "driver_level": "4.27",
                      "driver_card": "京I11011",
                      "driver_car_color": "红",
                      "driver_car_type": "奥迪A6（进口）",
                      "flat": 31.181364111,
                      "flng": 121.48687111,
                      "tlat": 30.982883111,
                      "tlng": 121.23012111,
                      "dlat": 30.982883111,
                      "dlng": 121.23012111,
                      "clat": None,
                      "clng": None,
                      "estimate_price": "148.6",
                      "passenger_name": "苍伟",
                      "passenger_phone": "11046248696",
                      "common_level": None,
                      "common_comment": None,
                      "strive_time": car_param['strive_time'],
                      # "begin_charge_time": None,
                      # "finish_time": None,
                      "begin_charge_time": car_param['begin_charge_time'],
                      "finish_time": car_param['finish_time'],
                      "is_emergency_help": "0",
                      "emergency_help_url": car_param['emergency_help_url'],
                      "emergency_help_time": None,
                      "passenger_clat": car_param['passenger_clat'],
                      "passenger_clng": car_param['passenger_clng'],
                      "source": car_param['source']
                    }
                  }
  mock_response = Mock(return_value=response_json)
  print("返回:%s" % mock_response())
  return mock_response()
# 企业管家——供应商取消
def mock_carcannel_supplier(param,car_param):
    no = param
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": "11111111111",
                          "cap_uid": car_param['cap_uid'],
                        "state": "cancel",
                        "state_name": "已取消",
                        "amount": "1.00",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "",
                        "driver_phone": "",
                        "driver_avatar": "",
                        "driver_order_count": "0",
                        "driver_level": "0",
                        "driver_card": "",
                        "driver_car_color": "",
                        "driver_car_type": "",
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": None,
                        "dlng": None,
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": None,
                        "begin_charge_time": None,
                        "finish_time": None,
                        "source": car_param['source']
                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——供应商超时
def mock_cartimeout(param,car_param):
    no = param
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": "11111111111",
                          "cap_uid": car_param['cap_uid'],
                        "state": "timeout",
                        "state_name": "超时",
                        "amount": "0",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "",
                        "driver_phone": "",
                        "driver_avatar": "",
                        "driver_order_count": "0",
                        "driver_level": "0",
                        "driver_card": "",
                        "driver_car_color": "",
                        "driver_car_type": "",
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": None,
                        "dlng": None,
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": None,
                        "begin_charge_time": None,
                        "finish_time": None,
                        "source": "shouqi"
                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——取消(司机接单后取消费用)
def mock_carcannel():
    response_json = {
                      "code": "0",
                      "message": "success",
                      # "data": {
                      #   "cost": 0.0
                      # }
                        "data": None
                    }
    # 异常
    # response_json = {
    #                   "code": "4001",
    #                   "message": "fail",
    #                   "data": {
    #                     "cost": 0.0
    #                   }
    #                 }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——取消(未接单取消无取消费用)
def mock_carcannel1():
    response_json = {
                      "code": "0",
                      "message": "success",
                      # "data": {
                      #   "cost": 0.0
                      # }
                        "data": None
                    }
    # 异常
    # response_json = {
    #                   "code": "4001",
    #                   "message": "fail",
    #                   "data": {
    #                     "cost": 0.0
    #                   }
    #                 }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——车型
def mock_carcityprice():
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "didi": [
                          200,
                          400,
                          100,
                          600,
                          900
                        ],
                        "shenzhou": [
                          100,
                          200,
                          400
                        ],
                        "caocao": [
                          600
                        ],
                        "yidao": [
                          100,
                          200,
                          600
                        ],
                          "shouqi": [
                              100,
                              200,
                              600
                          ]
                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——询价
def mock_carestimateprice():
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "didi": {
                          "estimate_price": {
                            "price": 198,
                            "name": "普通型",
                            "real_price": 198,
                            "memo": "",
                            "favourable": False
                          },
                          "min_duration": {
                            "has_car": True,
                            "min_duration": 4,
                            "min_distance": 1206
                          }
                        },
                        "shenzhou": {
                          "estimate_price": {
                            "price": 9,
                            "name": "普通型",
                            "real_price": 9,
                            "memo": "",
                            "favourable": False
                          },
                          "min_duration": {
                            "has_car": True,
                            "min_duration": 1,
                            "min_distance": 100
                          }
                        },
                        "caocao": {
                          "estimate_price": {
                            "price": 20,
                            "name": "新能源",
                            "real_price": 20,
                            "memo": "限时9.8折",
                            "favourable": True
                          },
                          "min_duration": {
                            "has_car": True,
                            "min_duration": 4,
                            "min_distance": 987
                          }
                        },
                        "yidao": {
                          "estimate_price": {
                            "price": 199,
                            "name": "易达",
                            "real_price": 200,
                            "memo": "",
                            "favourable": False
                          },
                          "min_duration": {
                            "has_car": True,
                            "min_duration": 5,
                            "min_distance": 1500
                          }
                        },
                          "shouqi": {
                              "estimate_price": {
                                  "price": 14.6,
                                  "name": "首汽",
                                  "real_price": 12.6,
                                  "memo": "",
                                  "favourable": False
                              },
                              "min_duration": {
                                  "has_car": True,
                                  "min_duration": 5,
                                  "min_distance": 1500
                              }
                          },
                          "dida": {
                              "estimate_price": {
                                  "price": 34.0,
                                  "name": "出租车",
                                  "real_price": 34.0,
                                  "memo": "",
                                  "favourable": True
                              },
                              "min_duration": {
                                  "has_car": False,
                                  "min_duration": 19,
                                  "min_distance": None
                              }
                          }
                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——下单
def mock_create(source):
    out_source_no = random.randint(1000000000000000,9999999999999999)
    no = "BO0" + str(out_source_no+1)
    out_source_no_str = str(out_source_no)
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": out_source_no_str,
                        "state": "pending",
                        "state_name": "呼叫中",
                        "amount": 0,
                        "total_amount": 0,
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": 0,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "",
                        "level": 600,
                        "driver_name": None,
                        "driver_phone": None,
                        "driver_avatar": None,
                        "driver_order_count": None,
                        "driver_level": None,
                        "driver_card": None,
                        "driver_car_color": "红",
                        "driver_car_type": None,
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": None,
                        "dlng": None,
                        "clng": None,
                        "clat": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "note": None,
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": None,
                        "begin_charge_time": None,
                        "finish_time": None,
                        "source": source
                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——支付
def mock_carpay():
    response_json = {
        "code": "0",
        "message": "success",
        "data": {
                  "id": 7566,
                  "no": "TR0319133702215F969",
                  "status": "pay_succeed",
                  "amount": "-20.0",
                  "paid_at": "2019-03-19T13:37:02.458+08:00",
                  "base_order_id": 31511,
                  "user_id": None,
                  "organization_id": 477,
                  "account_id": 653,
                  "account_type": "Organizeaccount",
                  "out_trade_no": None,
                  "transaction_no": None,
                  "succeeded_at": "2019-03-19T13:37:02.458+08:00",
                  "created_at": "2019-03-19T13:37:02.314+08:00",
                  "updated_at": "2019-03-19T13:37:02.465+08:00",
                  "trade_type": "Business",
                  "source_id": None,
                  "source_type": None,
                  "out_trade_string": None,
                  "out_source_callback_data": None,
                  "combine_orders": None,
                  "memo": None,
                  "external_memo": None
                }
    }
    # 异常
    # response_json = {
    #                   "code": "4004",
    #                   "message": "暂不能支付,请稍后重试",
    #                   "data": None
    #                 }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——滴滴下单录音授权
def mock_create_ex(source):
    out_source_no = random.randint(1000000000000000,9999999999999999)
    no = "BO0" + str(out_source_no+1)
    out_source_no_str = str(out_source_no)
    response_json = {
                      "code": "20051",
                      "message": "https://page.udache.com/passenger/apps/record-authorize-third/index.html?openid=MTAwMDUyMDE1YWA8hZD7ELv9EYBHt7%2BSR%2FlYG90%3D&third_token=79C1C3957ECB330166C9ABB9003D21C85A60DBEAAAE07B83A28DDA226322A4FCD5BE819880C046E0784BC37DBD24875A9362C417BF9EAA03FA6564EDD3DFEEF0&record_type=video",
                      "data": {
                        "no": no,
                        "out_source_no": out_source_no_str,
                        "state": "pending",
                        "state_name": "呼叫中",
                        "amount": 0,
                        "total_amount": 0,
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": 0,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "",
                        "level": 600,
                        "driver_name": None,
                        "driver_phone": None,
                        "driver_avatar": None,
                        "driver_order_count": None,
                        "driver_level": None,
                        "driver_card": None,
                        "driver_car_color": "红",
                        "driver_car_type": None,
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": None,
                        "dlng": None,
                        "clng": None,
                        "clat": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "note": None,
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": None,
                        "begin_charge_time": None,
                        "finish_time": None,
                        "source": source
                      }
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 企业管家——异常单子简单返回处理
def mock_carelse(param,car_param):
    no = param
    # strive_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                      "code": "0",
                      "message": "success",
                      "data": {
                        "no": no,
                        "out_source_no": "11111111",
                          "cap_uid": car_param['cap_uid'],
                          "state": "cancel",
                          "state_name": "已取消",
                        # "state": "waiting",
                        # "state_name": "等待接驾",
                        "amount": "0",
                        "call_together_no": None,
                        "call_together_result_no": None,
                        "order_type": 0,
                        "instead_call": None,
                        "from": "鲁能国际中心C座",
                        "from_detail": "",
                        "to": "松江南站",
                        "to_detail": "盐仓路",
                        "level": 600,
                        "driver_name": "李师傅",
                        "driver_phone": "13482405154",
                        "driver_avatar": None,
                        "driver_order_count": "59",
                        "driver_level": "4.27",
                        "driver_card": "京I11011",
                        "driver_car_color": "红",
                        "driver_car_type": "奥迪A6（进口）",
                        "flat": 31.181364111,
                        "flng": 121.48687111,
                        "tlat": 30.982883111,
                        "tlng": 121.23012111,
                        "dlat": car_param['dlat'],
                        "dlng": car_param['dlng'],
                        "clat": None,
                        "clng": None,
                        "estimate_price": "148.6",
                        "passenger_name": "苍伟",
                        "passenger_phone": "11046248696",
                        "common_level": None,
                        "common_comment": None,
                        "strive_time": "2019-01-08 09:27:36",
                        "begin_charge_time": None,
                        "finish_time": None,
                        "source": "shouqi"
                      }
                    }
    # time.sleep(2.5)
    mock_response = Mock(return_value=response_json)
    # print("返回:%s" % mock_response())
    return mock_response()


# 智行
# 智行——下单
def mock_create_zhixing():
    random_num = random.randint(10000000, 99999999)
    orderNo = TimeHandler.mockcar_time_zhixing() + str(random_num)
    response_json = {
                        "data": {
                            "orderNo": orderNo
                        },
                        "code": 200,
                        "success": True,
                        "msg": None
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——接单
def mock_carwait_zhixing(param,car_param):
    no = param
    strive_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                    "data": {
                        "basicOrderVO": {
                            "callerPhone": "18912394254",
                            "cityCode": "2",
                            "departureTime": car_param["booking_time"],
                            "endAddress": "盐仓路",
                            "endName": "",
                            "realEndAddress": None,
                            "beginChargeTime": None,
                            "estimatePrice": 12000,
                            "extOrderId": car_param['cap_uid'],
                            "otaOrderId": "7249302000",
                            "extraInfo": "",
                            "features": {
                                "start_name": "鲁能国际中心C座",
                                "o_cbi": "null",
                                "o_bsl": "b84c1ed2ca6c70f9",
                                "end_name": "松江南站",
                                "reassigned": "0",
                                "is_c": None
                            },
                            "fromLocation": {
                                "lat": 31.181364,
                                "lng": 121.48687
                            },
                            "invoiceStatus": 0,
                            "invoiced": False,
                            "orderId": "7249302000",
                            "orderLocation": {
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "orderTime": car_param["booking_time"],
                            "passengerName": "鲍洋",
                            "passengerPhone": "18912394254",
                            "realStartLocation": {
                                "direction": 0.0,
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "requireLevel": 4,
                            "startAddress": "",
                            "realStartAddress": None,
                            "startName": "",
                            "startServiceTime": strive_time,
                            "status": 2,  # 已派单
                            "striveTime": strive_time,
                            "toLocation": {
                                "lat": 30.982883,
                                "lng": 121.23012
                            },
                            "realEndLocation": None,
                            "type": 1,  #实时单
                            "flightNumber": None,
                            "canceledTime": None,
                            "finishTime": None,
                            "payTime": None,
                            "normalDistance": None,
                            "normalTime": None
                        },
                        "driverInfoVo": {
                            "avatar": None,
                            "carId": 900006302,
                            "carType": "S60L E驱混动",
                            "card": "浙A7189",
                            "color": "红色",
                            "id": 100001081,
                            "level": "5.0",
                            "location": {
                                "lat": car_param['dlat'],
                                "lng": car_param['dlng']
                            },
                            "name": "田师傅",
                            "orderCnt": 16,
                            "phone": "13826193851"
                        },
                        "orderFeeVo": {
                            "detailFeeVos": [{
                                "amount": 0,
                                "chargeCode": "start_fee",
                                "chargeDesc": "订单起步价"
                            }],
                            "originTotalFee": 0,
                            "totalFee": 12000
                        }
                    },
                    "code": 200,
                    "success": True,
                    "msg": None
                }
    # time.sleep(2.5)
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response(),strive_time
# 智行——到达
def mock_cararrive_zhixing(param,car_param):
    no = param
    response_json = {
                    "data": {
                        "basicOrderVO": {
                            "callerPhone": "18912394254",
                            "cityCode": "2",
                            "departureTime": car_param["booking_time"],
                            "endAddress": "盐仓路",
                            "endName": "",
                            "realEndAddress": None,
                            "beginChargeTime": None,
                            "estimatePrice": 12000,
                            "extOrderId": car_param['cap_uid'],
                            "otaOrderId": "7249302000",
                            "extraInfo": "",
                            "features": {
                                "start_name": "鲁能国际中心C座",
                                "o_cbi": "null",
                                "o_bsl": "b84c1ed2ca6c70f9",
                                "end_name": "松江南站",
                                "reassigned": "0",
                                "is_c": None
                            },
                            "fromLocation": {
                                "lat": 31.181364,
                                "lng": 121.48687
                            },
                            "invoiceStatus": 0,
                            "invoiced": False,
                            "orderId": "7249302000",
                            "orderLocation": {
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "orderTime": car_param["booking_time"],
                            "passengerName": "鲍洋",
                            "passengerPhone": "18912394254",
                            "realStartLocation": {
                                "direction": 0.0,
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "requireLevel": 4,
                            "startAddress": "",
                            "realStartAddress": None,
                            "startName": "",
                            "startServiceTime": car_param['strive_time'],
                            "status": 12,  # 到达
                            "striveTime": car_param['strive_time'],
                            "toLocation": {
                                "lat": 30.982883,
                                "lng": 121.23012
                            },
                            "realEndLocation": None,
                            "type": 1,  #实时单
                            "flightNumber": None,
                            "canceledTime": None,
                            "finishTime": None,
                            "payTime": None,
                            "normalDistance": None,
                            "normalTime": None
                        },
                        "driverInfoVo": {
                            "avatar": None,
                            "carId": 900006302,
                            "carType": "S60L E驱混动",
                            "card": "浙A7189",
                            "color": "红色",
                            "id": 100001081,
                            "level": "5.0",
                            "location": {
                                "lat": car_param['dlat'],
                                "lng": car_param['dlng']
                            },
                            "name": "田师傅",
                            "orderCnt": 16,
                            "phone": "13826193851"
                        },
                        "orderFeeVo": {
                            "detailFeeVos": [{
                                "amount": 0,
                                "chargeCode": "start_fee",
                                "chargeDesc": "订单起步价"
                            }],
                            "originTotalFee": 0,
                            "totalFee": 12000
                        }
                    },
                    "code": 200,
                    "success": True,
                    "msg": None
                }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——行程中
def mock_cardrive_zhixing(param,car_param):
    no = param
    begin_charge_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    response_json = {
                    "data": {
                        "basicOrderVO": {
                            "callerPhone": "18912394254",
                            "cityCode": "2",
                            "departureTime": car_param["booking_time"],
                            "endAddress": "盐仓路",
                            "endName": "",
                            "realEndAddress": None,
                            "beginChargeTime": begin_charge_time,
                            "estimatePrice": 12000,
                            "extOrderId": car_param['cap_uid'],
                            "otaOrderId": "7249302000",
                            "extraInfo": "",
                            "features": {
                                "start_name": "鲁能国际中心C座",
                                "o_cbi": "null",
                                "o_bsl": "b84c1ed2ca6c70f9",
                                "end_name": "松江南站",
                                "reassigned": "0",
                                "is_c": None
                            },
                            "fromLocation": {
                                "lat": 31.181364,
                                "lng": 121.48687
                            },
                            "invoiceStatus": 0,
                            "invoiced": False,
                            "orderId": "7249302000",
                            "orderLocation": {
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "orderTime": car_param["booking_time"],
                            "passengerName": "鲍洋",
                            "passengerPhone": "18912394254",
                            "realStartLocation": {
                                "direction": 0.0,
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "requireLevel": 4,
                            "startAddress": "",
                            "realStartAddress": None,
                            "startName": "",
                            "startServiceTime": car_param['strive_time'],
                            "status": 3,  # 计费
                            "striveTime": car_param['strive_time'],
                            "toLocation": {
                                "lat": 30.982883,
                                "lng": 121.23012
                            },
                            "realEndLocation": None,
                            "type": 1,  #实时单
                            "flightNumber": None,
                            "canceledTime": None,
                            "finishTime": None,
                            "payTime": None,
                            "normalDistance": None,
                            "normalTime": None
                        },
                        "driverInfoVo": {
                            "avatar": None,
                            "carId": 900006302,
                            "carType": "S60L E驱混动",
                            "card": "浙A7189",
                            "color": "红色",
                            "id": 100001081,
                            "level": "5.0",
                            "location": {
                                "lat": car_param['dlat'],
                                "lng": car_param['dlng']
                            },
                            "name": "田师傅",
                            "orderCnt": 16,
                            "phone": "13826193851"
                        },
                        "orderFeeVo": {
                            "detailFeeVos": [{
                                "amount": 0,
                                "chargeCode": "start_fee",
                                "chargeDesc": "订单起步价"
                            }],
                            "originTotalFee": 0,
                            "totalFee": 12000
                        }
                    },
                    "code": 200,
                    "success": True,
                    "msg": None
                }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response(), begin_charge_time
# 智行——待支付
def mock_carprepay_zhixing(param,car_param):
    no = param
    finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                    "data": {
                        "basicOrderVO": {
                            "callerPhone": "18912394254",
                            "cityCode": "2",
                            "departureTime": car_param["booking_time"],
                            "endAddress": "盐仓路",
                            "endName": "",
                            "realEndAddress": None,
                            "beginChargeTime": car_param['begin_charge_time'],
                            "estimatePrice": 10102,
                            "extOrderId": car_param['cap_uid'],
                            "otaOrderId": "7249302000",
                            "extraInfo": "",
                            "features": {
                                "start_name": "鲁能国际中心C座",
                                "o_cbi": "null",
                                "o_bsl": "b84c1ed2ca6c70f9",
                                "end_name": "松江南站",
                                "reassigned": "0",
                                "is_c": None
                            },
                            "fromLocation": {
                                "lat": 31.181364,
                                "lng": 121.48687
                            },
                            "invoiceStatus": 0,
                            "invoiced": False,
                            "orderId": "7249302000",
                            "orderLocation": {
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "orderTime": car_param["booking_time"],
                            "passengerName": "鲍洋",
                            "passengerPhone": "18912394254",
                            "realStartLocation": {
                                "direction": 0.0,
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "requireLevel": 4,
                            "startAddress": "",
                            "realStartAddress": None,
                            "startName": "",
                            "startServiceTime": car_param['strive_time'],
                            "status": 7,  # 待支付
                            "striveTime": car_param['strive_time'],
                            "toLocation": {
                                "lat": 30.982883,
                                "lng": 121.23012
                            },
                            "realEndLocation": None,
                            "type": 1,  #实时单
                            "flightNumber": None,
                            "canceledTime": None,
                            "finishTime": finish_time,
                            "payTime": None,
                            "normalDistance": None,
                            "normalTime": None
                        },
                        "driverInfoVo": {
                            "avatar": None,
                            "carId": 900006302,
                            "carType": "S60L E驱混动",
                            "card": "浙A7189",
                            "color": "红色",
                            "id": 100001081,
                            "level": "5.0",
                            "location": {
                                "lat": car_param['dlat'],
                                "lng": car_param['dlng']
                            },
                            "name": "田师傅",
                            "orderCnt": 16,
                            "phone": "13826193851"
                        },
                        "orderFeeVo": {
                            "detailFeeVos": [{
                                "amount": 0,
                                "chargeCode": "start_fee",
                                "chargeDesc": "订单起步价"
                            }],
                            "originTotalFee": 0,
                            "totalFee": 10102
                        }
                    },
                    "code": 200,
                    "success": True,
                    "msg": None
                }

    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response(),finish_time
# 智行——待支付（因为finishtime值）
def mock_carprepay1_zhixing(param,car_param):
    no = param
    finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                    "data": {
                        "basicOrderVO": {
                            "callerPhone": "18912394254",
                            "cityCode": "2",
                            "departureTime": car_param["booking_time"],
                            "endAddress": "盐仓路",
                            "endName": "",
                            "realEndAddress": None,
                            "beginChargeTime": car_param['begin_charge_time'],
                            "estimatePrice": 10102,
                            "extOrderId": car_param['cap_uid'],
                            "otaOrderId": "7249302000",
                            "extraInfo": "",
                            "features": {
                                "start_name": "鲁能国际中心C座",
                                "o_cbi": "null",
                                "o_bsl": "b84c1ed2ca6c70f9",
                                "end_name": "松江南站",
                                "reassigned": "0",
                                "is_c": None
                            },
                            "fromLocation": {
                                "lat": 31.181364,
                                "lng": 121.48687
                            },
                            "invoiceStatus": 0,
                            "invoiced": False,
                            "orderId": "7249302000",
                            "orderLocation": {
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "orderTime": car_param["booking_time"],
                            "passengerName": "鲍洋",
                            "passengerPhone": "18912394254",
                            "realStartLocation": {
                                "direction": 0.0,
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "requireLevel": 4,
                            "startAddress": "",
                            "realStartAddress": None,
                            "startName": "",
                            "startServiceTime": car_param['strive_time'],
                            "status": 7,  # 待支付
                            "striveTime": car_param['strive_time'],
                            "toLocation": {
                                "lat": 30.982883,
                                "lng": 121.23012
                            },
                            "realEndLocation": None,
                            "type": 1,  #实时单
                            "flightNumber": None,
                            "canceledTime": None,
                            "finishTime": car_param['finish_time'],
                            "payTime": None,
                            "normalDistance": None,
                            "normalTime": None
                        },
                        "driverInfoVo": {
                            "avatar": None,
                            "carId": 900006302,
                            "carType": "S60L E驱混动",
                            "card": "浙A7189",
                            "color": "红色",
                            "id": 100001081,
                            "level": "5.0",
                            "location": {
                                "lat": car_param['dlat'],
                                "lng": car_param['dlng']
                            },
                            "name": "田师傅",
                            "orderCnt": 16,
                            "phone": "13826193851"
                        },
                        "orderFeeVo": {
                            "detailFeeVos": [{
                                "amount": 0,
                                "chargeCode": "start_fee",
                                "chargeDesc": "订单起步价"
                            }],
                            "originTotalFee": 0,
                            "totalFee": 10102
                        }
                    },
                    "code": 200,
                    "success": True,
                    "msg": None
                }

    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——取消(司机接单后取消费用)
def mock_carcannel_zhixing():
    response_json = {
                    "code": 200,
                    "success": True,
                    "data": { "cancelFee": "111" }
                    # "code": 22005,
                    # "success": False,
                    # "data": {" cancelFee ": "0"},
                    # "msg":"订单已取消"
                }
    # 异常
    # response_json = {
    #                   "code": "4001",
    #                   "message": "fail",
    #                   "data": {
    #                     "cost": 0.0
    #                   }
    #                 }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——取消(未接单取消无取消费用)
def mock_carcannel1_zhixing():
    response_json = {
                    "code": 200,
                    "success": True,
                    "data": { "cancelFee": "0" }
                    # "code": 22005,
                    # "success": False,
                    # "data": {" cancelFee ": "0"},
                    # "msg":"订单已取消"
                }
    # 异常
    # response_json = {
    #                   "code": "4001",
    #                   "message": "fail",
    #                   "data": {
    #                     "cost": 0.0
    #                   }
    #                 }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——取消费用查询
def mock_cancelorderfee_zhixing():
    response_json = {
                    "code": 200,
                    "success": True,
                    "data": { "cancelFee": "111" }
                }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——询价
def mock_carestimateprice_zhixing():
    response_json = {
                      "data": [
                        {
                          "carType": 1,
                          "distance": 7706,
                          "duration": 1505,
                          "name": "经济型",
                          "vendorDetails": [
                            {
                              "vendorId": "996",
                              "vendorName": "曹操出行",
                              "price": "20100",
                              "priceKey": "03dcab48-b2a9-42ed-91c1-4e767de199c0",
                              "detail": [
                                {
                                  "amount": 11,
                                  "chargeCode": "start_fee",
                                  "chargeDesc": "订单起步价"
                                },
                                {
                                  "amount": 0,
                                  "chargeCode": "travel_km_fee",
                                  "chargeDesc": "路长费用"
                                },
                                {
                                  "amount": 242,
                                  "chargeCode": "travel_minute_fee",
                                  "chargeDesc": "时间费用"
                                },
                                {
                                  "amount": 0,
                                  "chargeCode": "long_km_fee",
                                  "chargeDesc": "订单长途费用"
                                },
                                {
                                  "amount": 25,
                                  "chargeCode": "discount_fee",
                                  "chargeDesc": "折扣金额"
                                }
                              ]
                            },
                            {
                              "vendorId": "998",
                              "vendorName": "首汽用车",
                              "price": "20200",
                              "priceKey": "03dcab48-b2a9-42ed-91c1-4e767de199c0",
                              "detail": [
                                {
                                  "amount": 11,
                                  "chargeCode": "start_fee",
                                  "chargeDesc": "订单起步价"
                                },
                                {
                                  "amount": 0,
                                  "chargeCode": "travel_km_fee",
                                  "chargeDesc": "路长费用"
                                },
                                {
                                  "amount": 242,
                                  "chargeCode": "travel_minute_fee",
                                  "chargeDesc": "时间费用"
                                },
                                {
                                  "amount": 0,
                                  "chargeCode": "long_km_fee",
                                  "chargeDesc": "订单长途费用"
                                },
                                {
                                  "amount": 25,
                                  "chargeCode": "discount_fee",
                                  "chargeDesc": "折扣金额"
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "carType": 2,
                          "distance": 7706,
                          "duration": 1505,
                          "name": "舒适型",
                          "vendorDetails": [
                            {
                              "vendorId": "996",
                              "vendorName": "曹操出行",
                              "price": "752",
                              "priceKey": "a5115e44-b894-4b6e-a6e4-87f30584ba89",
                              "detail": [
                                {
                                  "amount": 1000,
                                  "chargeCode": "start_fee",
                                  "chargeDesc": "订单起步价"
                                },
                                {
                                  "amount": 6710,
                                  "chargeCode": "travel_km_fee",
                                  "chargeDesc": "路长费用"
                                },
                                {
                                  "amount": 2400,
                                  "chargeCode": "travel_minute_fee",
                                  "chargeDesc": "时间费用"
                                },
                                {
                                  "amount": 77100,
                                  "chargeCode": "long_km_fee",
                                  "chargeDesc": "订单长途费用"
                                },
                                {
                                  "amount": 1000,
                                  "chargeCode": "discount_fee",
                                  "chargeDesc": "折扣金额"
                                }
                              ]
                            },
                            {
                              "vendorId": "998",
                              "vendorName": "首汽用车",
                              "price": "852",
                              "priceKey": "a5115e44-b894-4b6e-a6e4-87f30584ba89",
                              "detail": [
                                {
                                  "amount": 1000,
                                  "chargeCode": "start_fee",
                                  "chargeDesc": "订单起步价"
                                },
                                {
                                  "amount": 6710,
                                  "chargeCode": "travel_km_fee",
                                  "chargeDesc": "路长费用"
                                },
                                {
                                  "amount": 2400,
                                  "chargeCode": "travel_minute_fee",
                                  "chargeDesc": "时间费用"
                                },
                                {
                                  "amount": 77100,
                                  "chargeCode": "long_km_fee",
                                  "chargeDesc": "订单长途费用"
                                },
                                {
                                  "amount": 1000,
                                  "chargeCode": "discount_fee",
                                  "chargeDesc": "折扣金额"
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "carType": 3,
                          "distance": 7706,
                          "duration": 1505,
                          "name": "商务型",
                          "vendorDetails": [
                            {
                              "vendorId": "996",
                              "vendorName": "曹操出行",
                              "price": "5500",
                              "priceKey": "f4a869d8-b303-4c98-a133-2c5fc3152114",
                              "detail": []
                            },
                            {
                              "vendorId": "998",
                              "vendorName": "首汽用车",
                              "price": "5600",
                              "priceKey": "f4a869d8-b303-4c98-a133-2c5fc3152114",
                              "detail": []
                            },
                          ]
                        },
                        {
                          "carType": 4,
                          "distance": 7706,
                          "duration": 1505,
                          "name": "豪华型",
                          "vendorDetails": [
                            {
                              "vendorId": "996",
                              "vendorName": "曹操出行",
                              "price": "11001",
                              "priceKey": "2a3498ec-32be-43bb-baed-394a605fb5fc",
                              "detail": [
                                {
                                  "amount": 11,
                                  "chargeCode": "start_fee",
                                  "chargeDesc": "订单起步价"
                                },
                                {
                                  "amount": 0,
                                  "chargeCode": "travel_km_fee",
                                  "chargeDesc": "路长费用"
                                },
                                {
                                  "amount": 242,
                                  "chargeCode": "travel_minute_fee",
                                  "chargeDesc": "时间费用"
                                },
                                {
                                  "amount": 0,
                                  "chargeCode": "long_km_fee",
                                  "chargeDesc": "订单长途费用"
                                },
                                {
                                  "amount": 25,
                                  "chargeCode": "discount_fee",
                                  "chargeDesc": "折扣金额"
                                }
                              ]
                            },
                            {
                              "vendorId": "998",
                              "vendorName": "首汽用车",
                              "price": "11101",
                              "priceKey": "2a3498ec-32be-43bb-baed-394a605fb5fc",
                              "detail": [
                                {
                                  "amount": 11,
                                  "chargeCode": "start_fee",
                                  "chargeDesc": "订单起步价"
                                },
                                {
                                  "amount": 0,
                                  "chargeCode": "travel_km_fee",
                                  "chargeDesc": "路长费用"
                                },
                                {
                                  "amount": 242,
                                  "chargeCode": "travel_minute_fee",
                                  "chargeDesc": "时间费用"
                                },
                                {
                                  "amount": 0,
                                  "chargeCode": "long_km_fee",
                                  "chargeDesc": "订单长途费用"
                                },
                                {
                                  "amount": 25,
                                  "chargeCode": "discount_fee",
                                  "chargeDesc": "折扣金额"
                                }
                              ]
                            }
                          ]
                        }
                      ],
                      "code": 200,
                      "success": True,
                      "msg": None
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——司机位置
def mock_cardriverlocation_zhixing(param,car_param):
    response_json = {
                      "data": {
                        "direction": 294.960938,
                        "latitude": car_param['dlat'],
                        "longitude": car_param['dlng']
                      },
                      "code": 200,
                      "success": True,
                      "msg": None
                    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——异常单子简单返回处理
def mock_carelse_zhixing(param,car_param):
    no = param
    strive_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json = {
                    "data": {
                        "basicOrderVO": {
                            "callerPhone": "18912394254",
                            "cityCode": "2",
                            "departureTime": car_param["booking_time"],
                            "endAddress": "盐仓路",
                            "endName": "",
                            "realEndAddress": None,
                            "beginChargeTime": None,
                            "estimatePrice": 12000,
                            "extOrderId": car_param['cap_uid'],
                            "otaOrderId": "7249302000",
                            "extraInfo": "",
                            "features": {
                                "start_name": "鲁能国际中心C座",
                                "o_cbi": "null",
                                "o_bsl": "b84c1ed2ca6c70f9",
                                "end_name": "松江南站",
                                "reassigned": "0",
                                "is_c": None
                            },
                            "fromLocation": {
                                "lat": 31.181364,
                                "lng": 121.48687
                            },
                            "invoiceStatus": 0,
                            "invoiced": False,
                            "orderId": "7249302000",
                            "orderLocation": {
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "orderTime": car_param["booking_time"],
                            "passengerName": "鲍洋",
                            "passengerPhone": "18912394254",
                            "realStartLocation": {
                                "direction": 0.0,
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "requireLevel": 4,
                            "startAddress": "",
                            "realStartAddress": None,
                            "startName": "",
                            "startServiceTime": strive_time,
                            "status": 2,  # 已派单
                            "striveTime": strive_time,
                            "toLocation": {
                                "lat": 30.982883,
                                "lng": 121.23012
                            },
                            "realEndLocation": None,
                            "type": 1,  #实时单
                            "flightNumber": None,
                            "canceledTime": None,
                            "finishTime": None,
                            "payTime": None,
                            "normalDistance": None,
                            "normalTime": None
                        },
                        "driverInfoVo": {
                            "avatar": None,
                            "carId": 900006302,
                            "carType": "S60L E驱混动",
                            "card": "浙A7189",
                            "color": "红色",
                            "id": 100001081,
                            "level": "5.0",
                            "location": {
                                "lat": car_param['dlat'],
                                "lng": car_param['dlng']
                            },
                            "name": "田师傅",
                            "orderCnt": 16,
                            "phone": "13826193851"
                        },
                        "orderFeeVo": {
                            "detailFeeVos": [{
                                "amount": 0,
                                "chargeCode": "start_fee",
                                "chargeDesc": "订单起步价"
                            }],
                            "originTotalFee": 0,
                            "totalFee": 12000
                        }
                    },
                    "code": 200,
                    "success": True,
                    "msg": None
                }
    # time.sleep(2.5)
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——供应商取消
def mock_carcannel_supplier_zhixing(param,car_param):
    no = param
    response_json = {
                    "data": {
                        "basicOrderVO": {
                            "callerPhone": "18912394254",
                            "cityCode": "2",
                            "departureTime": car_param["booking_time"],
                            "endAddress": "盐仓路",
                            "endName": "",
                            "realEndAddress": None,
                            "beginChargeTime": None,
                            "estimatePrice": 12000,
                            "extOrderId": car_param['cap_uid'],
                            "otaOrderId": "7249302000",
                            "extraInfo": "",
                            "features": {
                                "start_name": "鲁能国际中心C座",
                                "o_cbi": "null",
                                "o_bsl": "b84c1ed2ca6c70f9",
                                "end_name": "松江南站",
                                "reassigned": "0",
                                "is_c": None
                            },
                            "fromLocation": {
                                "lat": 31.181364,
                                "lng": 121.48687
                            },
                            "invoiceStatus": 0,
                            "invoiced": False,
                            "orderId": "7249302000",
                            "orderLocation": {
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "orderTime": car_param["booking_time"],
                            "passengerName": "鲍洋",
                            "passengerPhone": "18912394254",
                            "realStartLocation": {
                                "direction": 0.0,
                                "lat": 0.0,
                                "lng": 0.0
                            },
                            "requireLevel": 4,
                            "startAddress": "",
                            "realStartAddress": None,
                            "startName": "",
                            "startServiceTime": car_param['strive_time'],
                            "status": 4,  # 取消
                            "striveTime": car_param['strive_time'],
                            "toLocation": {
                                "lat": 30.982883,
                                "lng": 121.23012
                            },
                            "realEndLocation": None,
                            "type": 1,  #实时单
                            "flightNumber": None,
                            "canceledTime": None,
                            "finishTime": None,
                            "payTime": None,
                            "normalDistance": None,
                            "normalTime": None
                        },
                        "driverInfoVo": {
                            "avatar": None,
                            "carId": 900006302,
                            "carType": "S60L E驱混动",
                            "card": "浙A7189",
                            "color": "红色",
                            "id": 100001081,
                            "level": "5.0",
                            "location": {
                                "lat": car_param['dlat'],
                                "lng": car_param['dlng']
                            },
                            "name": "田师傅",
                            "orderCnt": 16,
                            "phone": "13826193851"
                        },
                        "orderFeeVo": {
                            "detailFeeVos": [{
                                "amount": 0,
                                "chargeCode": "start_fee",
                                "chargeDesc": "订单起步价"
                            }],
                            "originTotalFee": 0,
                            "totalFee": 12000
                        }
                    },
                    "code": 200,
                    "success": True,
                    "msg": None
                }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()
# 智行——确认费用
def mock_carpaynotice_supplier_zhixing():
    response_json = {
                      "code":200,
                      "success":True,
                      "msg":None
    }
    mock_response = Mock(return_value=response_json)
    print("返回:%s" % mock_response())
    return mock_response()