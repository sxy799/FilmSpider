
from lxml import etree
import requests
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
from tkinter import *
from  tkinter  import ttk


def  Get_Actor_Info(url):
    html = requests.get(url).content
    page = etree.HTML(html)
    info = page.xpath("//*[@id='headline']/div[2]/ul/li")
    title = (page.xpath("//*[@id='content']/h1/text()")[0]).split()[0]
    ret = []
    top1 = tk.Toplevel()
    top1.title('影人  :' + title + ' 基本信息显示 ')
    top1.geometry("500x400")

    for i in info:
        tmp=i.xpath('string(.)').strip()
        tmp = tmp.replace('\r', '').replace('\n', '').replace('\t', '')
        ret.append(tmp)
        text = tk.Label(top1, text=tmp)
        text.pack()
    print (ret)
    return ret

def  Get_Actor_Partner(url):
    html = requests.get(url).content
    page = etree.HTML(html)
    next_url = page.xpath("//*[@id='partners']/div[1]/h2/span/a/@href")[0]
    print("Parters_URL : " + next_url)

    ret=[]
    html = requests.get(next_url).content
    page = etree.HTML(html)
    info = page.xpath("//div[@class='partners item']")
    for i in info:
        per_ret = []
        per_ret.append(i.xpath(".// div[2] / h2 / a/text()")[0].split()[0])
        per_ret.append(re.findall(r"\d+\.?\d*",i.xpath(".// div[2] / ul / li[2] / text()[1]")[0])[0])
        ret.append(per_ret)

    # # 画图
    name_set = [x[0] for x in ret]
    times_set = [int(x[1]) for x in ret]

    fig = plt.figure(1)
    ax1 = plt.subplot(111)
    data = np.array(times_set)
    width = 0.5
    x_bar = np.arange(10)
    rect = ax1.bar(left=x_bar, height=data, width=width, color="lightblue")
    for rec in rect:
        x = rec.get_x()
        height = rec.get_height()
        ax1.text(x + 0.1, 1.02 * height, str(height))

    ax1.set_xticks(x_bar)
    ax1.set_xticklabels(name_set)
    ax1.set_ylabel("合作次数")
    ax1.set_title("与其合作的影人次数——条形图")
    ax1.grid(True)
    ax1.set_ylim(0, max(times_set) + 1)
    plt.show()

    print(ret)
    return  ret

def  Get_Actor_Movie(url):
    html = requests.get(url + "/movies").content
    page = etree.HTML(html)
    info = page.xpath(" // *[ @ id = 'content'] / div / div[1] / div[2] / ul / li")
    ret = []

    top1 = tk.Toplevel()
    top1.title('影人——主演电影信息显示 ')
    tree = ttk.Treeview(top1)  # 表格
    tree["columns"] = ("电影名字", "评分", "年份")
    tree.column("电影名字")  # 表示列,不显示
    tree.column("评分")
    tree.column("年份")
    tree.heading("电影名字", text="电影名字")  # 显示表头
    tree.heading("评分", text="豆瓣评分")
    tree.heading("年份", text="上映年份")
    ct = 0
    for i in info:
        per_ret = []
        per_ret.append(i.xpath(".//dl/dt/a/img/@title")[0])
        per_ret.append(i.xpath(".//dl/dd/div/span[2]/text()")[0])
        per_ret.append(re.findall(r"\d+\.?\d*",i.xpath(".//dl/dd/h6/span[1]/text()")[0])[0])
                   #  (re.findall(r"\d+\.?\d*", i.xpath(".// div[2] / ul / li[2] / text()[1]")[0])[0])
        ret.append(per_ret)

        tree.insert("",ct,text="第"+ str(ct+1) + "个",values=(per_ret[0],per_ret[1],per_ret[2])) #插入数据，
        ct+=1

    tree.pack()
    # ----vertical scrollbar------------
    vbar = ttk.Scrollbar(top1, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=vbar.set)
    tree.grid(row=0, column=0, sticky=NSEW)
    vbar.grid(row=0, column=1, sticky=NS)

    # ----horizontal scrollbar----------
    hbar = ttk.Scrollbar(top1, orient=HORIZONTAL, command=tree.xview)
    tree.configure(xscrollcommand=hbar.set)
    hbar.grid(row=1, column=0, sticky=EW)

    top1.mainloop()
    print (ret)

