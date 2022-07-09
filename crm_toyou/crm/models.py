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
    birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    custumer_phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    custumer_email = models.EmailField(verbose_name='E-mail', blank=True)
    type_call = models.ForeignKey(Type_call, on_delete=models.PROTECT, related_name='custumers',
                                  verbose_name='Тип связи', null=True, blank=True)
    custumer_photo = models.ImageField(upload_to='photos/catalog/%Y/%m/%d/', verbose_name='Фото', blank=True)
    custumer_position = models.CharField(max_length=150, verbose_name='Должность', blank=True)
    custumer_adress = models.CharField(max_length=150, verbose_name='Адрес', blank=True)
    custumer_comment = models.TextField(verbose_name='Комментарий', blank=True)
    phisic_person = models.BooleanField(verbose_name='Физическое лицо')

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ['id']
        verbose_name = "Заказчика"
        verbose_name_plural = "Заказчики"


class DocumentStatus(models.Model):
    title = models.CharField(max_length=150, verbose_name='Статус документа')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Статус документа"
        verbose_name_plural = "Статусы документов"

class Dogovor(models.Model):
    dogovor_title = models.CharField(max_length=150, verbose_name='Название', blank=True)
    dogovor_number = models.CharField(max_length=150, verbose_name='Номер Договора', blank=True)
    dogovor_date = models.DateField(verbose_name='Дата Договора', null=True, blank=True)
    dogovor_file = models.FileField(upload_to='docs/dogovors/', verbose_name='Файл', null=True, blank=True)
    dogovor_price = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Стоимость', blank=True)
    document_status = models.ForeignKey(DocumentStatus, on_delete=models.PROTECT, related_name='projects',
                                        verbose_name='Статус', null=True, blank=True)
    custumer = models.ForeignKey(to=Custumer, on_delete=models.PROTECT, related_name='dogovor_custumer',
                                 verbose_name='Заказчик', null=True, blank=True)

    def __str__(self):
        return self.dogovor_title

    class Meta:
        ordering = ['id']
        verbose_name = "Договор"
        verbose_name_plural = "Договоры"


class DogovorTask(models.Model):
    dogovor_task_title = models.CharField(max_length=150, verbose_name='Название Задания', blank=True)
    task_number = models.CharField(max_length=150, verbose_name='Номер Задания', blank=True)
    task_date = models.DateField(verbose_name='Дата Задания', null=True, blank=True)
    task_file = models.FileField(upload_to='docs/tasks/', verbose_name='Файл Задания', null=True, blank=True)
    task_price = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Сумма', blank=True)
    document_status = models.ForeignKey(DocumentStatus, on_delete=models.PROTECT, related_name='dogovor_tasks',
                                        verbose_name='Статус', null=True, blank=True)
    dogovor = models.ForeignKey(to=Dogovor, on_delete=models.PROTECT, related_name='dogovor_tasks',
                                verbose_name='Договор', null=True, blank=True)

    def __str__(self):
        return self.dogovor_task_title

    class Meta:
        ordering = ['id']
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class Schet(models.Model):
    schet_title = models.CharField(max_length=150, verbose_name='Название счета', blank=True)
    schet_number = models.CharField(max_length=150, verbose_name='Номер счета', blank=True)
    schet_date = models.DateField(verbose_name='Дата счета', null=True, blank=True)
    schet_file = models.FileField(upload_to='docs/schets/', verbose_name='Файл счета', null=True, blank=True)
    schet_price = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Сумма', blank=True)
    document_status = models.ForeignKey(DocumentStatus, on_delete=models.PROTECT, related_name='dogovor_schets',
                                        verbose_name='Статус', null=True, blank=True)
    dogovor = models.ForeignKey(to=Dogovor, on_delete=models.PROTECT, related_name='dogovor_schets',
                                verbose_name='Договор', null=True, blank=True)

    def __str__(self):
        return self.schet_title

    class Meta:
        ordering = ['id']
        verbose_name = "Счет"
        verbose_name_plural = "Счета"


class Akt(models.Model):
    akt_title = models.CharField(max_length=150, verbose_name='Название акта', blank=True)
    akt_number = models.CharField(max_length=150, verbose_name='Номер акта', blank=True)
    akt_date = models.DateField(verbose_name='Дата акта', null=True, blank=True)
    akt_file = models.FileField(upload_to='docs/acts/', verbose_name='Файл акта', null=True, blank=True)
    akt_price = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Сумма', blank=True)
    document_status = models.ForeignKey(DocumentStatus, on_delete=models.PROTECT, related_name='dogovor_akts',
                                        verbose_name='Статус', null=True, blank=True)
    dogovor = models.ForeignKey(to=Dogovor, on_delete=models.PROTECT, related_name='dogovor_acts',
                                verbose_name='Договор', null=True, blank=True)

    def __str__(self):
        return self.akt_title

    class Meta:
        ordering = ['id']
        verbose_name = "Акт"
        verbose_name_plural = "Акты"


class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    project_description = models.TextField(verbose_name='Описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    project_photo = models.ImageField(upload_to='photos/catalog/%Y/%m/%d/', verbose_name='Фото', blank=True)
    start_project = models.DateField(verbose_name='Начало', null=True, blank=True)
    project_deadline = models.DateField(verbose_name='Дедлайн', null=True, blank=True)
    custumer = models.ForeignKey(Custumer, on_delete=models.PROTECT, related_name='projects', verbose_name='Заказчик',
                                 null=True, blank=True)
    in_charge = models.CharField(max_length=150, verbose_name='Представитель Заказчика', blank=True)
    in_charge_phone = models.CharField(max_length=150, verbose_name='Телефон представителя', blank=True)
    status_project = models.ForeignKey(Status_project, on_delete=models.PROTECT, related_name='projects',
                                       verbose_name='Статус')
    is_long = models.BooleanField(verbose_name='Длительный')
    dogovor = models.ManyToManyField(Dogovor, related_name='dogovors', verbose_name='Договор', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    # archives = models.ManyToManyField(Archives, on_delete=models.PROTECT, related_name='archives', verbose_name='Архив', blank=True)
    # tasks = models.ForeignKey(Tasks, on_delete=models.PROTECT, related_name='projects', verbose_name='Задачи', blank=True)
