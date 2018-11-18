from django.contrib import admin
from django.contrib.auth.models import Group
from django.conf import settings
from .models import Profile, Stuff
from django.contrib.auth.admin import UserAdmin
from .models import User


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 0


class MyUserAdmin(UserAdmin):
    inlines = [ProfileInline]

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'openid', 'nickname')
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # search_fields = ('username', 'first_name', 'last_name', 'email')
    # ordering = ('username',)


admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
# admin.site.register(Profile)
admin.site.register(Stuff)
