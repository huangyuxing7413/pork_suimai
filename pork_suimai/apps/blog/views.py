# pork_suimai/apps/blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import BlogTag, BlogType, Blog,FriendLink

'''
views.py是django中关视图处理的文件，当然，也可以写成shitu.py
        但是，你需要将urls.py里的的路由方法改成path('', shitu.blog_list, name='blog_list'),

结合urls.py、views.py、model.py,这里讲一下django的运行方式吧
1.首先我们启动了的django的服务器
2.我们在浏览器中输入了“http://127.0.0.1:8000/blog”，这样就有了一个对dango服务器的请求
3.django服务器呢就会从 根目录下的pork_suimai目录中的urls.py文件中寻找该路由的配置
    如果没有匹配到该路径，就会返回404错误（大家可以试试，输入不存在的路径）

    如果找到了，结合这个例子，我们找到了”/blog“，（总路由是包括了在apps的应用的路径的）
    那服务器就会看该路径使用了那个视图方法，”path('', views.blog_list, name='blog_list'),“
    由上面可以知道，”/blog“用了views.py中的blog_list的方法
4.看下面的blog_list函数可以知道
    blog_list接受到请求后，生成了一个名为context的字典
    然后我们给字典定义了一个键名为“blogs”
    它的内容是Blog.objects.all()
    Blog是数据库的表单名，objects是对象，all是所有
    也就是说：context中的blogs这个键包含了数据库Blog表单的所有对象

    最后，return render(request, 'blog_list.html', context)
    以blog_list.html作为模板渲染context的内容，来回应这个请求
'''


# 所有博客列表
def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    
    return render(request, 'blog_list.html', context)


# 按类型分类的博客列表
def blog_type(request, slug):  # 分类页
    context = {}
    blog_type = get_object_or_404(BlogType, slug=slug)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)

    return render(request, 'blog_type.html', context)


# 按标签分类的博客列表
def blog_tag(request, slug):
    context = {}
    blog_tag = get_object_or_404(BlogTag, slug=slug)
    context['blogs'] = Blog.objects.filter(blog_tag=blog_tag)

    return render(request, 'blog_tag.html', context)


# 文章详情页
def blog_detail(request, slug): # 接受request请求，和slug参数

    context = {}                # 生成命名为context的一个空字典
    context['blog'] = get_object_or_404(Blog, slug=slug)

    response = render(request, 'blog_detail.html', context)

    # 发送cookie ，阅读该文章，一天内只算一次，要24小时后阅读量才增+1
    key = "%s_read" % (slug)
    response.set_cookie(key, 'true', max_age=60 * 60 * 24)

    return response


