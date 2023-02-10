from django.contrib import admin
from .models import Student,Batch
# Register your models here.
class StudAdmin(admin.ModelAdmin):
    list_display=('date','sub','prn','batch','present')
    search_fields=('prn','batch','sub')
    list_filter=('batch','sub')
class BatchAdmin(admin.ModelAdmin):
    list_display=('batch','prn')
    search_fields=('prn','batch')
    list_filter=('batch',)
admin.site.register(Student,StudAdmin)
admin.site.register(Batch,BatchAdmin)