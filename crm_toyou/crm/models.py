from django.db import models

class Project(models.Model) :
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    project_description = models.TextField(verbose_name='Описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    project_photo = models.ImageField(upload_to='photos/catalog/%Y/%m/%d/', verbose_name='Фото', blank=True)
    start_project = models.DateField(verbose_name='Начало', blank=True)
    project_deadline = models.DateField(verbose_name='Дедлайн', blank=True)
    location = models.CharField(max_length=250, verbose_name='Локация', blank=True)
    custumer = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='custumers', verbose_name='Заказчик', blank=True)
    tasks = models.ForeignKey(Tasks, on_delete=models.PROTECT, related_name='tasks', verbose_name='Задачи', blank=True)
    in_charge = models.CharField(max_length=150, verbose_name='Представитель Заказчика', blank=True)
    in_charge_phone = models.CharField(max_length=150, verbose_name='Телефон представителя', blank=True)
    status_project = models.ForeignKey(Status_project, on_delete=models.PROTECT, related_name='status', verbose_name='Статус')
    Dogovor = models.ForeignKey(Dogovor, on_delete=models.PROTECT, related_name='dogovors', verbose_name='Договор', blank=True)
    project_type = models.ForeignKey(Project_type, on_delete=models.PROTECT, related_name='project_types', verbose_name='Тип', blank=True)
    is_long = models.BooleanField(verbose_name='Длительный')