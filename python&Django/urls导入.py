#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''

project-》urls
——————————————————————————————————————————————————————————————————————————
urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),    
    url(r'^bbs/', include(bbs.urls)),
    url(r'^$', 'bbs.views.index'),
)
——————————————————————————————————————————————————————————————————————————

app bbs新建文件urls.py
——————————————————————————————————————————————————————————————————————————
urlpatterns = patterns('',
    url(r'^$', 'bbs.views.index'),
    url(r'^list/(.+)/$', 'bbs.views.index'),
)
——————————————————————————————————————————————————————————————————————————

bbs->views创建函数index
def index(req):
    return render_to_response('bbs.html',RequestContext(req))


