#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''
4. return HttpResponseRedirect('/contact/thanks/')

3.return HttpResponse('hello django')

2.返回普通模板
def into_bbs(req):
    return render_to_response('bbs.html',{"a":"sdf"},RequestContext(req))
————————————————————————————————————————————————————————
bbs.html————————————————————————————————
{{a}}


1.返回ajax
url:————————————————————————————————————————————————————————————————————————————————————
url(r'^topic/(.+)/publish$', 'bbs.views.add_a_opinion'),
————————————————————————————————————————————————————————
views:  get请求不需要@csrf_exempt————————————————————————————————————————————————————————
@csrf_exempt
def add_a_opinion(req,param):
    if req.method == "POST" and req.COOKIES.has_key('userid'):
        jsonReq = simplejson.loads(req.body)
        title = jsonReq['title']
        id = jsonReq['id']
        return HttpResponse(json.dumps({"tips":"登录用户每min只可发布一条意见"}),content_type="application/json")
——————————————————————————————————————————————————————————
jq:——————————————————————————————————————————————————————————————————————————————————————
$(function check() {
          $("#sub-val").click(function() {
                  $.ajax({
                    type: "POST",
                    url: "/collection/answer/check/",
                    dataType: "json",
                    timeout: 1000,
                    data:JSON.stringify({
                        "id":$("input[name='col-id']").val(),
                        "title":{
                            "id":$("input[name='col-title-id']").val(),
                            "answer":$("#sub-ans").val().trim()
                        },
                }),
                    error: function(){                    },
                success: function(data){                    }
        })
    })
})
————————————————————————————————————————————————————————