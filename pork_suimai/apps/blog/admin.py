# pork_suimai/apps/blog/admin.py
from django.contrib import admin
from .models import Blog, BlogTag, BlogType, FriendLink
'''
admin.py的作用是注册应用在后台显示

这里的话，需要先把本篇文章后面的步骤完成后才能看到它的作用，
大概在你生成超级管理员，并登录后台的时候就可以看到这里的内容了
下面的内容可以这样理解，首先要知道他们的意思
admin 管理员
register 注册
list 列表
display 显示
ModelAdmin 管理员模型
@xxx   @是python的装饰器，这个自行查阅python的基础知识

这里我用伪代码来讲吧

@管理员的.注册方法（博客类型）
生成一个名为BlogTypeAdmin继承了admin中的ModelAdmin类方法
    显示列表等于 名字、id、slug、简介

当我们请求了’http://127.0.0.1:8000/admin‘并成功登录后
我们可以看到有BlogType、BlogTag、Blog、FriendLink
        （这里我们在models.py中对它们进行了美化处理，显示的内容是’类别‘、’类别列表之类的’）
        （可以把models.py中的class meta：、 def __str__(self):的内容去掉后就会看到它们原来的面目了）

随便点开一个选项可以看到一个表单，表单的键名就是我们定义的list_display

'''



@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug','introduction')


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug','introduction')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'slug', 'author', 'created_time', 'update_time')


@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
