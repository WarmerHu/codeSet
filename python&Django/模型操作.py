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

6.count
Job.objects.count() 

7.Q
Q class
from django.db.models import Q
Keyword argument queries – in filter(), etc. – are “AND”ed together. 
If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.
从文档把Q放在Complex lookups with Q objects,下就可以看出，Q是做复杂查询的
and --> XX.objects.filter(Q(f=1),Q(f=2))  # 肯定木有结果 f == 1 and f == 2
or --> XX.objects.filter(Q(f=1) | Q(f=2)) # f ==1 | f == 2
not --> XX.objects.filter(~Q(f=1),Q(f=2))  # f != 1 and f == 2

8.F
F class
from django.db.models import F
Instances of F() act as a reference to a model field within a query. 
These references can then be used in query filters to compare the values of two different fields on the same model instance
例如model 有两列 一列叫做user,一列叫做assigned_user,
需求是取出user=assigned_user的记录
direct_comment = _tasks.filter(user=F('assigned_user'))

9.group_by
def group_by(query_set, group_by):
    '''util:django 获取分类列表'''
    assert isinstance(query_set, QuerySet)
    django_groups = query_set.values(group_by).annotate(Count(group_by))
    groups = []
    for dict_ in django_groups:
        groups.append(dict_.get(group_by))
    return groups
例如:
assign_to = _tasks.exclude(user=F('assigned_user'))
groups = group_by(assign_to, 'group')
取出的是一个列表groups = [1L, 3L, 4L]

P.S.多种函数可以组合用，Topic.objects.filter(userid=self.us).order_by("-time")[:1]
==========================================================================================

插入：============================================
//userid是外键
Activity(userid=self.us,time=realtime).save()
================================================

批量插入：===========================================
def insert_titles(self,req):
        querysetlist=[]
        for i in req:
            querysetlist.append(Exercise(title=req['title'],
                                         answer=req['answer'],
                                         tips=req['tips'],
                                         userid=self.us,
                                         state='ACTIVE'))        
        Exercise.objects.bulk_create(querysetlist)
==================================================

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