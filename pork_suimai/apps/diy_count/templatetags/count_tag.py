# pork_suimai/apps/diy_count/templatetags/count_tag.py
from django import template
from ..models import ReadNum
register = template.Library()

# 文章详情内使用
@register.simple_tag
def get_read_detail(request, obj):
    key = "%s_read" % (obj.slug)
    read_num, created = ReadNum.objects.get_or_create(slug_name=obj.slug)
    if not request.COOKIES.get(key) and request.user != obj.author: # 如果客户端请求中没有key这个cookie
        '''get_or_create是django的内置方法，获取或创建
            这里整个函数的目的是，获取到请求，如果没有key这个cookie，阅读数加一，并返回阅读数
            如果有这个cookice，则直接返回阅读数       
        '''
        read_num.read_detail_num += 1
    read_num.save()
    get_read_num = ReadNum.objects.get(slug_name=obj.slug).read_detail_num
    return get_read_num

# 文章列表和其它地方使用
@register.simple_tag
def read_count_tag(slug):
    list_read_num = ReadNum.objects.get(slug_name=slug).read_detail_num

    return list_read_num