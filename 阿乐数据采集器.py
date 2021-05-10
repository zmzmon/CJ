from tkinter import *
import requests
import pandas as pd


class GUI:
    def __init__(self, my_window):
        self.my_window = my_window
        self.url = None
        self.cookie = None
        self.referer = None
        self.useragent = None
        self.variate = None
        self.page = None
        self.log = None

    def setting(self):
        # 设置标题
        self.my_window.title('阿乐数据采集器v1.0    BY: Alenm    773593595@qq.com')
        # 设置窗口大小
        width = 900
        height = 600
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = self.my_window.winfo_screenwidth()
        screenheight = self.my_window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.my_window.geometry(alignstr)
        # 设置窗口是否可变长、宽，True：可变，False：不可变
        self.my_window.resizable(width=True, height=True)
        # 创建一个标签，显示文本
        Label(self.my_window, text="", width=8, height=1).pack()
        Label(self.my_window, text="url", width=10, height=1).pack()
        self.url = Text(self.my_window, width=80, height=1)
        self.url.pack()
        Label(self.my_window, text="cookie", width=10, height=1).pack()
        self.cookie = Text(self.my_window, width=80, height=1)
        self.cookie.pack()
        Label(self.my_window, text="referer", width=20, height=1).pack()
        self.referer = Text(self.my_window, width=80, height=1)
        self.referer.pack()
        Label(self.my_window, text="user-agent", width=20, height=1).pack()
        self.useragent = Text(self.my_window, width=80, height=1)
        self.useragent.pack()
        Label(self.my_window, text="variate", width=20, height=1).pack()
        self.variate = Text(self.my_window, width=80, height=1)
        self.variate.pack()
        Label(self.my_window, text="page", width=20, height=1).pack()
        self.page = Text(self.my_window, width=80, height=1)
        self.page.pack()
        Label(self.my_window, text="", width=10, height=2).pack()
        Button(self.my_window, text="start", bg="lightblue", width=10, height=2, command=self.run).pack()
        Label(self.my_window, text="", width=8, height=1).pack()
        Label(self.my_window, text="log", width=10, height=1).pack()
        self.log = Text(self.my_window, width=80, height=10)
        self.log.pack()
        # Label(self.my_window, text="Alenm：773593595@qq.com", width=40, height=1).pack()
        self.my_window.mainloop()

    def run(self):
        url = self.url.get(1.0, END).strip().replace("\n", "")
        cookie = self.cookie.get(1.0, END).strip().replace("\n", "")
        referer = self.referer.get(1.0, END).strip().replace("\n", "")
        useragent = self.useragent.get(1.0, END).strip().replace("\n", "")
        variate = self.variate.get(1.0, END).strip().replace("\n", "")
        page = self.page.get(1.0, END).strip().replace("\n", "")
        # log = self.log.get(1.0, END).strip().replace("\n", "")
        # 移除首尾的空格
        print(url)
        print(cookie)
        print(referer)
        print(useragent)
        print(variate)
        print(page)
        headers = {
            'Cookie': cookie,
            'User-Agent': useragent,
            'Referer': referer
        }
        page = int(page)
        self.log.delete(1.0, END)
        for i in range(1, page + 1):
            url_new = url + '&' + variate + '=' + str(i)
            print(url_new)
            response = requests.get(url_new, headers=headers)
            f = open("page" + str(i) + ".html", 'w', encoding='UTF-8')
            f.write(response.content.decode('UTF-8'))
            f.close()
            data = pd.DataFrame()
            data = data.append(pd.read_html("page" + str(i) + ".html", encoding='UTF-8'), ignore_index=True)
            print(data)
            data.to_csv('data.csv', encoding='utf_8_sig', mode='a')
            logmsg0 = url + "\n"
            logmsg1 = cookie + "\n"
            logmsg2 = referer + "\n"
            logmsg3 = useragent + "\n"
            logmsg4 = variate + "\n"
            logmsg5 = str(page) + "\n"
            logmsg6 = url_new + "\n"
            logmsg7 = '当前第' + str(i) + '页' + "\n"
            self.log.insert(END, logmsg0)
            self.log.insert(END, logmsg1)
            self.log.insert(END, logmsg2)
            self.log.insert(END, logmsg3)
            self.log.insert(END, logmsg4)
            self.log.insert(END, logmsg5)
            self.log.insert(END, logmsg6)
            self.log.insert(END, logmsg7)


def gui_start():
    my_window = Tk()
    # 实例化出一个父窗口
    new = GUI(my_window)
    # 设置根窗口默认属性
    new.setting()
    my_window.mainloop()
    # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()

# __init__ 和 __int__不一样的，我日，这个错误半天没发现，我是傻逼
# 打包命令pyinstaller -F -w 阿乐数据采集器.py
# 打包命令pyinstaller -F -w -i 1.ico 阿乐数据采集器.py,可以加图标
# https://blog.csdn.net/weixin_36165569/article/details/114430394 upx加壳打包
# pyinstaller --upx-dir=D:\ProgramData\Anaconda3\Lib\site-packages\PyInstallerupx-3.96-win64 -F -w -i 1.ico 阿乐数据采集器.py
# pyinstaller 打包过大 https://blog.csdn.net/p1967914901/article/details/109706449
# pyinstaller --upx-dir=C:\Users\aa\.virtualenvs\Py_Project\Scripts\PyInstaller -F -w -i 1.ico D:\Py_Project\CJ\阿乐数据采集器.py
# 新的python环境，需要request， pandas， lxml包, 打包出来30多mb
