from django.contrib import admin
from .models import Student
# Register your models here.
class StudAdmin(admin.ModelAdmin):
    list_display=('date','sub','prn','batch','present')
    search_fields=('prn','batch','sub')
    list_filter=('batch','sub')
admin.site.register(Student,StudAdmin)