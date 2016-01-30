#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''
$(function initial(){
    $.ajax({
        type:"GET",
        url:"/bbs/topic/list/"+bbsid,
        dataType:"json",
        success:function(data){
            if(!$.isEmptyObject(data)){
                $.each(data.opinions,function(n,v){ //遍历data.opinions的元素，n是第几遍，v是实际内容
                    var parentdiv = $("<div class='p_postlist'></div>");
                    var contentdiv = $("<div class='p_content'>" +
                            "<pre>"+v.content+"</pre></div>");
                    contentdiv.appendTo(parentdiv);
                    
                    parentdiv.appendTo($("#opi-all"));
                });
            }
    },
    error:function(){}
    });
})   
————————————————————————————
data{
     "id":11244,
     "opinions":[
                 {
                    "content":"dsfsd"
                  },
                 {
                    "content":"fgaad"
                  },
                 ...
    ]
}