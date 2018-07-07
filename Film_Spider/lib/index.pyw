
import tkinter as tk
import pymysql
from tkinter import *
from  tkinter  import ttk
import tkinter.messagebox #这个是消息框，对话框的关键


import Search
import SearchMovie
import SearchActor
import draw
import Logging

mylog=Logging.MyLog()


database_dict = {
	'剧情': 'movie_info1',
	'喜剧': 'movie_info2',
	'动作': 'movie_info3',
	'爱情': 'movie_info4',
	'科幻': 'movie_info5',
	'悬疑': 'movie_info6',
	'惊悚': 'movie_info7',
	'恐怖': 'movie_info8',
	'犯罪': 'movie_info9',
	'同性': 'movie_info10',
	'音乐': 'movie_info11',
	'歌舞': 'movie_info12',
	'传记': 'movie_info13',
	'历史': 'movie_info14',
	'战争': 'movie_info15',
	'西部': 'movie_info16',
	'奇幻': 'movie_info17',
	'冒险': 'movie_info18',
	'灾难': 'movie_info19',
	'武侠': 'movie_info20',
	'情色': 'movie_info21'
}


def show1():
    mylog.info('查看' +  number.get() + '标签电影数据 ')
    top1 = tk.Toplevel()

    top1.title('所选' +  number.get() + '标签电影数据 ')
    top1.geometry("500x400")
    listboxStudents = tk.Listbox(top1, width=300)
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='doubandb', charset='utf8')
    sql_select = '''SELECT * FROM  '''+ database_dict[number.get()]
    cursor = conn.cursor()
    cursor.execute(sql_select)
    for u in cursor.fetchall():
        result = 'Name : ' + u[0]
        result = result + ' ;Date: ' + str(u[1])
        result = result + ' ;Time; ' + str(u[2])
        result = result + ' ;Duration: ' + u[3]
        listboxStudents.insert(0, result)

    listboxStudents.place(x=10, y=30, width=300, height=200)
    top1.mainloop()


def show2():
   mylog.info('可视化' + number.get() + '标签电影数据 ')
   draw.main( database_dict[number.get()] )


def show3():
    mylog.info('搜索' + t1.get() )
    top1 = tk.Toplevel()
    top1.title('搜索' + t1.get() + '结果显示 ')
    top1.geometry("500x400")
    judge,url = Search.Input_Main(t1.get())
    if judge == 0:
        type = tk.Label(top1, text="影人")
        type.pack()
        b1 = ttk.Button(top1, text="基本信息", command=lambda : SearchActor.Get_Actor_Info(url = url))  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        b1.pack()
        b2 = ttk.Button(top1, text="主演电影评分", command=lambda :SearchActor.Get_Actor_Movie(url = url))  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        b2.pack()
        b3 = ttk.Button(top1, text="合作的影人", command=lambda : SearchActor.Get_Actor_Partner(url = url))  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        b3.pack()
    elif judge == 1:
        type = tk.Label(top1, text="影片")
        type.pack()
        b1 = ttk.Button(top1, text="基本信息", command=lambda : SearchMovie.Get_Movie_Info(url = url))  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        b1.pack()
        b2 = ttk.Button(top1, text="豆瓣评分", command=lambda : SearchMovie.Get_Movie_Rate(url = url))  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        b2.pack()
        b3 = ttk.Button(top1, text="看过该电影的还喜欢", command=lambda : SearchMovie.Get_Movie_Recommend(url = url))  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        b3.pack()
        b3 = ttk.Button(top1, text="生成评论词云", command=lambda : SearchMovie.Get_Movie_Comment(url = url))  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        b3.pack()
    else:
        tk.messagebox.showinfo('警告', '没有找到关于 '+t1.get()+' 的电影，换个搜索词试试吧')
        t1.set('')
        top1.destroy()
    top1.mainloop()


def  show4():
    tk.messagebox.showinfo('提示', '重置成功')
    t1.set('')

url = ""

# # ====================   Create instance =====================================
root = tk.Tk()

# Add a title
root.title("Python 图形用户界面")

# # Disable resizing the GUI
root.geometry("500x400")
root.geometry("+450+250")
root.resizable(0, 0)

#----------------------- Tab Control introduced here --------------------------
tabControl = ttk.Notebook(root)  # Create Tab Control

up= ttk.Frame(tabControl)  # Create a tab
tabControl.add(up, text='分类')  # Add the tab

down = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(down, text='搜索')  # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# ---------------UP 控件介绍------------------#

aa = tk.Label(up, text="\n\n请选择电影标签")
aa.pack()

# 创建一个下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(up, width=12, textvariable=number)
numberChosen['values'] = ('剧情','喜剧','动作','爱情','科幻','悬疑','惊悚','恐怖','犯罪','同性','音乐','歌舞','传记','历史','战争')     # 设置下拉列表的值
numberChosen.pack()    # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值


action = ttk.Button(up, text="查看数据", command=show1)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.pack()    # 设置其在界面中出现的位置  column代表列   row 代表行
action1 = ttk.Button(up, text="数据可视化", command=show2)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action1.pack()   # 设置其在界面中出现的位置  column代表列   row 代表行





# ---------------DOWN 控件介绍------------------#
aa = tk.Label(down, text="\n\n搜索影人或者影片")
aa.pack()
t1 = tk.StringVar()
t1.set('')
entry = tk.Entry(down, textvariable = t1).pack()
# print (t1.get())
action = ttk.Button(down, text="确定", command=show3)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.pack()   # 设置其在界面中出现的位置  column代表列   row 代表行
action1 = ttk.Button(down, text="重置", command=show4)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action1.pack()   # 设置其在界面中出现的位置  column代表列   row 代表行




# Change the main windows icon
root.iconbitmap('D:\Spider\Film_Spider\Film_Spider\img\\bitbug_favicon.ico')

# Place cursor into name Entry

# ======================
# Start GUI
# ======================
root.mainloop()