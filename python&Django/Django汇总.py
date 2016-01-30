#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''
1.cookie================================================================
1.删除cookies
response = HttpResponseRedirect("/")
response.delete_cookie("username", "/")

2.读取cookie
req.COOKIES["userid"]
判断是否存在字段：req.COOKIES.has_key('userid')
========================================================================

2.获取POST数据===========================================================================================================
字符串，数字：
request.POST[strName]
判断是否存在这个key：request.POST.has_key(strName)

获取[]类型的数据：例如，每行数据前面都带个checkbox的操作。这时候可能会选多个checkbox,传入到后台时，如果用request.POST[strname]获取，那么只能获取到一个值
request.POST.getlist(strName)

获取json数据：————————————————————————————————————————————
jsonReq = simplejson.loads(req.body)
title = jsonReq['title']
id = jsonReq['id']
json：-------------------------------------------------
data:JSON.stringify({
    "id":$("input[name='col-id']").val(),
    "title":{
        "id":$("input[name='col-title-id']").val(),
        "answer":$("#sub-ans").val().trim()
    },
})
——————————————————————————————————————————————————————

form：
if req.method == 'POST':
    modifyform = modifyForm(req.POST)
    if modifyform.is_valid():
        delete = modifyform.cleaned_data['delete']
======================================================================================================================

3.获取get数据：url传递参数=========================================================================
(r'^plist/p1(\w+)p2(.+)/$', helloParams）
def helloParams(request，param1,param2):
return HttpResponse("p1 = " + param1 + "; p2 = " + param2)

通过传统的”?”传递参数
例如，http://127.0.0.1:8000/plist/?p1=china&p2=2012，url中‘?’之后表示传递的参数，这里传递了p1和p2两个参数。
(r'^plist/$', helloParams1）
def helloParams(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    return HttpResponse("p1 = " + p1 + "; p2 = " + p2)
============================================================================================

4.时区============================================================================================================
timezone.localtime(v.time).strftime('%Y-%m-%d %H:%M:%S')    //将v.time转换为当前时区的时间并按strftime的格式显示
=================================================================================================================

5.上传文件==================================================================================================
配置MEDIA
setting---------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/').replace("\\","/")
url-----------------------------------------------------------------------------------------------
url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
后台处理-------------------------------------------------------------------------------------------
@csrf_exempt
def upload_resources(req):
    if req.COOKIES.has_key('userid'):
        file = req.FILES['uploadedfile']  # @ReservedAssignment
        points = req.POST['points']
        filename = req.POST['filename'].decode('utf-8').encode('utf-8')
        if file:
            userid = req.COOKIES['userid'].decode('utf-8').encode('utf-8')
            uploadFile({'userid':userid,'file':file,'filename':filename,'points':points})
    return HttpResponse(json.dumps({'tips':'上传失败'}),content_type="application/json")
def uploadFile(req):
    f_path = settings.MEDIA_ROOT + req['filename']
    with open(f_path,'wb+') as info:
        for chunk in req['file'].chunks():
            info.write(chunk)
前端-----------------------------------------------------------------------------------------------
<form id= "uploadForm"  enctype="multipart/form-data"> 
    <input id="uploadedfile" name="uploadedfile" type="file" />
    <input type="button" value="上传" onclick="doUpload()" /> 
        下载时所需积分：<input id="points" name="points" value=0 />
        <input type="hidden" name="filename" id="filename" />
    </form>
function doUpload(){
        var file = $("#uploadedfile").val();
        var strFileName=file.split("/").pop();
        $("#filename").val(strFileName);
        var formData = new FormData($( "#uploadForm" )[0]);  
         $.ajax({  
              url: '/resources/upload/' ,  
              type: 'POST',  
              data: formData,  
              async: false,  
              cache: false,  
              contentType: false,  
              processData: false,  
              success: function (data) {                },  
              error: function (data) {                }  
         }); 
    }
==========================================================================================================

6.下载文件==================================================================================
1）直接访问配置好的url即可下载
=========================================================================================
