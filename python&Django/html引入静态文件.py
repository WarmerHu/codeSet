#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''
1.setting设置，创建相应文档：
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'subject/static')

2.运行python manage.py collectstatic
# 这个命令应该是把STATICFILES_DIRS指定下的文件都复制到了STATIC_ROOT指定的文件夹下

3.在urls.py中添加：
url(r'^static/(?P<path>.*)$','django.views.static.serve',),  

4.在views.py中需要改成：
return render_to_response("test.html",RequestContext(request))
   
5.在html中引用：
<link href="{{STATIC_URL}}css/a_bbs.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="{{STATIC_URL}}jquery/index.js"></script>
