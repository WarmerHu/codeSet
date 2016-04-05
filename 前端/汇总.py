#coding:utf-8
'''
Created on 2016年1月28日
@author: Warmer
'''
19.正则========================================================================
匹配邮箱：
var reg =/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
reg.test(use) ——》true、False
=============================================================================

18.弹窗
alert("请求错误");

17.md5=============
1.导入jquery.md5.js
2.加密：$.md5(usps)
===================

16.获取值：=======================================
$("#detail").val()//获取id="detail"的元素的value
$(this).attr("id");//this表示当前元素，常用与点击事件
$("input[name='col-id-"+n+"']").attr("value")
获取变量长度： detail.length
获取元素的高、宽等参考css
    text() - 设置或返回所选元素的文本内容
    html() - 设置或返回所选元素的内容（包括 HTML 标记）
    val() - 设置或返回表单字段的值
================================================

15.元素赋值：============================================================================
$(".title-imgs").attr("src",data.head);#class="title-imgs"的元素的src属性为data.head
$("#islog").attr("href","/account/logout");
$("input[name='col-id']").val(data.id);
$("#tips").html("data.tips");# id="tips"的元素赋值为"data.tips"
$("h1[name='title-topic']").html(data.topic);#<h1 name='title-topic']>
=================================================================================

14.删除元素：
$("tr[name='tr-" + n + "']").remove();

13.去除前后空格： $.trim($("#detail").val());

12.判断对象是否为空：================================================================================
$.isEmptyObject({}) // true
$.isEmptyObject({ foo: "bar" }) // false
==========================================================================================

11.判断是否有该键值================
if(data.tips)
“tips”in data
===========================

10.刷新当前页面：window.location.reload();

9.跳转页面：  location.href = "/account/go_login";    #http://ip:host/account/go_login

8.console调试：
打印：console.log("获取动态失败");

7.全局变量的声明=================================================================================
var dataAsw = "";
window.dataAsw = data.answer

dataAsw = "";
dataAsw = data.answer
===========================================================================================

6.遍历：
$.each(data.opinions,function(n,v){ //遍历data.opinions的元素，n是第几遍，v是实际内容}

5.绑定点击事件：=================================================================================
$(function(){
      $("#toTitle").click(function(){
                                     do sth...
      })
})
当需要绑定的元素是动态创建时：
$(function toTopic(){
    $("body").on('click',"tr[class='toTopic']",function(){
        $.cookie("bbsid",$(this).attr("id"));
        location.href = "/bbs/topic";
    });
})
==========================================================================================

4.元素的显示与隐藏==============================================
显示：$("#tips").html(result.tips).show();
隐藏：$('#tips').hide();
切换元素的可见状态：
    $("#PWch").hide();
    $("#sub-val").click(function(){
            $("#PWch").toggle();
    })
===========================================================

    

3.cookie====================================================================================
1.引入jquery.cookie.js
2.代码：
Create session cookie:
$.cookie('name', 'value');
Create expiring cookie, 7 days from then:
$.cookie('name', 'value', { expires:7 });
Create expiring cookie, valid across entire site:
$.cookie('name', 'value', { expires:7, path:'/' });
Read cookie:
$.cookie('name'); // => "value"     $.cookie('nothing'); // => undefined
Read all available cookies:
$.cookie(); // => { "name": "value" }
Delete cookie:
// Returns true when cookie was successfully deleted, otherwise false   
$.removeCookie('name'); // => true  $.removeCookie('nothing'); // => false
// Need to use the same attributes (path, domain) as what the cookie was written with   $.cookie('name', 'value', { path:'/' });
// This won't work!    $.removeCookie('name'); // => false    
// This will work!  $.removeCookie('name', { path:'/' }); // => true
==========================================================================================

2.滚动页面时DIV到达顶部时固定在顶部滚动页面时DIV到达顶部时固定在顶部==============================================================================================
html:------------------------------------------------------------------------------------------
<div id="nav"></div>
js:--------------------------------------------------------------------------------------------
function menuFixed(id){
    var obj = document.getElementById(id);
    var _getHeight = obj.offsetTop; //offsetTop:获取对象相对于版面或由 offsetTop 属性指定的父坐标的计算顶端位置
    
    window.onscroll = function(){ //onscroll:滚动div时的事件
        changePos(id,_getHeight);
    }
}
function changePos(id,height){
    var obj = document.getElementById(id);
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;    //获取滚动条的滚动距离
    if(scrollTop < height){
        obj.style.position = 'relative';
        obj.style.top = '0px';
    }else{
        obj.style.position = 'fixed';
        obj.style.top = '50px';
    }
}

window.onload = function(){
    menuFixed('nav');
}
================================================================================================


1.函数调用========================================================================================
html引入test.js，自动加载function a,function b的代码；
执行function b，不执行funtion a
function b,function c成功引用function a
test.js :————————————————————————————————————————————————————————
function a(){             }
$(function b(){               a();               c(data);               
               }
  )
function c(data){             a();             }
————————————————————————————————————————————————————————
===================================================================================================

20.获取url=================================
http://127.0.0.1:8000/?hello
var r = window.location.search; // ?hello
==========================================

21.截取字符串============================================
r = r.substring(r.indexOf("?"),r.length-1);
======================================================

22. 导航栏下拉栏=======================================================================================================================
<nav class="navbar navbar-inverse navbar-fixed-top">
    <ul class="nav navbar-nav">
        <li>
                <a class="dropdown-toggle" aria-expanded="true" aria-haspopup="true" role="button" href="#" data-toggle="dropdown">
                                                             刷题宝典
                    <span class="caret"></span>
                </a>
                <ul class="dropdown-menu">
                    <li>
                        <a href="/title">开始刷题</a>
                    </li>
                    <li>
                        <a href="/title/publish/add">发布题目</a>
                    </li>
                </ul>
            </li>
    </ul>
</nav>
====================================================================================================================================

23. 对齐=====================
右对齐：css——float: right;
============================

24. 按钮不可点击，输入框不可操作================================
<ul class="nav nav-pills" role="tablist">
        <li class="active" role="presentation">
            <a data-toggle="tab" role="tab" aria-controls="home" href="#intro" onclick="firt()">逐一手动输入题目</a>
        </li>
        <li role="presentation">
            <a data-toggle="tab" role="tab" aria-controls="profile" href="#coin" onclick="sect()">通过execl发布题目</a>
        </li>
    </ul>
<textarea id='qu' name="question" type="text" class="form-control"></textarea>
<input name="answer" type="text" class="form-control" />
<button class="btn btn-primary btn-lg btn-block" id="add-val"  >继续添加下一题</button>

function firt(){
    $(".form-control").removeAttr("readonly");
    $("#add-val").removeAttr("disabled");
}
function sect(){
    $(".form-control").attr("readonly","true");
    $("#add-val").attr("disabled","true");
}
=======================================================