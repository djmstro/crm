from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class Status_projectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class Type_callAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class CustumerAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'name', 'last_name', 'get_photo', 'custumer_phone', 'custumer_email', 'type_call')
    list_display_links = ('id', 'name', 'last_name', 'get_photo')
    search_fields = ['name', 'last_name', 'custumer_phone', 'custumer_email']
    readonly_fields = ('created_at', 'get_photo')

    def get_photo(self, obj):
        if obj.custumer_photo:
            return mark_safe(f'<img src="{obj.custumer_photo.url}" width="120">')
        return '-'

    get_photo.short_description = 'Фото'


class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
    'id', 'title', 'custumer', 'project_deadline', 'get_photo', 'created_at', 'start_project', 'status_project')
    list_display_links = ('id', 'title', 'custumer', 'get_photo')
    search_fields = ['title']
    list_filter = ('custumer',)
    readonly_fields = ('created_at', 'get_photo')

    def get_photo(self, obj):
        if obj.project_photo:
            return mark_safe(f'<img src="{obj.project_photo.url}" width="120">')
        return '-'


admin.site.register(Status_project, Status_projectAdmin)
admin.site.register(Type_call, Type_callAdmin)
admin.site.register(Custumer, CustumerAdmin)
admin.site.register(Project, ProjectAdmin)
