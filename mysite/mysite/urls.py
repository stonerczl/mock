"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from mockmodel import views, testdata, dingding, views_flight
from apscheduler.schedulers.background import BackgroundScheduler

#[\s\S]*
urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^tmc-hub/[\s\S]*$', views.queryHotelLowestPrice1),
    # 航天
    path('cn_interface/tcTrain', views.trainsupplier),
    path('trainSearch', views.trainsupplier_search),
    # 极淼
    path('api/tcTrain/search', views.train_search_jimiao),
    path('api/tcTrain/order', views.train_book_jimiao),
    path('api/tcTrain/cancel', views.train_cancel_jimiao),
    path('api/tcTrain/returnTicket', views.train_returnTicket_jimiao),
    path('api/tcTrain/confirm', views.train_confirm_jimiao),
    path('api/tcTrain/cancleChange', views.train_cancleChange_jimiao),
    path('api/tcTrain/confirmChange', views.train_confirmChange_jimiao),
    path('api/tcTrain/requestChange', views.train_requestChange_jimiao),
    path('api/tcTrain/nightCancle', views.train_nightCancle_jimiao),
    path('payc-web/installment/prepay', views.trainprepay),
    # 数据仓库
    path('testdata', testdata.datagenerate),
    # 企业管家
    re_path('v1/all_taxis/[\s\S]*', views.carsupplier),
    path('v1/all_taxis', views.carsuppliercreate),
    # 智行
    path('v1/orderCar', views.carsuppliercreate_zhixing),
    path('v1/queryOrderDetail', views.carsupplier_zhixing),
    path('v1/cancelOrder', views.carsuppliercannel_zhixing),
    path('v1/estimatePriceWithDetail', views.carestimateprice_zhixing),
    path('v1/queryDriverLocationByOrderId', views.cardriverlocation_zhixing),
    path('v1/getCancelOrderFee', views.cancelorderfee_zhixing),
    path('v1/feeConfirm', views.paynotice_zhixing),
    path('ssish/ws', views_flight.policy_confirmation_api),
]


scheduler = BackgroundScheduler()
scheduler.add_job(dingding.order_dinner, 'cron', day_of_week='mon-fri', hour='16', minute='05')
scheduler.add_job(dingding.booking_dinner, 'cron', day_of_week='mon-fri', hour='13', minute='30')
scheduler.start()