#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''
1 获取变量长度：len(content)

2 编码，解码=============================================
encode：username.encode('utf-8')//将unicode编码成utf-8
decode：username.decode('utf-8')//将utf-8解码成unicode
======================================================

3 time=====================================================================
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time.time() 获取当前时间戳
time.localtime() 当前时间的struct_time形式
time.ctime() 当前时间的字符串形式
时间相加减-----------------------------------------------------------
last_month = time.localtime()[1]-1 or 12
》》》time.localtime()
》》》time.struct_time(tm_year=2016, tm_mon=2, tm_mday=1, tm_hour=14, tm_min=31, tm_sec=40, tm_wday=0, tm_yday=32, tm_isdst=0)
===========================================================================

4 字符串======================================================
拼接：
1   "\t".join(i,j)  将i，j拼接为 i\tj
2   settings.STATIC_URL+'img/'+self.bbs.userid.head
============================================================

5 class======================================================
dao = activityDao()
dao.add_a_activity(realcontent)
class activityDao():
    def __init__(self,req):
        self.us = User.objects.get(id=req["userid"])
    def add_a_activity(self,realcontent):
        do sth。。。
=============================================================

6 获取当前电脑信息================================================
myname = socket.getfqdn(socket.gethostname(  ))#获取本机电脑名
myaddr = socket.gethostbyname(myname)#获取本机ip
=============================================================

7.字典==============================
读取-------------
判断是否有键值：req.has_key('now')
===================================
