
from lxml import etree
import requests
import urllib.request, re, json
import mpl_toolkits.axisartist.axislines as axislines
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import tkinter as tk

def Get_Movie_Info(url):
    html = requests.get(url).content
    page = etree.HTML(html)
    title =(page.xpath("//*[@id='content']/h1/span[1]/text()")[0]).split()[0]
    info = page.xpath("//*[@id='info']")[0]
    movie ={}
    movie['director'] = info.xpath("./span[1]/span[2]/a/text()")[0]
    movie['screenwriter'] = info.xpath("./span[2]/span[2]/a/text()")[0]
    movie['actors'] = '/'.join(info.xpath("./span[3]/span[2]/a/text()"))
    movie['type'] = '/'.join(info.xpath("./span[@property='v:genre']/"
                                        "text()"))
    movie['initialReleaseDate'] = '/'. \
        join(info.xpath(".//span[@property='v:initialReleaseDate']/text()"))
    movie['runtime'] = \
        info.xpath(".//span[@property='v:runtime']/text()")[0]

    top1 = tk.Toplevel()
    top1.title('电影  :' + title + ' 基本信息显示 ')
    top1.geometry("500x400")

    text= tk.Label(top1, text="导演 :" +  movie['director'])
    text.pack()
    text = tk.Label(top1, text="编剧 ：" + movie['screenwriter'])
    text.pack()
    text = tk.Label(top1, text="演员 :" + movie['actors'])
    text.pack()
    text = tk.Label(top1, text="类型 :" + movie['type'])
    text.pack()
    text = tk.Label(top1, text="上映时间 :" +  movie['initialReleaseDate'])
    text.pack()
    text = tk.Label(top1, text="时长 :" + movie['runtime'])
    text.pack()

def Get_Movie_Rate(url):
    html = requests.get(url).content
    page = etree.HTML(html)
    title =(page.xpath("//*[@id='content']/h1/span[1]/text()")[0]).split()[0]
    info = page.xpath("//*[@id='info']")[0]
    movie ={}
    movie['director'] = info.xpath("./span[1]/span[2]/a/text()")[0]
    movie['screenwriter'] = info.xpath("./span[2]/span[2]/a/text()")[0]
    movie['actors'] = '/'.join(info.xpath("./span[3]/span[2]/a/text()"))
    movie['type'] = '/'.join(info.xpath("./span[@property='v:genre']/"
                                        "text()"))
    movie['initialReleaseDate'] = '/'. \
        join(info.xpath(".//span[@property='v:initialReleaseDate']/text()"))
    movie['runtime'] = \
        info.xpath(".//span[@property='v:runtime']/text()")[0]

    star = page.xpath("//*[@id='interest_sectl']")[0]
    movie['five_star'] = re.findall(r"\d+\.?\d*",star.xpath("./div[1]/div[3]/div[1]/span[2]/text()")[0])
    movie['four_star'] = re.findall(r"\d+\.?\d*",star.xpath("./div[1]/div[3]/div[2]/span[2]/text()")[0])
    movie['three_star'] = re.findall(r"\d+\.?\d*",star.xpath("./div[1]/div[3]/div[3]/span[2]/text()")[0])
    movie['two_star'] = re.findall(r"\d+\.?\d*",star.xpath("./div[1]/div[3]/div[4]/span[2]/text()")[0])
    movie['one_star'] = re.findall(r"\d+\.?\d*",star.xpath("./div[1]/div[3]/div[5]/span[2]/text()")[0])
    print (movie)

    #画图
    fig = plt.figure(1, figsize=(10, 6))
    fig.subplots_adjust(bottom=0.2)
    ax2 = axislines.Subplot(fig, 111)
    fig.add_subplot(ax2)


    labels =  ['一星','两星','三星','四星','五星']
    # 每个标签占多大，会自动去算百分比
    explode = [0, 0, 0, 0,0.05]  # 0.1 凸出这部分，
    sizes =  [movie['one_star'] ,movie['two_star'],movie['three_star'],movie['four_star'],movie['five_star']]
    patches, l_text, p_text = plt.pie(sizes,  labels=labels, explode=explode,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.6)
    for t in l_text:
        t.set_size = (30)
    for t in p_text:
        t.set_size = (20)
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.suptitle(title + "豆瓣评分-饼图", FontProperties='STKAITI', fontsize=24)

    plt.show()

    #print ("=======================================================")
    #return movie;


def Get_Movie_Recommend(url):
    html = requests.get(url).content
    page = etree.HTML(html)
    recom = []
    top1 = tk.Toplevel()
    top1.title('喜欢这个电影的还喜欢这些 ')
    top1.geometry("500x400")
    # print ("test : " +page.xpath("//*[@id='recommendations']/div/dl[1]/dd/a/text")[0] )
    for i in range(1,11):
       info = page.xpath("//*[@id='recommendations']/div/dl["+str(i)+"]/dd/a/text()")[0]
       text = tk.Label(top1, text=info )
       text.pack()
       recom.append(info)
    print ("=====================info==================================")
    print(recom)
    return recom;


def Get_Movie_Comment(url):
    html = requests.get(url).content
    page = etree.HTML(html)
    comment_url = page.xpath("//*[@id='comments-section']/div[1]/h2/span/a/@href")[0]
    print ("Comment_URL : " + comment_url)
    html = requests.get(comment_url).content
    page = etree.HTML(html)
    filename = 'jieba_data.txt'
    with open(filename, 'w',encoding="utf8") as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        comment_info = []
        info = page.xpath("//*[@id='comments']")[0]
        for k in range(1,21):
            # comment = {}
            # comment ['name'] = info.xpath("./ div["+str(k) + "] / div[2] / h3 / span[2] / a /text()")[0]
            # comment['href'] = info.xpath("./ div["+str(k) + "] / div[2] / h3 / span[2] / a /@href")[0]
            comment = info.xpath("./ div["+str(k) + "] / div[2] / p/text()")[0]
            f.write(comment + "\n")
           # comment_info.append(comment)
            print("=======================================================")
            print (comment)

    text_from_file_with_apath = open('jieba_data.txt', encoding='UTF-8').read()

    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    wc = WordCloud()
    wc.font_path = "simhei.ttf"  # 黑体e
    my_wordcloud = wc.generate(wl_space_split)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    return comment_info


