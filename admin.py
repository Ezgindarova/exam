from django.contrib import admin
from .models import iexam

@admin.register(veexam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'created_at', 'exam_date', 'is_public')
    list_filter = ('is_public', 'created_at')
    search_fields = ('exam_name', 'users__email')
    filter_horizontal = ('users',)
    date_hierarchy = 'exam_date'
    
    fieldsets = (
        (None, {
            'fields': ('exam_name', 'exam_date', 'exam_image', 'is_public')
        }),
        ('Участники', {
            'fields': ('users',)
        }),
    )