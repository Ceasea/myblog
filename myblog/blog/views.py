# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    articles = models.Article.objects.all
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article':article})

"""
def edit_action(request):
    
    http请求将页面内容一起传递到后台,此时取出页面中的title,content,id
    如果是重新编辑，则将得到的title,content赋给edit_page的
    input表单中title,content,并返回edit_page；
    如果是新建文章，则直接返回edit_page
    
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        
        如果id为0, 说明是新建文章，此时创建所有文章对象
        并返回到首页, 根据id为0，跳转到创建新文章页面
        
        
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all
        return render(request, 'blog/index.html', {'articles': articles})
    
    
    如果id不为0, 即重新编辑, 则通过id获得文章对象, 将get到的文章title
    与content赋给article对象并传递到前端，前端经表单修改后
    的内容(表格过程不是很明白，有待学习)
    
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})
    
    index.html    
    <!--
    <a href="{% url 'blog:edit_page'  %}">新文章</a>
    -->
    
    article_page.html
    <!--a href="{% url 'blog:edit_page' article.id %}">修改文章</a-->
"""
