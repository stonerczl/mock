# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 17:23
# @Author  : huangkaiding

from django.http import JsonResponse, HttpResponse
from io import open


def policy_confirmation():
    """
    投保确认
    :return:
    """
    resp_success = '<?xml version="1.0" encoding="UTF-8"?> <ResultInfo> <Success>true</Success> ' \
                   '<PolicyNo>1001186844</PolicyNo> <OrderId>0</OrderId> </ResultInfo> '
    resp_fail = '<?xml version="1.0" encoding="UTF-8"?> <ResultInfo> <Success>false</Success> ' \
                '<Message>被保险人年龄不在承保范围内</Message> <OrderId>0</OrderId> </ResultInfo> '
    return HttpResponse(resp_success)


def policy_cancellation():
    """
    保单注销
    :return:
    """
    resp_success = '<?xml version="1.0" encoding="UTF-8"?> <ResultInfo> <Success>true</Success> ' \
                   '<PolicyNo>1001186844</PolicyNo> <OrderId>0</OrderId> </ResultInfo> '
    resp_fail = '<?xml version="1.0" encoding="UTF-8"?> <ResultInfo> <Success>false</Success> ' \
                '<Message>保单已生效</Message> <OrderId>0</OrderId> </ResultInfo> '
    return HttpResponse(resp_success)


def policy_printing():
    """
    保单打印
    :return:
    """
    with open('test.pdf', "rb") as my_pdf:
        return HttpResponse(my_pdf)
