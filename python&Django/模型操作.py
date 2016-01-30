#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''
查询=======================================================================================
1.order by
#查询Activity所有数据，按字段id倒序排序，显示第1~req个数据
# order_by(), + 正序， -倒叙
# 分片 [i:j] 显示第i~j个数据
    dao = Activity.objects.order_by("-id")[:req]

2.get
User.objects.get(id=req["userid"])
返回("id":1231,"test":"xfga")

get_object_or_404(Collection,id=p1)#返回Collection object or 404

3.filter
//topicid = models.ForeignKey('Topic', db_column='topicId')， class Topic(models.Model)
//self.bbs = Topic.objects.get(id=2131)
Opinion.objects.filter(userid=self.us,topicid=self.bbs,time__startswith=realtime)
返回[("id":1231,"test":"xfga"),(),...]

P.S.多种函数可以组合用，Topic.objects.filter(userid=self.us).order_by("-time")[:1]
==========================================================================================

插入：============================================
//userid是外键
Activity(userid=self.us,time=realtime).save()
================================================

更新：============================================
1.
self.bbs = Topic.objects.get(id=req["id"])
self.bbs.replytime += 1
self.bbs.save()
================================================

删除：============================================
col = get_object_or_404(Collection,id=p1)
col.delete()
================================================