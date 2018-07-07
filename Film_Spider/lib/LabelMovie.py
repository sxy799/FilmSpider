
import pymysql
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist.axislines as axislines
from collections import Counter
import numpy as np

def  ConnDB():
     conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='doubandb', charset='utf8')
     return conn

def SelectDB(conn):
    cursor = conn.cursor()
    sql = "select * from movie_info ;"
    print (sql)
    # 执行SQL语句
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results

def CountDateDB(conn):
    cursor = conn.cursor()
    sql = "SELECT movie_date,count(*)FROM  movie_info  group  BY movie_date;"
    # print(sql)
    # 执行SQL语句
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results

def CountTimeDB(conn):
    cursor = conn.cursor()
    sql = "SELECT movie_time,count(*)FROM  movie_info  group  BY movie_time;"
    # print(sql)
    # 执行SQL语句
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results

def CloseDB(conn):
    conn.close()



if __name__ == '__main__':

    fig = plt.figure(1, figsize=(10, 6))
    fig.subplots_adjust(bottom=0.2)

    #1. 连接数据库
    conn = ConnDB()

    #  子图1
    ax1 = axislines.Subplot(fig, 211)
    fig.add_subplot(ax1)
    results = []
    results = SelectDB(conn)
    for row in results:
       # print(row[3])
        ax1.scatter(row[1],row[3],s=int(row[2]) / 10)  # 第三个变量表明根据收入气泡的大
    #"豆瓣电影年份-评分图", FontProperties='STKAITI', fontsize=10)


    # # 子图2
    ax2 = axislines.Subplot(fig, 223)
    fig.add_subplot(ax2)

    results = []
    results = CountDateDB(conn)
    labels =  [x[0] for x in results]
    # 每个标签占多大，会自动去算百分比
    sizes =  [x[1] for x in results]
    patches, l_text, p_text = plt.pie(sizes,  labels=labels,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.6)
    for t in l_text:
        t.set_size = (30)
    for t in p_text:
        t.set_size = (20)
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.suptitle("豆瓣电影年份-饼图", FontProperties='STKAITI', fontsize=10)

    # # 子图3
    ax2 = axislines.Subplot(fig, 224)
    fig.add_subplot(ax2)
    results = []
    results = CountTimeDB(conn)
    labels = [x[0] for x in results]
    # 每个标签占多大，会自动去算百分比
    sizes = [x[1] for x in results]
    patches, l_text, p_text = plt.pie(sizes, labels=labels,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.6)
    for t in l_text:
        t.set_size = (30)
    for t in p_text:
        t.set_size = (20)
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.suptitle("豆瓣电影时长-饼图", FontProperties='STKAITI', fontsize=10)

    plt.show()

    CloseDB(conn)