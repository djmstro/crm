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
    list_filter = ('document_status', 'dogovor',)


class SchetAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('schet_title', 'schet_number', 'schet_date', 'schet_price', 'document_status')
    list_display_links = ('schet_title', 'schet_number')
    search_fields = ['schet_title', 'schet_number']
    list_filter = ('document_status', 'dogovor',)


class AktAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('akt_title', 'akt_number', 'akt_date', 'akt_price', 'document_status')
    list_display_links = ('akt_title', 'akt_number')
    search_fields = ['akt_title', 'akt_number']
    list_filter = ('document_status', 'dogovor',)


class DogovorAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dogovor_title', 'dogovor_number', 'dogovor_date', 'dogovor_price', 'document_status')
    list_display_links = ('dogovor_title', 'dogovor_number')
    search_fields = ['dogovor_title', 'dogovor_number']
    list_filter = ('document_status', 'custumer',)


class CompanyAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'short_name', 'company_email', 'inn', 'kpp', 'director', 'get_logo')
    list_display_links = ('id', 'short_name')
    search_fields = ['short_name']
    readonly_fields = ['created_at']
    prepopulated_fields = {"slug": ("short_name",)}
    list_filter = ('director',)

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
    list_filter = ('phisic_person', 'company', 'custumer_position',)
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
    list_filter = ('status_project', 'custumer',)
    readonly_fields = ('created_at', 'get_photo')
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, obj):
        if obj.project_photo:
            return mark_safe(f'<img src="{obj.project_photo.url}" width="120">')
        return '-'


class ProjectTaskStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ParkingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'service_comment', 'must_count', 'service_price', 'service_cost')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    list_filter = ('service_category', 'type_of_executor',)


class TypeOfExecutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class TypeOfExecutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class ArchivesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'archives_title', 'created_at', 'full_size', 'sn')
    list_display_links = ('id', 'archives_title')
    search_fields = ['archives_title']
    readonly_fields = ['created_at']
    prepopulated_fields = {"slug": ("archives_title",)}


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class FilePathAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'directory_name', 'created_at', 'size', 'path', 'flash_card_count')
    list_display_links = ('id', 'directory_name')
    search_fields = ['directory_name']
    readonly_fields = ['created_at']
    list_filter = ('archives',)


class ExecutorAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'last_name', 'name', 'created_at', 'phone_number', 'get_photo')
    list_display_links = ('id', 'last_name', 'name', 'get_photo')
    search_fields = ['last_name']
    readonly_fields = ['created_at', 'get_photo']
    prepopulated_fields = {"slug": ("last_name",)}
    list_filter = ('department', 'office', 'driving_license',)

    def get_photo(self, obj):
        if obj.executor_photo:
            return mark_safe(f'<img src="{obj.executor_photo.url}" width="120">')
        return '-'


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'number')
    list_display_links = ('id', 'brand', 'model', 'number')
    search_fields = ['brand', 'model', 'number']
    list_filter = ('executor',)


class TaskAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'id', 'project_task_title', 'created_at', 'task_start_date', 'task_deadline', 'project_task_status',
        'task_type',
        'final_clip_Vimeo')
    list_display_links = ('id', 'project_task_title')
    search_fields = ['project_task_title']
    list_filter = ('project_task_status', 'task_type', 'executor', 'project', 'archives', 'services',)
    readonly_fields = ['created_at']
    prepopulated_fields = {"slug": ("project_task_title",)}


class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class EquipmentBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class EquipmentAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
    'id', 'brand', 'model', 'equipment_description', 'get_photo', 'sn', 'equipment_cost', 'equipment_price', 'link',
    'roma', 'price')
    list_display_links = ('id', 'brand', 'model', 'get_photo')
    search_fields = ['brand', 'model', 'equipment_description', 'sn']
    readonly_fields = ['created_at', 'get_photo']
    list_filter = ('equipment_type', 'brand', 'roma',)

    def get_photo(self, obj):
        if obj.equipment_photo:
            return mark_safe(f'<img src="{obj.equipment_photo.url}" width="120">')
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
admin.site.register(ProjectTaskStatus, ProjectTaskStatusAdmin)
admin.site.register(TaskType, TaskTypeAdmin)
admin.site.register(Parking, ParkingAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(TypeOfExecutor, TypeOfExecutorAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(FilePath, FilePathAdmin)
admin.site.register(Executor, ExecutorAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Archives, ArchivesAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(EquipmentBrand, EquipmentBrandAdmin)
admin.site.register(Equipment, EquipmentAdmin)
