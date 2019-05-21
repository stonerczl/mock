import pymysql

mysql_list = {"car":['10.33.16.34', 3363, 'car_sys_rw', 'xhy520', 'car_sys']}

def mysql_query(sql, instance):
    mysqldb = mysql_list[instance]
    # 打开数据库连接 car mysql
    db = pymysql.connect(host = mysqldb[0], port = mysqldb[1], user = mysqldb[2], passwd=mysqldb[3], db=mysqldb[4])
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute(sql)
    try:
        result = cursor.fetchall()[0]
    except:
        result = ('',)
    cursor.close()
    db.close()
    return result


if __name__ == '__main__':
    sql1 = "select child_order_id from car_child_order where business_order_id = 'BO01797161288181161'"
    sql2 = "select child_order_id from car_child_order where business_order_id = '11111'"
    sql = "select state,order_type,origin,origin_detail,destination,destination_detail,depart_latitude,depart_longitude,dest_latitude,dest_longitude from car_order where order_id = '104720181201153807653331655000' and member_id = '1180426025332159'"
    result = mysql_query(sql1, 'car')[0]
    print(result)
    print(type(result))
    result = mysql_query(sql2, 'car')[0]
    print(result)
    print(type(result))

