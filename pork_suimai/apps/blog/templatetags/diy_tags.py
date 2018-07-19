# pork_suimai/apps/blog/templaatetags/diy_tags
from django import template     # 从Django中导入模板方法
from ..models import BlogTag, BlogType, Blog, FriendLink
from django.db.models.aggregates import Count   # 从django的数据库模型总数中导入计数方法
register = template.Library()   # 注册   模板的库   Library 图书馆，可以理解为放书进去，

@register.simple_tag
def test(): # 测试
    return 'hello world'

@register.simple_tag    # 注册简单标签，这是python关于装饰器的方法
def get_blog_list():# 获取所有博客列表
    return Blog.objects.all()


@register.simple_tag # 这句代码，是注册这个模板标签到服务器中
def get_blog_type_list():# 获取博客类型列表
    '''下面代码的意思是获取到博客类型所有对象，然后检查,如果该对象所对应的文章数为0则不返回该对象，下面的标签同理'''
    return BlogType.objects.annotate(total_num=Count('blog')).filter(total_num__gt=0)
    # 返回   博客类型   对象   注释            计算blog的数量      过滤数量为0的博客类型

@register.simple_tag
def get_blog_tag_list(): # 获取博客标签列表
    return BlogTag.objects.annotate(total_num=Count('blog')).filter(total_num__gt=0)

@register.simple_tag
def get_friend_link(): # 获取友情链接列表
    return FriendLink.objects.all()

@register.simple_tag
def get_detail_tags(each):
    tags = Blog.blog_tag
    return tags