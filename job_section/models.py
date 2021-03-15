from django.db import models

class Post(models.Model):
    # 标题
    title = models.CharField(max_length=70)
    # 公司
    company = models.CharField(max_length=70)
    # 薪水
    salary = models.CharField(max_length=70)
    # 地址
    address = models.CharField(max_length=70)
    # 详细
    detail = models.TextField()
    # 其他属性
    def __str__(self):
        return self.title