
from django.contrib import admin

from .models import Course, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'course', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('course',)
