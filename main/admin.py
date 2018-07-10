from django.contrib import admin
from .models import *

class UserProfileList(admin.ModelAdmin):
    list_display = ('user',)
    ordering = ['user']
admin.site.register(UserProfile, UserProfileList)
# Register your models here.
