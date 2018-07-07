
from selenium import webdriver
import urllib.request
import urllib.error
import time

import urllib.request, re
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']



def  GetInputUrl(input):
        movie_search_engine = "http://movie.douban.com/subject_search?search_text=" + urllib.request.quote(input) + "&cat=1002"
        print("INPUT_URL : " + movie_search_engine + "\n")
        browser = webdriver.Chrome()  # Get local session of firefox
        browser.get(movie_search_engine)  # Load page
        time.sleep(1)
        try:
            # title-text
            ret = browser.find_elements_by_class_name('title-text')[0].get_attribute('href')
            print ("ANS_URL : " + ret)
        except IndexError:
             ret = ""
        browser.quit() #保证浏览器关闭
        return ret


def  Input_Main(input) :
    ans_url = GetInputUrl(input)
    res = ans_url.find("celebrity")
    if ans_url.find("celebrity") != -1:
        print("你查找的是影人")
        return 0,ans_url
    elif ans_url.find("subject") != -1:
        print("你查找的是电影")
        return 1, ans_url
    else:
        print("你查找的是不合法")
        return 2,""
