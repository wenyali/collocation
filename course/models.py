# coding=utf-8
from django.conf import settings
from django.db import models

class AppCategory(models.Model):
    name = models.CharField("项目类别", max_length=200, unique=True)
    intro = models.CharField("项目介绍", max_length=500, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'course_category'
        verbose_name = '项目类别'
        verbose_name_plural = '项目介绍'

    def __str__(self):
        return self.name

PUBLIC_TYPE_CHOICES = (
    (0, "内测版"),
    (1, "公测版"),
)


class App(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             on_delete=models.SET_NULL)
    category = models.ForeignKey(AppCategory, null=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField("项目名称", max_length=200)
    logo_image = models.ImageField("项目logo", upload_to="course/logo_image", blank=True)
    file = models.FileField("文件路径",upload_to="course/file",blank=True)
    public_type = models.SmallIntegerField("项目类型", default=0,
                                           choices=PUBLIC_TYPE_CHOICES)
    intro = models.CharField("项目介绍", max_length=1000)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'app'
        verbose_name = 'App应用'
        verbose_name_plural = 'App应用'

    def __str__(self):
        return self.title


class AppComment(models.Model):
    app_comment = models.ForeignKey(AppCategory, null=True,
                                       on_delete=models.SET_NULL)
    comment = models.CharField("评论内容", max_length=500, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             on_delete=models.SET_NULL)
    parent = models.ForeignKey("self", null=True, blank=True,
                               on_delete=models.SET_NULL)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'course_comment'
        verbose_name = '项目评论'
        verbose_name_plural = '项目评论'
    
    def __str__(self):
        return self.comment
