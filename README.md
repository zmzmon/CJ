# CJ
阿乐数据采集器

* 阿乐数据采集器V1.0 .exe
[**高速下载**](https://pan.forensix.cn/f/bd1d926cd54b4ec0a493/?dl=1)

## 使用方法

1.使用浏览器登陆后台页面，找到需要取的页面，如果是有框架的网站，右键框架仅显示此框架，或者F12找到真实的地址。进入F12审查，点击网络，从中查找cookie，useragent。

2.url中填入地址，去掉变动的参数，我测试的是 http://192.168.0.1/adm.php?m=carmodel&a=list&page=1 ， 则填入url为 http://192.168.0.1/adm.php?m=carmodel&a=list 。

3.cookie中填入cookie，例如SESSIONID=e1dc5fbd-5090-46f4-8e95-6b36884c8de0.QhpGbjQ1mMK__ILRyyy6pi9IBCk; PHPSESSID=ta6e8vr3k3ia81997fipo25ra5; order=1。

4.referer填写来源的网址，例如 http://192.168.0.1/adm.php?m=carmodel&a=list 。

5.useragent中填浏览器的标识，例如Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0 。
 
6.variate中填写变量，比如url中第一页page=1，第二页page=2，这里填写page。

7.page填写页数，例如100。可以参照截图中的填写方式，后面的版本填写时会进行提示。

## 截图
![Image text](https://pan.forensix.cn/thumbnail/051a225f-2e62-45b4-b187-c478644ab108/1024/1.png)
