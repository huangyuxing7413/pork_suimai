from django.urls import path,re_path   # 从django的路由方法导入路径方法，和正则表达式路径方法
from . import views #从当前目录导入views.py的内容

urlpatterns = [

    # 定义该应用的路由的根路径为空，调用的视图处理方法为当前目录下的views文件中的blog_list方法，路由名为blog_list
    path('', views.blog_list, name='blog_list'),                  # 所有文章
    # http://127.0.0.1:8000/blog    这是例子，这个是博文所有文章的列表


    # 定义该应用的路由的根路径为type/，调用的视图处理方法为当前目录下的views文件中的blog_type方法，路由名为blog_type
    # 这是正则表达式匹配路径，/(?P<slug>[\w-]+)/
    # 以/开头 以/结束  括号()是括起来的的表达式作为一个分组
    # [\w-]是匹配任意字母数字和减号
    # (?P<slug>[\w-]+)就是把slug进行分组，匹配里面的[\w-]
    re_path('type/(?P<slug>[\w-]+)/', views.blog_type, name='blog_type'),# 类型归档
    # http://127.0.0.1:8000/type/slug


    re_path('tag/(?P<slug>[\w-]+)/', views.blog_tag, name='blog_tag'),    # 标签归档
    # http://127.0.0.1:8000/tag/slug


    re_path('detail/(?P<slug>[\w-]+)/', views.blog_detail, name='detail'),          #文章内容
    # http://127.0.0.1:8000/blog/detail/slug

]
