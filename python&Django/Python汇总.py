#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''
获取变量长度：len(content)

编码，解码————————————————————————————————————————————————————————
encode：username.encode('utf-8')//将unicode编码成utf-8
decode：username.decode('utf-8')将utf-8解码成unicode
————————————————————————————————————————————————————————————————

time————————————————————————————————————————————————————————————————————————
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))#获取当前时间
————————————————————————————————————————————————————————————————————————————

字符串——————————————————————————————————————————————————————
拼接：
1   "\t".join(i,j)  将i，j拼接为 i\tj
2   settings.STATIC_URL+'img/'+self.bbs.userid.head
——————————————————————————————————————————————————————————

class————————————————————————————————————————————————————
dao = activityDao()
dao.add_a_activity(realcontent)
class activityDao():
    def __init__(self,req):
        self.us = User.objects.get(id=req["userid"])
    def add_a_activity(self,realcontent):
        do sth。。。
—————————————————————————————————————————————————————————
