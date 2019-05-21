import datetime, random, time

def clear_time():
    paytime = datetime.datetime.now() + datetime.timedelta(minutes=25)
    paytime = paytime.strftime('%Y-%m-%d %H:%M:%S')
    return paytime

def req_time():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    stamp = ("".join(time_stamp.split()[0].split("-")) + "".join(time_stamp.split()[1].split(":"))).replace('.', '')
    return stamp

def time_stamp():
    stamp = int(time.time()*1000)
    return stamp

def mockcar_time_zhixing():
    orderid_time = datetime.datetime.now()
    orderid_time = orderid_time.strftime('%Y%m%d%H%M%S')
    return orderid_time

def mockcar_bookingtime_zhixing():
    bokingtime = datetime.datetime.now()
    bokingtime = bokingtime.strftime('%Y-%m-%d %H:%M:%S')
    return bokingtime

if __name__ == '__main__':
    print(time_stamp())