# 阿乐数据采集器

## 下载

*阿乐数据采集器V2.0 .exe（推荐使用最新版）*

[**高速下载**](https://pan.forensix.cn/f/4179987ab80b49cbb041/?dl=1)

* 新增调用绿色谷歌浏览器网页截图功能。
* 新增返回数据包含var XXX = {}的处理。
* 新增操作手册，演示视频。
* 解决返回数据是字典，但是没有引号，用处理json的方式出错。
* 解决没有浏览器，运行无法继续的问题。


----

*阿乐数据采集器V1.2 .exe*

[**高速下载**](https://pan.forensix.cn/f/fce87a35b60a46e0af98/?dl=1)

* 新增多线程爬取功能。
* 新增url构造的方式，不使用&连接的url。
* 新增json格式数据处理的方式，现在有两种处理方式，形成了两个csv文件。
* 新增不填写UA使用随机UA的功能，作为反爬虫的一些处理。
* 新增不填写referer使用请求的url作为referer。
* 新增请求延时功能，设置范围后在范围内选择随机的等待时间。
* 解决了带扩展名网站爬取报错的问题。
* 解决了https网站爬取报错的问题。
* 解决了线程数等于1时除数为0报错的问题。
* 解决了多线程时重复爬取页面导致表格产生重复数据问题。

----

*阿乐数据采集器V1.1 .exe*

[**高速下载**](https://pan.forensix.cn/f/fce87a35b60a46e0af98/?dl=1)

* 新增json格式的爬取，并转换成csv。

----

*阿乐数据采集器V1.0 .exe*

[**高速下载**](https://pan.forensix.cn/f/bd1d926cd54b4ec0a493/?dl=1)

* 目前只支持get请求，数据类型需要是标准的表格形式。
* 下个版本加入多线程，post请求，随机的useragent，支持json格式的爬取。

----

## 使用方法

[**使用说明视频下载（新）**](https://pan.forensix.cn/f/9a60d0a48b114466a770/?dl=1)

1.使用浏览器登陆后台页面，找到需要取的页面，如果是有框架的网站，右键框架仅显示此框架，或者F12找到真实的地址。进入F12审查，点击网络，从中查找cookie，useragent。

2.url中填入地址，去掉变动的参数，我测试的是 http://192.168.0.1/adm.php?m=carmodel&a=list&page=1 ， 则填入url为 http://192.168.0.1/adm.php?m=carmodel&a=list 。

3.cookie中填入cookie，例如SESSIONID=e1dc5fbd-5090-46f4-8e95-6b36884c8de0.QhpGbjQ1mMK__ILRyyy6pi9IBCk; PHPSESSID=ta6e8vr3k3ia81997fipo25ra5; order=1。

4.referer填写来源的网址，例如 http://192.168.0.1/adm.php?m=carmodel&a=list 。

5.useragent中填浏览器的标识，例如Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0 。
 
6.variate中填写变量，比如url中第一页page=1，第二页page=2，这里填写page。

7.page填写页数，例如100。可以参照截图中的填写方式，后面的版本填写时会进行提示。

----

## 性能测试

我自己测试的网站，PHP做的cms，里面有表格。服务器配置是腾讯云轻量级服务器，2核2g内存，带宽5m。网络是电信300m。

Speed：

单线程，爬取800页，处理表格，不截图，用时 130s

单线程，爬取800页，处理表格，全截图，用时 280s

四线程，爬取800页，处理表格，不截图，用时 40s

四线程，爬取800页，处理表格，全截图，用时 108s

八线程，爬取800页，处理表格，不截图，用时 36s

八线程，爬取800页，处理表格，全截图，用时 57s

----

## 其他正在开发功能

1.浏览器输入网址，自动提取url，cookie，referer等。

2.爬取的日志，以及html文件的哈希值。

3.post请求网站的爬取。

4.动态加载网站的爬取和保存。

5.多个参数变化的网站爬取。

6.服务器端，分布式爬取。

7.页数选择，从中间的页数开始提取。

8.代理，加入ip代理池。

9.文件锁，爬取网站时，打开csv文件用只读，不会使爬虫停止。

10.UI太丑了，研究一下qt5重新做一下。

11.异步请求会不会好一点？

----

## 截图
* 截图需要挂代理才能看到

![Image text](https://raw.githubusercontent.com/zmzmon/CJ/main/%E8%BD%AF%E4%BB%B6%E6%88%AA%E5%9B%BE/1.png)
---
![Image text](https://raw.githubusercontent.com/zmzmon/CJ/main/%E8%BD%AF%E4%BB%B6%E6%88%AA%E5%9B%BE/2.png)
---
