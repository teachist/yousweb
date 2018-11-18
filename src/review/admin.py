from django.contrib import admin
from .models import Review

# # Register your models here.


# class StuffAdmin(admin.ModelAdmin):
#     list_display = ('position',)
#     list_filter = ['position']
#     search_fields = ['name']


admin.site.register(Review)
