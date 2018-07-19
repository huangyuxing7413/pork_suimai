from django.db import models

import markdown
from django.contrib.auth.models import User
'''
models.py的作用是，定义数据库的表名和键名、键名的属性（类型）、键名参数
表名就是像下面的BlogType、BlogTag、Blog、FriendLink
键名就像是title、body、name、slug、author……之类的
键名的属性（字段类型）CharField、SlugField、TextField等等，还有一个叫ForeignKey和ManyToManyField
                的是外键关联和多对多关联。
                其实这里的字段类型都是见名知意的英语单词，就slug的话有点难理解
                slug翻译是“块”、”金属块”，还有一种翻译是术语，关于报纸的术语，可以理解为“短新闻”
                这里我们把它用作路由地址的索引，它只能用字母和数字还有符号来表示，其他像中文的是无法正常写入的

键名参数的话：里面的内容到都是见名知意的，详情看一下官方文档就好了。

关于函数部分，这些都是对表单的内容的键名进行处理，例如说Blog中的body，也就是我们的文章内容
            我们在后台写入后，内容仍然是我们的markdown格式的源代码，会包含### *** 之类的内容
            输出到前端页面，而浏览器是不会处理markdown格式的，需要我们对内容的markdown格式
            转化为html格式的文本内容，才能让前端显示markdown格式的内容。

            
'''




# 类型
class BlogType(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    introduction = models.TextField(verbose_name='简介')
    class Meta:
        verbose_name = "类别"
        verbose_name_plural = '类别列表'
        ordering = ['name']      #排序，按名字排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name

# 标签
class BlogTag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    introduction = models.TextField(verbose_name='简介')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签列表'
        ordering = ['id']       # 排序，按id排序
    # 使对象在后台显示更友善
    def __str__(self):
        return self.name




# 文章详情
class Blog(models.Model):
    title = models.CharField(verbose_name='标题',max_length=50)
    body = models.TextField(verbose_name='文章内容')
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    slug = models.SlugField(unique=True)
    blog_type = models.ForeignKey(BlogType, verbose_name='类型', on_delete=models.CASCADE)
    blog_tag = models.ManyToManyField(BlogTag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 使对象在后台显示更友善
    def __str__(self):
        return "<Blog:%s>" % self.title

    def body_markdown(self):
        mark = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        self.body = mark.convert(self.body)
        self.toc = mark.toc
        return self.body

    # 分页
    def get_pre(self):# 上一页
        return Blog.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):#下一页
        return Blog.objects.filter(id__gt=self.id).order_by('id').first()




class FriendLink(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField('友链地址', help_text='请填写http或https开头的完整形式地址')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name
