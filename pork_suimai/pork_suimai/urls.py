# pork_suimai/pork_suimai/urls.py
"""pork_suimai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin    # 从django的核心方法引入管理员方法
from django.conf import settings    # 从django配置中引入设置
from django.conf.urls.static import static  # 从django配置中引入路由的静态方法
from django.urls import path    # 从 django 包中的 路由 引入路径方法
from django.urls import include # 从 django 包中的 路由 引入 导入方法
                                # 其实这里可以写成from django.urls import path,include

from . import views             # 从当前目录引入views.py文件 ，下一章节创建该文件，现在编译器会显示报错信息

# 路由样式
urlpatterns = [
    path('', views.home, name='home'),  # 这是根目录也就是首页
                                        # 使用了当前目录下的views.py中的home函数，
                                        # url名字 是home


    # 路由的路径是blog/   引入了apps目录中的blog目录下的urls.py文件，这个应用还未创建，下一篇文章再创建。
    path('blog/', include('apps.blog.urls')),


    # 路由的路径是admin/  使用了管理员的site 中的urls配置， site这个单词，不知道该翻译成什么好，现场？？工地？？
    path('admin/', admin.site.urls),
]

# 路由样式加入静态方法的图片链接，文件路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
