from django.contrib import admin
from .models import Student
# Register your models here.
class StudAdmin(admin.ModelAdmin):
    list_display=('date','prn','batch','present')
    search_fields=('prn','batch')
    list_filter=('batch',)
admin.site.register(Student,StudAdmin)