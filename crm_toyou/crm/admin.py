from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class StatusProjectAdmin(admin.ModelAdmin):
    list_display = ['title']


class TypeCallAdmin(admin.ModelAdmin):
    list_display = ['title']


class DocumentStatusAdmin(admin.ModelAdmin):
    list_display = ['title']


class DogovorTaskAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dogovor', 'dogovor_task_title', 'task_number', 'task_date', 'task_price', 'document_status')
    list_display_links = ('dogovor_task_title', 'task_number')
    search_fields = ['dogovor_task_title', 'task_number']
    list_filter = (('document_status', admin.RelatedOnlyFieldListFilter),)


class SchetAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dogovor', 'schet_title', 'schet_number', 'schet_date', 'schet_price', 'document_status')
    list_display_links = ('schet_title', 'schet_number')
    search_fields = ['schet_title', 'schet_number']
    list_filter = (('document_status', admin.RelatedOnlyFieldListFilter),)


class AktAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dogovor', 'akt_title', 'akt_number', 'akt_date', 'akt_price', 'document_status')
    list_display_links = ('akt_title', 'akt_number')
    search_fields = ['akt_title', 'akt_number']
    list_filter = (('document_status', admin.RelatedOnlyFieldListFilter),)


class DogovorAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dogovor_title', 'dogovor_number', 'dogovor_date', 'dogovor_price', 'document_status')
    list_display_links = ('dogovor_title', 'dogovor_number')
    search_fields = ['dogovor_title', 'dogovor_number']
    list_filter = (
        ('document_status', admin.RelatedOnlyFieldListFilter), ('custumer', admin.RelatedOnlyFieldListFilter),)


class CompanyAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('short_name', 'company_email', 'inn', 'kpp', 'director', 'get_logo')
    list_display_links = ['short_name']
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
    list_display = (
        'get_photo', 'name', 'last_name', 'company', 'custumer_position', 'custumer_phone', 'custumer_email',
        'custumer_tg', 'type_call')
    list_display_links = ('name', 'last_name', 'get_photo')
    search_fields = ['name', 'last_name', 'custumer_phone', 'custumer_email', 'custumer_tg']
    readonly_fields = ('created_at', 'get_photo')
    list_filter = (('phisic_person', admin.BooleanFieldListFilter), 'company', 'custumer_position',)
    prepopulated_fields = {"slug": ("last_name",)}
    list_editable = ('type_call',)
    fieldsets = (
        (None, {
            'fields': ('name', 'last_name', 'slug', 'surname', 'custumer_photo', 'birth')
        }),
        ('Контактная информация', {
            'fields': ('custumer_phone', 'custumer_email', 'custumer_tg', 'type_call')
        }),
        ('Компания', {
            'fields': ('phisic_person', 'company', 'custumer_position', 'custumer_adress')
        }),
        ('Остальное', {
            'fields': ('custumer_comment', 'created_at')
        }),
    )

    def get_photo(self, obj):
        if obj.custumer_photo:
            return mark_safe(f'<img src="{obj.custumer_photo.url}" width="120">')
        return '-'

    get_photo.short_description = 'Фото'


class IsPaidAdmin(admin.ModelAdmin):
    list_display = ['title']


class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'title', 'custumer', 'created_at', 'status_project', 'is_long', 'get_dogovor', 'get_document_status',
        'get_dogovor_price', 'is_paid')
    list_display_links = ('title', 'custumer')
    search_fields = ['title']
    list_filter = ('status_project', 'is_paid', ('custumer', admin.RelatedOnlyFieldListFilter),)
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('status_project',)
    readonly_fields = ['created_at']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'project_description', 'project_photo')
        }),
        ('Сроки', {
            'fields': ('created_at', 'start_project', 'project_deadline')
        }),
        ('Заказчик, представители заказчика', {
            'fields': ('custumer', 'in_charge', 'in_charge_phone')
        }),
        ('Процесс', {
            'fields': ('status_project', 'is_long')
        }),
        ('Документы', {
            'fields': ('dogovor', 'origin_tz', 'kp')
        }),
        ('Стоимость', {
            'fields': ('project_cost', 'project_price', 'is_paid')
        }),
    )

    def get_photo(self, obj):
        if obj.project_photo:
            return mark_safe(f'<img src="{obj.project_photo.url}" width="120">')
        return '-'

    get_photo.short_description = 'Фото'

    def get_dogovor(self, obj):
        return ", \n".join([p.dogovor_number for p in obj.dogovor.all()])

    get_dogovor.short_description = 'Договор'

    def get_document_status(self, obj):
        return [p.document_status for p in obj.dogovor.all()]

    get_document_status.short_description = 'Статус документа'

    def get_dogovor_price(self, obj):
        return [p.dogovor_price for p in obj.dogovor.all()]

    get_dogovor_price.short_description = 'Сумма договора'


class ProjectTaskStatusAdmin(admin.ModelAdmin):
    list_display = ['title']


class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ['title']


class ParkingAdmin(admin.ModelAdmin):
    list_display = ['title']


class ServiceCategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'service_category', 'type_of_executor', 'title', 'service_comment', 'must_count', 'service_price',
        'service_cost')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    list_filter = ('service_category', 'type_of_executor',)


class TypeOfExecutorAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class TypeOfArchiveAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ArchivesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'get_photo', 'brand', 'archives_title', 'archives_subtitle', 'type_of_archive', 'created_at', 'full_size', 'sn')
    list_display_links = ('id', 'get_photo', 'archives_title')
    search_fields = ['archives_title', 'archives_subtitle']
    readonly_fields = ['created_at', 'get_photo']
    prepopulated_fields = {"slug": ("archives_title",)}
    list_filter = (('brand', admin.RelatedOnlyFieldListFilter), 'type_of_archive', 'full_size',)

    def get_photo(self, obj):
        if obj.archives_photo:
            return mark_safe(f'<img src="{obj.archives_photo.url}" width="120">')
        return '-'

    get_photo.short_description = 'Фото'


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class FilePathAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'archives', 'path', 'created_at', 'size', 'flash_card_count')
    search_fields = ['directory_name']
    readonly_fields = ['created_at']
    list_filter = (('archives', admin.RelatedOnlyFieldListFilter),)
    list_editable = ('archives', 'path', 'size', 'flash_card_count',)


class TypeOfInteractionAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ExecutorLevelAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ExecutorSkillsAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ExecutorProgramsAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ReferencePlatformAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'reference_url', 'reference_comment')
    list_display_links = ('id', 'title', 'reference_url',)
    search_fields = ['title', 'reference_url', ]
    list_filter = (
        ('executor_level', admin.RelatedOnlyFieldListFilter), ('executor_skills', admin.RelatedOnlyFieldListFilter),
        'reference_platform',)


class CostValueAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ExecutorAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'get_photo', 'name', 'last_name', 'get_type_of_executor', 'phone_number', 'executor_email', 'executor_tg',
        'get_executor_skills', 'driving_license', 'executor_level', 'executor_city', 'get_reference')
    list_display_links = ('last_name', 'name', 'get_photo')
    search_fields = ['name', 'last_name', 'phone_number', 'executor_email', 'executor_tg']
    readonly_fields = ['created_at', 'get_photo']
    prepopulated_fields = {"slug": ("last_name",)}
    list_filter = (
        'type_of_interaction', 'executor_programs', ('executor_skills', admin.RelatedOnlyFieldListFilter),
        ('executor_level', admin.RelatedOnlyFieldListFilter),
        'department', ('type_of_executor', admin.RelatedOnlyFieldListFilter),
        ('driving_license', admin.BooleanFieldListFilter),)
    fieldsets = (
        (None, {
            'fields': ('name', 'last_name', 'slug', 'surname', 'executor_photo', 'executor_city')
        }),
        ('Структурное подразделение', {
            'fields': ('type_of_interaction', 'department', 'type_of_executor')
        }),
        ('Контактная информация', {
            'fields': ('phone_number', 'executor_email', 'executor_tg')
        }),
        ('Навыки и умения', {
            'fields': ('executor_skills', 'executor_programs', 'executor_level', 'reference')
        }),
        ('Оплата и стоимость', {
            'fields': ('executor_cost', 'cost_value', 'credit_card')
        }),
        ('Паспортные данные', {
            'fields': (
                'birth', 'passport_s', 'passport_n', 'vydan', 'data_vydachi', 'adress', 'adress_date', 'birth_location',
                'kod_podrazdelenia')
        }),
        ('Автомобиль', {
            'fields': ('driving_license', 'car')
        }),
        ('Остальное', {
            'fields': ('executor_comment', 'created_at')
        }),
    )

    def get_photo(self, obj):
        if obj.executor_photo:
            return mark_safe(f'<img src="{obj.executor_photo.url}" width="120">')
        return '-'

    get_photo.short_description = 'Фото'

    def get_executor_skills(self, obj):
        return ", \n".join([p.title for p in obj.executor_skills.all()])

    get_executor_skills.short_description = 'Навыки'

    def get_type_of_executor(self, obj):
        return ", \n".join([p.title for p in obj.type_of_executor.all()])

    get_type_of_executor.short_description = 'Должность'

    def get_reference(self, obj):
        return "\n".join([p.reference_url for p in obj.reference.all()])

    get_reference.short_description = 'Референсы'


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'number')
    list_display_links = ('brand', 'model', 'number')
    search_fields = ['brand', 'model', 'number']


class TaskAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'id', 'project_task_title', 'project', 'get_executor', 'created_at', 'priority', 'task_start_date',
        'task_deadline',
        'project_task_status',
        'task_type', 'get_archive', 'get_file_path', 'comment', 'final_clip_Vimeo', 'final_clip_yandex')
    list_display_links = ('id', 'project_task_title')
    search_fields = ['project_task_title']
    list_filter = (
        ('project_task_status', admin.RelatedOnlyFieldListFilter), 'priority',
        ('task_type', admin.RelatedOnlyFieldListFilter),
        ('executor', admin.RelatedOnlyFieldListFilter), 'project', ('services', admin.RelatedOnlyFieldListFilter),)
    readonly_fields = ['created_at']
    list_editable = (
        'task_start_date', 'task_deadline', 'project_task_status',)
    fieldsets = (
        (None, {
            'fields': ('project_task_title', 'priority', 'comment')
        }),
        ('Сроки', {
            'fields': ('created_at', 'task_start_date', 'task_deadline')
        }),
        ('Детальная информация', {
            'fields': ('task_type', 'project', 'executor', 'services')
        }),
        ('Процесс', {
            'fields': ['project_task_status']
        }),
        ('Расположение файлов', {
            'fields': ['file_path']
        }),
        ('Съемка', {
            'fields': ['location']
        }),
        ('Итоговые файлы', {
            'fields': ('final_clip_yandex', 'final_clip_Vimeo')
        }),
    )

    def get_executor(self, obj):
        return ", \n".join([p.name + " " + p.last_name for p in obj.executor.all()])

    get_executor.short_description = 'Ответственный'

    def get_file_path(self, obj):
        return ", \n".join([p.path for p in obj.file_path.all()])

    get_file_path.short_description = 'Расположение файлов'

    def get_archive(self, obj):
        return [p.archives for p in obj.file_path.all()]

    get_archive.short_description = 'Архив'


class EquipmentTypeAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class EquipmentBrandAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class EquipmentLocationAdmin(admin.ModelAdmin):
    search_fields = ['title']


class EquipmentAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'id', 'get_photo', 'brand', 'model', 'equipment_description', 'additional', 'count', 'comment', 'owner_office',
        'owner_executor',
        'sn', 'link',
        'equipment_location', 'defect')
    list_display_links = ('id', 'brand', 'model', 'get_photo')
    search_fields = ['model', 'equipment_description', 'sn']
    readonly_fields = ['created_at', 'get_photo']
    list_filter = (
        'equipment_type', 'owner_office', ('owner_executor', admin.RelatedOnlyFieldListFilter),
        ('brand', admin.RelatedOnlyFieldListFilter), ('equipment_location', admin.RelatedOnlyFieldListFilter),)
    fieldsets = (
        (None, {
            'fields': (
                'equipment_type', 'brand', 'model', 'equipment_description', 'count', 'defect', 'additional', 'comment',
                'equipment_photo')
        }),
        ('Информация о покупке', {
            'fields': ('sn', 'buy_date', 'chek_number', 'chek_date', 'created_at')
        }),
        ('Владение', {
            'fields': ('owner_office', 'owner_executor', 'owner_arenda', 'roma')
        }),
        ('Стоимость', {
            'fields': ('equipment_cost', 'equipment_price', 'price', 'link')
        }),
        ('Место хранения', {
            'fields': ['equipment_location']
        }),
    )

    def get_photo(self, obj):
        if obj.equipment_photo:
            return mark_safe(f'<img src="{obj.equipment_photo.url}" width="120">')
        return '-'

    get_photo.short_description = 'Фото'


class IncomingTypeAdmin(admin.ModelAdmin):
    search_fields = ['title']


class IncomingAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'id', 'title', 'created_at', 'incoming_value', 'incoming_type', 'custumer', 'company', 'schet', 'project',
        'comment')
    list_display_links = ('id', 'title')
    search_fields = ['custumer', 'incoming_value', 'company', 'schet', 'project']
    list_filter = (
        'incoming_type', ('company', admin.RelatedOnlyFieldListFilter), ('custumer', admin.RelatedOnlyFieldListFilter),
        ('project', admin.RelatedOnlyFieldListFilter),)


class OutComingTargetAdmin(admin.ModelAdmin):
    search_fields = ['title']


class OutComingAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'id', 'title', 'created_at', 'outcoming_value', 'outcoming_target', 'outcoming_type', 'executor', 'company',
        'project', 'comment')
    list_display_links = ('id', 'title')
    search_fields = ['executor', 'company', 'outcoming_value', 'project', 'outcoming_target', 'outcoming_type']
    list_filter = (
        'outcoming_type', 'outcoming_target', ('company', admin.RelatedOnlyFieldListFilter),
        ('executor', admin.RelatedOnlyFieldListFilter),
        ('project', admin.RelatedOnlyFieldListFilter),)


class LocationTypeAdmin(admin.ModelAdmin):
    search_fields = ['title']


class LocationAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'get_photo', 'id', 'title', 'created_at', 'location_adress', 'location_cost', 'location_phone', 'parking',
        'location_type', 'location_comment')
    list_display_links = ('get_photo', 'id', 'title', 'location_adress')
    search_fields = ['title', 'location_adress', 'location_phone', 'location_comment']
    readonly_fields = ['created_at', 'get_photo']
    list_filter = (
        ('parking', admin.RelatedOnlyFieldListFilter),
        ('location_type', admin.RelatedOnlyFieldListFilter),)
    list_editable = ('location_phone',)
    fieldsets = (
        (None, {
            'fields': ('title', 'location_type', 'created_at', 'location_adress', 'location_cost')
        }),
        ('Контактная информация', {
            'fields': ('location_url', 'location_phone')
        }),
        ('Дополнительно', {
            'fields': ('parking', 'location_comment')
        }),
        ('Фотографии', {
            'fields': ('location_photo_1', 'location_photo_2', 'location_photo_3')
        }),
    )

    def get_photo(self, obj):
        if obj.location_photo_1:
            return mark_safe(f'<img src="{obj.location_photo_1.url}" width="120">')
        return '-'

    get_photo.short_description = 'Фото'


class KnowledgeBaseCategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class KnowledgeBaseItemAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'id', 'get_photo', 'title', 'created_at', 'knowledge_base_category', 'author', 'is_active')
    list_display_links = ('id', 'title', 'get_photo')
    search_fields = ['title']
    readonly_fields = ['created_at', 'get_photo']
    list_filter = (
        ('knowledge_base_category', admin.RelatedOnlyFieldListFilter),)
    list_editable = ('is_active',)
    fieldsets = (
        (None, {
            'fields': (
                'knowledge_base_category', 'title', 'knowledge_base_photo', 'content', 'author', 'is_active',
                'created_at')
        }),
    )

    def get_photo(self, obj):
        if obj.knowledge_base_photo:
            return mark_safe(f'<img src="{obj.knowledge_base_photo.url}" width="120">')
        return '-'

    get_photo.short_description = 'Фото'


class SubscriptionPlanAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ProgramItemAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'id', 'title', 'program_login', 'program_email', 'program_password', 'get_computers', 'program_license', 'activation_date', 'activation_for', 'subscription_plan', 'program_cost', 'program_url', 'is_active')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    readonly_fields = ['created_at']

    def get_computers(self, obj):
        return ", \n".join([p.title for p in obj.computers.all()])

    get_computers.short_description = 'Компьютеры'


class ComputersAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'get_photo', 'id', 'title', 'executor', 'videocard', 'get_hdd')
    list_display_links = ('get_photo', 'id', 'title')
    search_fields = ['title']
    readonly_fields = ['created_at', 'get_photo']
    list_filter = [('executor', admin.RelatedOnlyFieldListFilter),]

    def get_photo(self, obj):
        if obj.computer_photo:
            return mark_safe(f'<img src="{obj.computer_photo.url}" width="120">')
        return '-'

    get_photo.short_description = 'Фото'

    def get_hdd(self, obj):
        return ", \n".join([p.archives_title for p in obj.hdd.all()])

    get_hdd.short_description = 'Жесткие диски'


admin.site.register(StatusProject, StatusProjectAdmin)
admin.site.register(TypeCall, TypeCallAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(DocumentStatus, DocumentStatusAdmin)
admin.site.register(DogovorTask, DogovorTaskAdmin)
admin.site.register(Schet, SchetAdmin)
admin.site.register(Akt, AktAdmin)
admin.site.register(Dogovor, DogovorAdmin)
admin.site.register(Custumer, CustumerAdmin)
admin.site.register(IsPaid, IsPaidAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTaskStatus, ProjectTaskStatusAdmin)
admin.site.register(TaskType, TaskTypeAdmin)
admin.site.register(Parking, ParkingAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(TypeOfExecutor, TypeOfExecutorAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(FilePath, FilePathAdmin)
admin.site.register(TypeOfInteraction, TypeOfInteractionAdmin)
admin.site.register(ExecutorLevel, ExecutorLevelAdmin)
admin.site.register(ExecutorSkills, ExecutorSkillsAdmin)
admin.site.register(ExecutorPrograms, ExecutorProgramsAdmin)
admin.site.register(ReferencePlatform, ReferencePlatformAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(CostValue, CostValueAdmin)
admin.site.register(Executor, ExecutorAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(TypeOfArchive, TypeOfArchiveAdmin)
admin.site.register(Archives, ArchivesAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(EquipmentBrand, EquipmentBrandAdmin)
admin.site.register(EquipmentLocation, EquipmentLocationAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(IncomingType, IncomingTypeAdmin)
admin.site.register(Incoming, IncomingAdmin)
admin.site.register(OutComingTarget, OutComingTargetAdmin)
admin.site.register(OutComing, OutComingAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(KnowledgeBaseCategory, KnowledgeBaseCategoryAdmin)
admin.site.register(KnowledgeBaseItem, KnowledgeBaseItemAdmin)
admin.site.register(SubscriptionPlan, SubscriptionPlanAdmin)
admin.site.register(ProgramItem, ProgramItemAdmin)
admin.site.register(Computers, ComputersAdmin)
