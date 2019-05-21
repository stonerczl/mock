import random, os

def hotcity_list(trafficmode):
    hotcitylist = []
    # dir_parent = os.path.abspath(os.path.join(os.getcwd(), "../..")) #根据用例目录
    dir_parent = os.path.abspath(os.path.join(os.getcwd(), ".."))  # 根据用例目录
    print(dir_parent)
    if trafficmode == 'flight':
        file = dir_parent + r'\data\hotcity_flight.txt'
    elif trafficmode == 'train':
        file = dir_parent + r'\data\hotcity_train.txt'

    with open(file, 'r', encoding='UTF-8') as f:
        for i in f.readlines():
            i = i.strip('\n')
            hotcitylist.append(i)
    return hotcitylist


def choose_hotcity(trafficmode):
    hotcitylist = hotcity_list(trafficmode)
    # 无航班列表:北京天津\厦门深圳\武汉南京\武汉长沙\上海杭州\天津南京\青岛天津\杭州南京\深圳广州
    airline_no = ['BJSTSN', 'TSNBJS', 'SZXXMN', 'XMNSZX', 'WUHCSX', 'CSXWUH', 'WUHNKG', 'NKGWUH','HGHSHA','SHAHGH','TSNNKG','NKGTSN','TSNTAO','TAOTSN','HGHNKG','NKGHGH','SZXCAN','CANSZX']
    while True:
        choose_city = random.sample(hotcitylist, 2)
        temp = choose_city[0]+choose_city[1]
        if temp not in airline_no and trafficmode == 'flight':
            break
        elif trafficmode == 'train':
            break
    return choose_city[0], choose_city[1]


if __name__ == "__main__":
    froma,toa = choose_hotcity('train')
    froma = froma.split(',')[0]
    print(froma)