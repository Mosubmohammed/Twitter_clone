from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
class ProfileInline(admin.StackedInline):
    model=Profile

class UserAdmin(admin.ModelAdmin):
    model=User
    fields=["username"]
    inlines=[ProfileInline]

admin.site.unregister(User)
admin.site.register(User , UserAdmin)
# admin.site.register(Profile)

#max profile info to User info

    