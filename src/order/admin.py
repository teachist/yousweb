from django.contrib import admin
from .models import Order
from review.models import Review
# Register your models here.


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['user', 'customer', 'contact_phone', 'product', 'description', 'status']}),
        ('Date information', {'fields': ['create_time'], 'classes': ['collapse']}),
        # ('Extra information', {'fields': ['comment']}),
    ]

    inlines = [ReviewInline]
    list_display = (
        'customer',
        'contact_phone_format',
        # 'front_review',
        # 'designer_review',
        # 'installer_review',
        'status',
        'create_time',
        'finish_time_check'
    )
    list_filter = ['create_time', ]
    search_fields = ['contact_phone']


admin.site.register(Order, OrderAdmin)
