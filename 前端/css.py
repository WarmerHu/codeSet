#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''

动态设置css：#应该在所有class="p_author",class="p_content"的元素创建完毕后才调用函数getHeight
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

html编写css：
<style type="text/css">
    pre{
        background:none;
        border:none;
        margin: 0;
        padding: 5px;
    }
</style>