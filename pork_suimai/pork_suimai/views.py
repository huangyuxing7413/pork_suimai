# pork_suimai/pork_suimai/views.py

# 从django的快捷方式（快捷键）导入 呈现方法、要么获取对象成功，要么404的方法
from django.shortcuts import render, get_object_or_404



# 首页
def home(request):  # 定义一个名为home的函数
    # 返回  呈现（渲染），请求，home.html文件
    # 这里一句话说白，就是：
    # 以home.html作为模板，返回请求
    # 这里留到下一篇博文再讲，下一篇博文会更加详细的讲
    return render(request, 'home.html')
