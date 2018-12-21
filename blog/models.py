from django.db import models
from django.contrib.auth.models import User

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)  # 博客类型

    def __str__(self):  # 显示字段内容
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50)  # 博客标题
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)  # 关联到Blogtype
    content = models.TextField()  # 博客内容
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 作者 设为外键
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    last_updated_time = models.DateTimeField(auto_now_add=True)  # 最后修改时间

    def __str__(self):
        return "<blod. %s>" % self.title

    class Meta:
        ordering = ['-created_time']





