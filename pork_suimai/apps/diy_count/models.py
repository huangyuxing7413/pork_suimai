# pork_suimai/apps/diy_count/models.py
from django.db import models

# Create your models here.
class ReadNum(models.Model):
    '''slug是记录文章的后缀名，获取阅读数时的索引的名称'''
    slug_name = models.CharField(verbose_name='后缀名', max_length=60)
    '''这里的IntegerField是整数字段，默认为零'''
    read_detail_num = models.IntegerField(verbose_name='文章阅读数', default=0)