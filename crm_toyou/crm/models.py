from django.db import models

class Status_project(models.Model) :
    title = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Статус проекта"
        verbose_name_plural = "Статусы проектов"

class Type_call(models.Model) :
    title = models.CharField(max_length=100, verbose_name='Тип связи')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Тип связи с Заказчиком"
        verbose_name_plural = "Типы связи с Заказчиком"

class Custumer(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя', blank=True)
    surname = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    birth = models.DateField(verbose_name='Дата рождения', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    custumer_phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    custumer_email = models.EmailField(verbose_name='E-mail', blank=True)
    type_call = models.ForeignKey(Type_call, on_delete=models.PROTECT, related_name='custumers', verbose_name='Тип связи', blank=True)
    custumer_photo = models.ImageField(upload_to='photos/catalog/%Y/%m/%d/', verbose_name='Фото', blank=True)
    custumer_position = models.CharField(max_length=150, verbose_name='Должность', blank=True)
    custumer_adress = models.CharField(max_length=150, verbose_name='Адрес', blank=True)
    custumer_comment = models.TextField(verbose_name='Комментарий', blank=True)
    phisic_person = models.BooleanField(verbose_name='Физическое лицо')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    project_description = models.TextField(verbose_name='Описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    project_photo = models.ImageField(upload_to='photos/catalog/%Y/%m/%d/', verbose_name='Фото', blank=True)
    start_project = models.DateField(verbose_name='Начало', blank=True)
    project_deadline = models.DateField(verbose_name='Дедлайн', blank=True)
    custumer = models.ForeignKey(Custumer, on_delete=models.PROTECT, related_name='projects', verbose_name='Заказчик', blank=True)
    in_charge = models.CharField(max_length=150, verbose_name='Представитель Заказчика', blank=True)
    in_charge_phone = models.CharField(max_length=150, verbose_name='Телефон представителя', blank=True)
    status_project = models.ForeignKey(Status_project, on_delete=models.PROTECT, related_name='projects', verbose_name='Статус')
    is_long = models.BooleanField(verbose_name='Длительный')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


    # Dogovor = models.ForeignKey(Dogovor, on_delete=models.PROTECT, related_name='dogovors', verbose_name='Договор', blank=True)
    # archives = models.ManyToManyField(Archives, on_delete=models.PROTECT, related_name='archives', verbose_name='Архив', blank=True)
    # tasks = models.ForeignKey(Tasks, on_delete=models.PROTECT, related_name='projects', verbose_name='Задачи', blank=True)
