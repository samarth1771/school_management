from django.contrib import admin
from .models import *


# Register your models here.

class StudentInline(admin.StackedInline):
    model = Student


class TeacherInline(admin.TabularInline):
    model = Teacher


class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'city', 'bday']
    search_fields = ['roll_no', 'name']
    list_filter = ['gender']


class SchoolAdmin(admin.ModelAdmin):
    inlines = [StudentInline, TeacherInline]
    list_display = ['name', 'city']
    search_fields = ['name']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_id', 'name', 'city']
    search_fields = ['name']


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
