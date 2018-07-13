from django.contrib import admin
from .models import *

class UserProfileList(admin.ModelAdmin):
    list_display = ('user',)
    ordering = ['user']
admin.site.register(UserProfile, UserProfileList)

class SignUpAttemptList(admin.ModelAdmin):
    list_display = ('id','first_name',)
    ordering = ['id']
admin.site.register(SignUpAttempt, SignUpAttemptList)

class ForumPostList(admin.ModelAdmin):
    list_display = ('id','title',)
    ordering = ['id']
admin.site.register(ForumPost, ForumPostList)
# Register your models here.
