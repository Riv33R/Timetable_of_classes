from django.contrib import admin
from .models import Class, Subject, Schedule

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'subject', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('class_name', 'subject', 'day_of_week')
    search_fields = ('class_name__name', 'subject__name')
