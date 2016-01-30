#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''

新建base.htm
——————————————————————————————————————————————
html代码。。。
  {% block script %}{% endblock %}
  html代码。。。。。
{% block content %}{% endblock %}
html代码
——————————————————————————————————————————————
新建test.html
——————————————————————————————————————————————
{% extends "base.html" %}
{% block script %}
实际代码
{% endblock %}
{% block content %}
实际代码。。。。。。
{% endblock %}
—————————————————————————————————————————————— 


 

