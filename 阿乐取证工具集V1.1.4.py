from tkinter import *
from tkinter import ttk
import requests
import pandas as pd
import urllib3
from jsoncsv.jsontool import *
import fake_useragent
import threading
import time
import random

ua = fake_useragent.UserAgent()


class GUI:
    def __init__(self, my_window):
        self.my_window = my_window
        self.url = None
        self.cookie = None
        self.referer = None
        self.useragent = None
        self.variate = None
        self.page = None
        self.td_num = None
        self.tm_num = None
        self.log = None
        self.tk_num = None

    def setting(self):
        # 设置标题
        self.my_window.title('阿乐数据采集器v1.1.3    BY: Alenm    773593595@qq.com')
        # 设置窗口大小
        width = 1200
        height = 700
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
        Label(self.my_window, text="线程数", width=10, height=1).pack()
        self.td_num = ttk.Combobox(self.my_window, width=20, height=7)
        self.td_num['value'] = ('1', '2', '4', '6', '8', '10', '12', '16', '24', '48')
        self.td_num.current(2)
        self.td_num.pack()
        # 下拉框颜色
        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='alt',
                                settings=
                                {'TCombobox':
                                    {'configure':
                                        {
                                            'foreground': 'blue',  # 前景色
                                            'selectbackground': 'black',  # 选择后的背景颜色
                                            'fieldbackground': 'white',  # 下拉框颜色
                                            'background': 'grey'  # 下拉按钮颜色
                                        }}}
                                )
        combostyle.theme_use('combostyle')
        Label(self.my_window, text="请求延时", width=10, height=1).pack()
        self.tm_num = ttk.Combobox(self.my_window, width=20, height=7)
        self.tm_num['value'] = ('0', '0.5', '1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '4.5', '5.0', '其他手填')
        self.tm_num.current(0)
        self.tm_num.pack()
        Label(self.my_window, text="扩展名", width=10, height=1).pack()
        self.tk_num = ttk.Combobox(self.my_window, width=20, height=7)
        self.tk_num['value'] = ('无扩展名', 'html', 'php', 'jsp', 'asp', '其他手填')
        self.tk_num.current(0)
        self.tk_num.pack()
        Label(self.my_window, text="", width=10, height=1).pack()
        Button(self.my_window, text="start", bg="lightblue", width=10, height=2, command=self.start_spider).pack()
        # Label(self.my_window, text="", width=8, height=1).pack()
        Label(self.my_window, text="log", width=10, height=2).pack()
        self.log = Text(self.my_window, width=80, height=8)
        self.log.pack()
        self.my_window.mainloop()
        num = self.td_num.get()
        print(num)

    def run_i(self, start, end):
        url = self.url.get(1.0, END).strip().replace("\n", "")
        cookie = self.cookie.get(1.0, END).strip().replace("\n", "")
        referer = self.referer.get(1.0, END).strip().replace("\n", "")
        if referer == '':
            referer = url
        else:
            pass
        if self.useragent.get(1.0, END).strip().replace("\n", "") == '':
            useragent = ua.random
        else:
            useragent = self.useragent.get(1.0, END).strip().replace("\n", "")
        variate = self.variate.get(1.0, END).strip().replace("\n", "")
        # page = self.page.get(1.0, END).strip().replace("\n", "")
        # log = self.log.get(1.0, END).strip().replace("\n", "")
        # 移除首尾的空格
        # 检查输出内容
        print(url)
        print(cookie)
        print(referer)
        print(useragent)
        print(variate)
        print(start)
        print(end)
        # print(page)
        headers = {
            'Cookie': cookie,
            'User-Agent': useragent,
            'Referer': referer
        }
        # page = int(page)
        self.log.delete(1.0, END)
        tm_num = float(self.tm_num.get())
        tk_num = self.tk_num.get()
        if tk_num == '无扩展名':
            tk_num = ''
        else:
            tk_num = '.' + tk_num
        if tm_num == 0:
            sleep_t = 0
        else:
            sleep_t = random.uniform(tm_num - 0.49, tm_num)
        for i in range(start, end):
            if variate != '':
                url_new = url + '&' + variate + '=' + str(i) + tk_num
            else:
                url_new = url + str(i) + tk_num
            print(url_new)
            urllib3.disable_warnings()
            response = requests.get(url_new, headers=headers, verify=False)
            # print(response.content.decode('UTF-8'))
            f = open("page" + str(i) + ".html", 'w', encoding='UTF-8')
            f.write(response.content.decode('UTF-8'))
            f.close()
            # 请求完延时一下，防止被反爬
            time.sleep(sleep_t)
            try:
                data = pd.DataFrame()
                data = data.append(pd.read_html("page" + str(i) + ".html", encoding='UTF-8'), ignore_index=True)
                print(data)
                data.to_csv('data.csv', encoding='utf_8_sig', mode='a')
                # logmsg0 = url + "\n"
                # logmsg1 = cookie + "\n"
                # logmsg2 = referer + "\n"
                # logmsg3 = useragent + "\n"
                # logmsg4 = variate + "\n"
                # logmsg5 = str(page) + "\n"
                logmsg6 = url_new + "\n"
                logmsg7 = '当前第' + str(i) + '页' + "\n"
                # self.log.insert(END, logmsg0)
                # self.log.insert(END, logmsg1)
                # self.log.insert(END, logmsg2)
                # self.log.insert(END, logmsg3)
                # self.log.insert(END, logmsg4)
                # self.log.insert(END, logmsg5)
                self.log.insert(END, logmsg6)
                self.log.insert(END, logmsg7)
            except:
                try:
                    # p = os.popen('jsoncsv page' + str(i) + '.html data.csv', mode='r')
                    # # 这里可以加一些报错，比如csv正在被别的程序打开
                    # logmsg9 = '当前取的是json格式，第' + str(i) + '页' + "\n"
                    # self.log.insert(END, logmsg9)
                    # p.close()
                    # os.system('jsoncsv page' + str(i) + '.html data.csv')
                    # logmsg9 = '当前取的是json格式，第' + str(i) + '页' + "\n"
                    # self.log.insert(END, logmsg9)
                    df = pd.read_json('page' + str(i) + '.html')
                    df.to_csv('data1.csv', encoding='utf_8_sig', mode='a+')
                    logmsg9 = '当前取的是json格式，第' + str(i) + '页' + "\n"
                    self.log.insert(END, logmsg9)
                    c = open('page' + str(i) + '.html', 'r', encoding='UTF-8')
                    d = open('data2.csv', 'a+', encoding='UTF-8')
                    try:
                        convert_json(c, d, expand, separator=".", safe=False, json_array=False)
                        c.close()
                        d.close()
                        # jsoncsv.jsontool里面研究了一下里面的convert_json, expand是{}，restore[]
                    except:
                        convert_json(c, d, restore, separator=".", safe=False, json_array=False)
                        c.close()
                        d.close()
                except:
                    logmsg10 = '当前爬取的页面中不包含表格，仅保存响应的页面' + "\n"
                    self.log.insert(END, logmsg10)

    # @staticmethod
    # def thread_it(func, *args):
    #     t = threading.Thread(target=func, args=args)
    #     t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
    #     t.start()  # 启动
    #     # t.join()          # 阻塞--会卡死界面！

    # 分配线程任务
    # @staticmethod

    def start_spider(self):
        num = self.td_num.get()
        # num = self.td_num['value'][]
        print(num)
        num = int(num)
        start = 0
        end = 0
        count = self.page.get(1.0, END).strip().replace("\n", "")
        count = int(count)
        if num != 1:
            size = count // (num - 1)
            print(size)
            while num > 2:
                end = start + size
                print(start)
                print(end)
                t = threading.Thread(target=self.run_i, args=(start+1, end))
                t.start()
                start = end
                num = num - 1

            # 分配剩下的任务给新的线程
            # if num <= 1 & end < count:
            #     end = count
            #     self.p = [start, end]
            #     t = threading.Thread(target=self.run_i)
            #     t.setDaemon(True)
            #     t.start()
            if end <= count:
                end = count + 1
                t = threading.Thread(target=self.run_i, args=(start+1, end))
                t.start()
        if num == 1:
            end = count + 1
            t = threading.Thread(target=self.run_i, args=(1, end))
            t.start()


def gui_start():
    my_window = Tk()
    # 实例化出一个父窗口
    new = GUI(my_window)
    # 设置根窗口默认属性
    new.setting()
    my_window.mainloop()

    # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()

# __init__ 和 __int__不一样的，我日，这个错误半天没发现，我是傻逼 打包命令pyinstaller -F -w 阿乐数据采集器V1.1.1.py 打包命令pyinstaller -F -w -i 1.ico
# 阿乐数据采集器V1.1.1.py,可以加图标 https://blog.csdn.net/weixin_36165569/article/details/114430394 upx加壳打包 pyinstaller
# --upx-dir=D:\ProgramData\Anaconda3\Lib\site-packages\PyInstallerupx-3.96-win64 -F -w -i 1.ico 阿乐数据采集器V1.1.1.py
# pyinstaller 打包过大 https://blog.csdn.net/p1967914901/article/details/109706449 pyinstaller
# --upx-dir=C:\Users\aa\.virtualenvs\Py_Project\Scripts\PyInstaller -F -w -i 1.ico D:\Py_Project\CJ\阿乐数据采集器V1.1.1.py
# 新的python环境，需要request， pandas， lxml包, 打包出来30多mb
# 修改环境中导入的jsoncsv，把main中的wb+改成a+，就是可以在csv中尾部写入新数据不清空原来的数据。需要删除_pyache_重新编译
# os.propen, os.system 这两个不能把jsoncsv打包进去。还是直接把jsoncsv的包复制进项目，用里面的jsontool，研究下需要什么参数就可以用了
# 运行时间长总是会卡死，虽然后台在运行，但是程序会跳出来未响应 https://www.cnblogs.com/hhh5460/p/5186819.html
# 打包进线程后好像关闭会提示可以还原，但是程序还是会有未响应的情况，虽然后台任然在运行
# 目前存在的问题：1.url如果是0.0.0.0/../page1.html这种情况不能够拼接。之前只考虑了0.0.0.0/../abc?type=1&page=1这种情况。5/19已解决
# 2.多线程没有解决。需要同时爬不同的网页，（获取到的网页内容，处理网页内容成为csv也需要同时能够处理） 5/18 已解决
# 反爬：已经做了随机ua，后面需要加入ip代理池，随机的等待时间（避免固定频率）https://zhuanlan.zhihu.com/p/150320164
# 参考https://gitee.com/chengrongkai/OpenSpiders/blob/master/qianchengwuyouSpider/requestMethod.py
# 多线程出现的新问题，保存的csv顺序是乱的。解决：边爬边处理，处理完了按顺序再遍历一次保存的页面，形成一个顺序的表格
# 需要把延时设置成下拉框来选择。0-1的随机延时可能不够
# 保存的文件还是放到一个新的文件夹比较好，最好还是可以手动选择目录
# 一种不多见的拼接方式 0.0.0.0/index.php?page=2，可以满足，url填写 0.0.0.0/index.php?
# 后面再加一个时间，计算时间的，再加计算哈希，日志等报告的
# 遇到了requests.exceptions.SSLError: HTTPSConnectionPool的问题，https://blog.csdn.net/ywj_486/article/details/106479003
# 安装
# requests.get('http://xxx.com/', headers = header, verify=False)
# pip install cryptography
#
# pip install pyOpenSSL
#
# pip install certifi
# 导入urllib3包
# import urllib3
# urllib3.disable_warnings() #这个添加在 requests.get('http://xxx.com/', headers = header, verify=False)上面一行


# 0.0.0.0/page1
# 0.0.0.0/index?page1
# 0.0.0.0/page1.html
# 0.0.0.0/index?m=1&page=1
