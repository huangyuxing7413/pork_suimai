from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ReadNum


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('slug_name', 'read_detail_num')