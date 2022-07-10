from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class Status_projectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class Type_callAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class DocumentStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class DogovorTaskAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dogovor_task_title', 'task_number', 'task_date', 'task_price', 'document_status')
    list_display_links = ('dogovor_task_title', 'task_number')
    search_fields = ['dogovor_task_title', 'task_number']
    list_filter = ('dogovor',)


class SchetAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('schet_title', 'schet_number', 'schet_date', 'schet_price', 'document_status')
    list_display_links = ('schet_title', 'schet_number')
    search_fields = ['schet_title', 'schet_number']
    list_filter = ('dogovor',)


class AktAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('akt_title', 'akt_number', 'akt_date', 'akt_price', 'document_status')
    list_display_links = ('akt_title', 'akt_number')
    search_fields = ['akt_title', 'akt_number']
    list_filter = ('dogovor',)


class DogovorAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dogovor_title', 'dogovor_number', 'dogovor_date', 'dogovor_price', 'document_status')
    list_display_links = ('dogovor_title', 'dogovor_number')
    search_fields = ['dogovor_title', 'dogovor_number']
    list_filter = ('custumer',)

class CompanyAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'short_name', 'company_email', 'inn', 'kpp', 'director', 'get_logo')
    list_display_links = ('id', 'short_name')
    search_fields = ['short_name']
    readonly_fields = ['created_at']
    prepopulated_fields = {"slug": ("short_name",)}

    def get_logo(self, obj):
        if obj.company_logo:
            return mark_safe(f'<img src="{obj.company_logo.url}" width="120">')
        return '-'

    get_logo.short_description = 'Логотип'

class CustumerAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'name', 'last_name', 'get_photo', 'custumer_phone', 'custumer_email', 'type_call')
    list_display_links = ('id', 'name', 'last_name', 'get_photo')
    search_fields = ['name', 'last_name', 'custumer_phone', 'custumer_email']
    readonly_fields = ('created_at', 'get_photo')
    list_filter = ('company',)
    prepopulated_fields = {"slug": ("surname",)}

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
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, obj):
        if obj.project_photo:
            return mark_safe(f'<img src="{obj.project_photo.url}" width="120">')
        return '-'


admin.site.register(Status_project, Status_projectAdmin)
admin.site.register(Type_call, Type_callAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(DocumentStatus, DocumentStatusAdmin)
admin.site.register(DogovorTask, DogovorTaskAdmin)
admin.site.register(Schet, SchetAdmin)
admin.site.register(Akt, AktAdmin)
admin.site.register(Dogovor, DogovorAdmin)
admin.site.register(Custumer, CustumerAdmin)
admin.site.register(Project, ProjectAdmin)
