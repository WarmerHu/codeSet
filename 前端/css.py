#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''

1. 动态设置css：#应该在所有class="p_author",class="p_content"的元素创建完毕后才调用函数getHeight====================================
'''
height()返回不带单位内容高度，不管border、padding、margin；    .css('height')返回带单位的高度；    
innerHeight()返回不带单位的内容高度+上下padding
outerHeight()返回不带单位的内容高度+上下padding+上下border；outerHeight(tru)返回不带单位的内容高度+上下padding+上下border+上下margin
'''
function getHeight(){
    authorh = $(".p_author").outerHeight(true)+30;
    contenth = $(".p_content").outerHeight(true);
    if(authorh>contenth){
        $(".p_postlist").css("height",authorh);//设置class=“p_postlist”的元素的内容高度为authorh
    }else{
        $(".p_postlist").css("height",contenth);
    }
}
=================================================================================================================

2. html编写css：=============
<style type="text/css">
    pre{
        background:none;
        border:none;
        margin: 0;
        padding: 5px;
    }
</style>
===========================

3. margin=================
例子 1
margin:10px 5px 15px 20px;
上外边距是 10px
右外边距是 5px
下外边距是 15px
左外边距是 20px
例子 2
margin:10px 5px 15px;
上外边距是 10px
右外边距和左外边距是 5px
下外边距是 15px
例子 3
margin:10px 5px;
上外边距和下外边距是 10px
右外边距和左外边距是 5px
例子 4
margin:10px;
所有 4 个外边距都是 10px
==================================

4. border=======================================================================
border:5px solid red;
可以按顺序设置如下属性:
border-width     规定边框的宽度。
border-style (dotted solid double dashed none hidden groove ridge inset outset inherit)
border-color     规定边框的颜色。

e.g.
border-style:dotted solid double dashed;(top,right,bottom,left)
border-color:red green blue;(top,right&left,bottom) 
set one of the borders: 
p  {
  border-style:solid;
  border-bottom-style:dotted;
  }
===============================================================================

5. content exceed table's width==
 table{
  table-layout:fixed;
   overflow:hidden;
  }
============================

6. width========
th{
   min-width:61px;
  }
================

7. 对齐===================================
  .td-t{
    text-align:center;
}
align——表示左右居中——left，center，right
valign——控制上下居中——left，center，right
右对齐：css——float: right;
===========================================