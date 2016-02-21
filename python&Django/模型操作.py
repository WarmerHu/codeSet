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

 contains   like
 gt, gte, lt, lte  大于，大于或等于，小于，小于或等于
 in=[1, 3, 4]  返回所有ID为1，3，或4的条目
 startswith  istartswith 区分大小写和忽略大小写的开头匹配
 endswith and iendswith  区分大小写和忽略大小写的末尾匹配
 range  You can use range anywhere you can use BETWEEN in SQL for dates
 year, month, and day  对date/datetime类型严格匹配年、月或日
 isnull  使用``True``或``False``，则分别相当于SQL语句中的``IS NULL``和``IS NOT NULL``

4.distinct(*fields)
mysql中的用法:Category.objects.values('parentcode','email').distinct()

5.执行原生sql
        q = '''select DISTINCT topicID,opinion.id, name,max(opinion.time) as newtime
            from opinion,topic where opinion.userID = 11 and topicId=topic.id
            GROUP BY topicId;'''
        opi = Opinion.objects.raw(q)
        for v in opi:
            value['topicId'] = v.topicID

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