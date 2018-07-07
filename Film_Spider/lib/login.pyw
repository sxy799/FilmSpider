from tkinter.messagebox import *
from tkinter import *
import pymysql as pymysql
import os
from tkinter.messagebox import showinfo


conn = pymysql.connect(host='127.0.0.1', user='root',
                       passwd='root', db='doubandb', charset='utf8')
cursor = conn.cursor()

# !/usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *
from  tkinter  import ttk

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']


def ShowRoot():
    top1 = tk.Toplevel()
    top1.title('管理员操作页面显示 ')
    top1.geometry("500x400")

    with open('Spider.log',"r+",encoding= "utf-8") as f:  # 默认模式为‘r’，只读模式
        print(f.encoding)
        for line in f:
            #line.decode("utf8", "ignore")
            text = tk.Label(top1, text=line)
            text.pack()
    top1.mainloop()


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (300, 200))
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        name = self.username.get()
        pwd = self.password.get()
        sql_select='''select user_pwd from user_info WHERE user_id="%s" '''%(name)
        cursor.execute(sql_select)
        if pwd == "".join(cursor.fetchone()):
            if name =="799":
               root.destroy()
               os.system("python index.pyw")
            elif name == "root":
                ShowRoot()
        else:
            showinfo(title='错误', message='账号或密码错误！')


root = Tk()
root.title('爬虫登录页面')
LoginPage(root)
root.mainloop()
