from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from faker import Faker
import json


def datagenerate(request):
    if request.method == "POST":
        request_data = request.body.decode()
        request_json = json.loads(request_data)
        res = datahandler(request_json)
        return HttpResponse(res)



#{
#    "dataname":["phone","certno","name"],
#	"amount":200
#}

def datahandler(request_json):
    data_dict = {"phone":"f.phone_number()","certno":"f.ssn()","name":"f.name()"}
    res_list = []
    f = Faker(locale='zh_CN')
    amount = request_json['amount'] # 数量
    dataname_list = request_json['dataname']
    dataname_len = len(dataname_list)
    for i in range(amount):
        for j in range(dataname_len):
            res = eval(data_dict[dataname_list[j]]) + ','
            res_list.append(res)
        res_list.append('\n')

    return res_list