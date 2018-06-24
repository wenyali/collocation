# coding=utf-8
from django.contrib import admin

from course.models import AppCategory, App, AppComment


class AppCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "intro", "ctime")


admin.site.register(AppCategory, AppCategoryAdmin)


class AppAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "ctime")


admin.site.register(App, AppAdmin)



class AppCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "app_comment", "comment", "user", "ctime")


admin.site.register(AppComment, AppCommentAdmin)
