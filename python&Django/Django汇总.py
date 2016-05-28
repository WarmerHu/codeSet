#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''
from django.contrib.auth.hashers import make_password
1.cookie================================================================
1.HttpResponse.delete_cookie(key, path='/', domain=None)
    Deletes the cookie with the given key. Fails silently if the key doesn’t exist.
    Due to the way cookies work, path and domain should be the same values you used in set_cookie() – otherwise the cookie may not be deleted.
response = HttpResponse("/")
response.delete_cookie("username", "/")

2.读取cookie
req.COOKIES["userid"]
判断是否存在字段：req.COOKIES.has_key('userid')

3. HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', domain=None, secure=None, httponly=False)
    Sets a cookie. The parameters are the same as in the Morsel cookie object in the Python standard library.
    max_age should be a number of seconds, or None (default) if the cookie should last only as long as the client’s browser session. If expires is not specified, it will be calculated.
    expires should either be a string in the format "Wdy, DD-Mon-YY HH:MM:SS GMT" or a datetime.datetime object in UTC. If expires is a datetime object, the max_age will be calculated.
    Use domain if you want to set a cross-domain cookie. For example, domain=".lawrence.com" will set a cookie that is readable by the domains www.lawrence.com, blogs.lawrence.com and calendars.lawrence.com. Otherwise, a cookie will only be readable by the domain that set it.
    Use httponly=True if you want to prevent client-side JavaScript from having access to the cookie.
    path     "/"   cookie生效的路径前缀，浏览器只会把cookie回传给带有该路径的页面，这样你可以避免将cookie传给站点中的其他的应用。当你的应用不处于站点顶层的时候，这个参数会非常有用。
    secure   False 如果设置为 True ，浏览器将通过HTTPS来回传cookie。

HttpResponse.set_signed_cookie(key, value, salt='', max_age=None, expires=None, path='/', domain=None, secure=None, httponly=True)
    Like set_cookie(), but cryptographic signing the cookie before setting it. Use in conjunction with HttpRequest.get_signed_cookie(). You can use the optional salt argument for added key strength, but you will need to remember to pass it to the corresponding HttpRequest.get_signed_cookie() call.

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

3.url传递参数=========================================================================
(r'^plist/p1(\w+)p2(.+)/$', helloParams）
def helloParams(request，param1,param2):
return HttpResponse("p1 = " + param1 + "; p2 = " + param2)

通过传统的”?”传递参数
例如，http://127.0.0.1:8000/plist/?p1=china&p2=2012，url中‘?’之后表示传递的参数，这里传递了p1和p2两个参数。
(r'^plist/$', helloParams1）
def helloParams(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
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

7.发送邮件================================================================================================================================
setting设置---------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '' //the host for an email server
EMAIL_PORT = 25
EMAIL_HOST_USER = 'xxx@xx.xx'
EMAIL_HOST_PASSWORD = 'xxx'
EMAIL_SUBJECT_PREFIX = 'xx'
view----------------------------------------------------------------------------------------------------------------------------------
send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None)
发邮件的最便捷方式就是使用 django.core.mail.send_mail() 。
subject, message, from_email and recipient_list 这四个参数是必须的。
    subject: 字符串，表示邮件标题。
    message: 字符串，表示邮件内容。
    from_email: 字符串，表示发件邮箱。
    recipient_list: 字符串列表，列表中每个成员都是一个邮箱地址，而且每个收件人都会在 “收件人/To:” 栏看到出现在 recipient_list 中的其他收件人。
    fail_silently: （可选）布尔值。为 False 时， send_mail 会抛出 smtplib.SMTPException 异常。 smtplib 文档列出了所有可能的异常。 这些异常都是 SMTPException 的子类。
    auth_user: （可选）SMTP服务器的认证用户名。没提供该参数的情况下，Django会使用 EMAIL_HOST_USER 配置项的设置。
    auth_password: （可选）SMTP服务器的认证密码，没提供该参数的情况下，Django会使用 EMAIL_HOST_PASSWORD 配置项的设置。
    connection: （可选）发送邮件的后端。没提供该参数的情况下，Django会使用默认后端的实例。可查看 Email backends 了解更多细节。
例子：
from django.core.mail import send_mail
send_mail(u'邮件标题', u'邮件内容', 'from@example.com', ['to@example.com'], fail_silently=False)

send_mass_mail(datatuple, fail_silently=False, auth_user=None, auth_password=None, connection=None)
django.core.mail.send_mass_mail() 适合处理群发邮件。
datatuple 是一个元组，其中每个元素格式如下:(subject, message, from_email, recipient_list)
fail_silently, auth_user 和 auth_password 与上面 send_mail() 中提到的一样。
datatuple 中每个元素都对应一封单独的邮件。与上面 send_mail() 一样，出现在 recipient_list 中的收件人同样会在 “收件人/To:” 字段中看到该邮件的其他所有收件人。

举个例子，下面的代码会给双组不同的收件人发送两封不同的邮件；但仅仅打开一次邮件服务器的链接:
message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
send_mass_mail((message1, message2), fail_silently=False)
=======================================================================================================================================

8.Django自带加密模块的使用=====================================================================================================================
make_password(password, salt=None, hasher='default')
    Currently supported algorithms are: 
        'pbkdf2_sha256', 'pbkdf2_sha1', 'bcrypt_sha256' (see Using bcrypt with Django), 
        'bcrypt', 'sha1', 'md5', 'unsalted_md5' (only for backward compatibility) and 'crypt' if you have the crypt library installed.
生成密码：
>>> make_password("qttc", None, 'pbkdf2_sha256')
u'pbkdf2_sha256$12000$H6HRZD4DDiKg$RXBGBTiFWADyw+J9O7114vxKvysBVP+lz7oSYxkoic0=' 
如果你不想每次都生成不同的密文，可以把make_password的第二个函数给一个固定的字符串，比如：
>>> make_password(text, "a", 'pbkdf2_sha256')

make_password每次生成的密文均不一致，需要使用专用的方法check_password验证
check_password(password, encoded)
>>> text = "qttc"
>>> passwd = make_password(text, None, 'pbkdf2_sha256')
>>> print passwd
pbkdf2_sha256$12000$xzMLhCNvQbb8$i1XDnJIpb/cRRGRX2x7Ym74RNfPRCUp5pbU6Sn+V3J0=
>>> print check_password(text, passwd)
True

is_password_usable(encoded_password)
    Checks if the given string is a hashed password that has a chance of being verified against check_password().
=========================================================================================================================================
