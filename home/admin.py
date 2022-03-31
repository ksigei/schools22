from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'hod', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'hod',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')