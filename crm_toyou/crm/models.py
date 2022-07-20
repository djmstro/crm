from django.db import models


class Status_project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Статус проекта"
        verbose_name_plural = "Статусы проектов"


class Type_call(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип связи')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Тип связи с Заказчиком"
        verbose_name_plural = "Типы связи с Заказчиком"


class Company(models.Model):
    name = models.TextField(verbose_name='Название', blank=True)
    short_name = models.CharField(max_length=200, verbose_name='Короткое название', blank=True)
    slug = models.SlugField(max_length=200, verbose_name='Url', unique=True)
    company_adress = models.TextField(verbose_name='Адрес', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлена')
    company_phone_number = models.CharField(max_length=100, verbose_name='Телефон', blank=True)
    company_email = models.EmailField(verbose_name='Email', blank=True)
    inn = models.BigIntegerField(verbose_name='ИНН', blank=True)
    kpp = models.BigIntegerField(verbose_name='КПП', blank=True)
    ogrn = models.BigIntegerField(verbose_name='ОГРН', blank=True)
    rs = models.CharField(max_length=30, verbose_name='Расчетный счет', blank=True)
    bank_name = models.CharField(max_length=200, verbose_name='Банк', blank=True)
    korr_schet = models.CharField(max_length=30, verbose_name='Корреспондентский счет', blank=True)
    bik = models.BigIntegerField(verbose_name='БИК', blank=True)
    director = models.CharField(max_length=200, verbose_name='Директор')
    director_main = models.TextField(verbose_name='На основании', blank=True)
    company_logo = models.ImageField(upload_to='companies_logo/', verbose_name='Логотип', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True)

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ['id']
        verbose_name = "Компанию"
        verbose_name_plural = "Компании"


class Custumer(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя', blank=True)
    surname = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    custumer_phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    custumer_email = models.EmailField(verbose_name='E-mail', blank=True)
    custumer_tg = models.CharField(max_length=100, verbose_name='Телеграм', blank=True)
    type_call = models.ForeignKey(Type_call, on_delete=models.PROTECT, related_name='custumers',
                                  verbose_name='Тип связи', null=True, blank=True)
    custumer_photo = models.ImageField(upload_to='photos/catalog/%Y/%m/%d/', verbose_name='Фото', null=True, blank=True)
    custumer_position = models.CharField(max_length=150, verbose_name='Должность', blank=True)
    custumer_adress = models.CharField(max_length=150, verbose_name='Адрес', blank=True)
    custumer_comment = models.TextField(verbose_name='Комментарий', blank=True)
    company = models.ForeignKey(to=Company, on_delete=models.PROTECT, related_name='custumer_company',
                                verbose_name='Компания', null=True, blank=True)
    phisic_person = models.BooleanField(verbose_name='Физическое лицо')

    def __str__(self):
        return self.name + " " + self.last_name

    class Meta:
        ordering = ['id']
        verbose_name = "Заказчика"
        verbose_name_plural = "003_Заказчики"


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
        verbose_name_plural = "007_Договоры"


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
        verbose_name_plural = "008_Задания"


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
        verbose_name_plural = "009_Счета"


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
        verbose_name_plural = "010_Акты"


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
        verbose_name_plural = "001_Проекты"


class ProjectTaskStatus(models.Model):
    title = models.CharField(max_length=100, verbose_name='Статус задачи')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Статус задачи"
        verbose_name_plural = "Статусы задач"


class TaskType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип задачи')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Тип задачи"
        verbose_name_plural = "Типы задач"


class Parking(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип парковки')
    parking_price = models.DecimalField(default=40, max_digits=5, decimal_places=0, verbose_name='Стоимость',
                                        blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Тип парковки"
        verbose_name_plural = "Типы парковок"


class ServiceCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    service_category_description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Категорию услуги"
        verbose_name_plural = "Категории услуг"


class TypeOfExecutor(models.Model):
    title = models.CharField(max_length=100, verbose_name='Должность')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Сотрудника"
        verbose_name_plural = "Сотрудники"


class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name='Услуга')
    type_of_executor = models.ForeignKey(TypeOfExecutor, on_delete=models.PROTECT, related_name='service_type_executor',
                                         verbose_name='Сотрудник', null=True, blank=True)
    service_description = models.TextField(verbose_name='Описание', blank=True)
    service_comment = models.CharField(max_length=100, verbose_name='Комментарий', blank=True)
    service_price = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Стоимость для клиента',
                                        blank=True)
    service_cost = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Себестоимость',
                                       blank=True)
    must_count = models.IntegerField(default=1, verbose_name='Кол-во')
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT, related_name='service_cat',
                                         verbose_name='Категория', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Услугу"
        verbose_name_plural = "005_Услуги"


class Department(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название отдела')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"


class Car(models.Model):
    brand = models.CharField(max_length=100, verbose_name='Марка', blank=True)
    model = models.CharField(max_length=100, verbose_name='Модель', blank=True)
    number = models.CharField(max_length=100, verbose_name='Регистрационный номер', blank=True)
    color = models.CharField(max_length=100, verbose_name='Цвет авто', blank=True)

    def __str__(self):
        return self.brand + " " + self.model + " " + self.number

    class Meta:
        ordering = ['id']
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class TypeOfInteraction(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Тип взаимодейтсвия"
        verbose_name_plural = "Типы взаимодействия"


class ExecutorLevel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Уровень Исполнителя"
        verbose_name_plural = "Уровни Исполнителей"


class ExecutorSkills(models.Model):
    title = models.CharField(max_length=100, verbose_name='Навык')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Навык Исполнителя"
        verbose_name_plural = "Навыки Исполнителей"


class ExecutorPrograms(models.Model):
    title = models.CharField(max_length=100, verbose_name='Программа')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Работа в программах"
        verbose_name_plural = "Работа в программах"


class ReferencePlatform(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Платформа для референсов"
        verbose_name_plural = "Платформы для референсов"


class Reference(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', blank=True)
    reference_url = models.URLField(verbose_name='Ссылка на референс', blank=True)
    reference_comment = models.TextField(verbose_name='Комментарий', blank=True)
    executor_skills = models.ManyToManyField(ExecutorSkills, related_name='reference_skills', verbose_name='Навыки',
                                             blank=True)
    executor_level = models.ForeignKey(to=ExecutorLevel, on_delete=models.PROTECT, related_name='reference_level',
                                       verbose_name='Уровень', null=True, blank=True)
    reference_platform = models.ForeignKey(ReferencePlatform, on_delete=models.PROTECT,
                                           related_name='reference_platform',
                                           verbose_name='Платформа', null=True, blank=True)

    def __str__(self):
        return self.reference_url

    class Meta:
        ordering = ['id']
        verbose_name = "Референс"
        verbose_name_plural = "Референсы"

class CostValue(models.Model):
    title = models.CharField(max_length=150, verbose_name='Ед.измерения')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Единицу измерения"
        verbose_name_plural = "Единицы измерения"

class Executor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', blank=True)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', blank=True)
    surname = models.CharField(max_length=100, verbose_name='Отчество', blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    type_of_interaction = models.ForeignKey(to=TypeOfInteraction, on_delete=models.PROTECT,
                                            related_name='executor_interaction', verbose_name='Тип взаимодейтсвия',
                                            null=True, blank=True)
    department = models.ManyToManyField(Department, related_name='executor_department', verbose_name='Отдел',
                                        blank=True)
    type_of_executor = models.ManyToManyField(TypeOfExecutor, related_name='executor_type_of', verbose_name='Должность',
                                              blank=True)
    executor_skills = models.ManyToManyField(ExecutorSkills, related_name='executor_skills', verbose_name='Навыки',
                                             blank=True)
    executor_programs = models.ManyToManyField(ExecutorPrograms, related_name='executor_programs',
                                               verbose_name='Программы',
                                               blank=True)
    executor_photo = models.ImageField(upload_to='executor_photo/', verbose_name='Фото', null=True, blank=True)
    phone_number = models.CharField(max_length=100, verbose_name='Телефон', blank=True)
    executor_email = models.EmailField(verbose_name='E-mail', blank=True)
    executor_tg = models.CharField(max_length=100, verbose_name='Телеграм', blank=True)
    birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    passport_s = models.IntegerField(verbose_name='Серия паспорта', null=True, blank=True)
    passport_n = models.IntegerField(verbose_name='Номер паспорта', null=True, blank=True)
    vydan = models.TextField(verbose_name='Выдан', blank=True)
    data_vydachi = models.DateField(verbose_name='Дата выдачи', null=True, blank=True)
    adress = models.TextField(verbose_name='Прописка', blank=True)
    adress_date = models.DateField(verbose_name='Дата регистрации', null=True, blank=True)
    birth_location = models.TextField(verbose_name='Место рождения', blank=True)
    kod_podrazdelenia = models.IntegerField(verbose_name='Код подразделения', null=True, blank=True)
    driving_license = models.BooleanField(verbose_name='в/у')
    car = models.ManyToManyField(Car, related_name='executor_car', verbose_name='Авто', blank=True)
    executor_cost = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Ставка', blank=True)
    cost_value = models.ForeignKey(CostValue, on_delete=models.PROTECT, related_name='executor_cost_value',
                                   verbose_name='ед.измерения', null=True, blank=True)
    executor_level = models.ForeignKey(to=ExecutorLevel, on_delete=models.PROTECT, related_name='executor_level',
                                       verbose_name='Уровень', null=True, blank=True)
    executor_city = models.CharField(max_length=100, verbose_name='Город', blank=True)
    credit_card = models.BigIntegerField(verbose_name='Банковская карта', null=True, blank=True)
    reference = models.ManyToManyField(Reference, related_name='executor_reference', verbose_name='Референс',
                                       blank=True)
    executor_comment = models.TextField(verbose_name='Комментарий', blank=True)

    def __str__(self):
        return self.name + " " + self.last_name

    class Meta:
        ordering = ['-id']
        verbose_name = "Исполнителя"
        verbose_name_plural = "004_Исполнители"


class Archives(models.Model):
    archives_title = models.CharField(max_length=100, verbose_name='Название архива')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    full_size = models.IntegerField(default=2000, verbose_name='Размер диска,МБ', blank=True)
    sn = models.CharField(max_length=100, verbose_name='Серийный номер', blank=True)

    def __str__(self):
        return self.archives_title

    class Meta:
        ordering = ['id']
        verbose_name = "Архив"
        verbose_name_plural = "011_Архивы"


class FilePath(models.Model):
    path = models.CharField(max_length=100, verbose_name='Путь', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    size = models.IntegerField(default=0, verbose_name='Размер папки,МБ', blank=True)
    flash_card_count = models.IntegerField(default=1, verbose_name='Количество флешек', blank=True)
    archives = models.ForeignKey(to=Archives, on_delete=models.PROTECT, related_name='filepath_archives',
                                 verbose_name='Архив', null=True, blank=True)

    def __str__(self):
        return self.path

    class Meta:
        ordering = ['id']
        verbose_name = "Директорию файла"
        verbose_name_plural = "012_Директории  файлов"


class Task(models.Model):
    priority = models.IntegerField(default=5, verbose_name='Приоритет')
    project_task_title = models.CharField(max_length=150, verbose_name='Задача')
    location = models.CharField(max_length=150, verbose_name='Локация', blank=True)
    services = models.ManyToManyField(Services, related_name='tasks_services', verbose_name='Услуги', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    executor = models.ManyToManyField(Executor, related_name='tasks_executor', verbose_name='Исполнители', blank=True)
    file_path = models.ManyToManyField(FilePath, related_name='tasks_file_path', verbose_name='Расположение файлов',
                                       blank=True)
    task_start_date = models.DateField(verbose_name='Начало', null=True, blank=True)
    task_deadline = models.DateField(verbose_name='Дедлайн', null=True, blank=True)
    project_task_status = models.ForeignKey(ProjectTaskStatus, on_delete=models.PROTECT,
                                            related_name='project_task_status', verbose_name='Статус задачи', null=True,
                                            blank=True)
    project = models.ForeignKey(to=Project, on_delete=models.PROTECT, related_name='project', verbose_name='Проект',
                                null=True, blank=True)
    task_type = models.ForeignKey(TaskType, on_delete=models.PROTECT, related_name='task_type',
                                  verbose_name='Тип задачи', null=True, blank=True)
    parking = models.ForeignKey(Parking, on_delete=models.PROTECT, related_name='task_parking',
                                verbose_name='Тип парковки', null=True, blank=True)
    final_clip_Vimeo = models.URLField(verbose_name='Финальное видео Vimeo', blank=True)
    final_clip_yandex = models.URLField(verbose_name='Финальное видео ЯД', blank=True)

    def __str__(self):
        return self.project_task_title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Задачу"
        verbose_name_plural = "002_Задачи"


class EquipmentType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Тип оборудования"
        verbose_name_plural = "Типы оборудования"


class EquipmentBrand(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Бренд оборудования"
        verbose_name_plural = "Бренды оборудования"


class Equipment(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.PROTECT, related_name='equipment_type',
                                       verbose_name='Тип оборудования', null=True, blank=True)
    brand = models.ForeignKey(EquipmentBrand, on_delete=models.PROTECT, related_name='equipment_brand',
                              verbose_name='Бренд', null=True, blank=True)
    model = models.CharField(max_length=100, verbose_name='Модель', blank=True)
    equipment_description = models.TextField(verbose_name='Описание', blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    buy_date = models.DateField(verbose_name='Дата покупки по чеку', null=True, blank=True)
    chek_number = models.CharField(max_length=150, verbose_name='Номер документа', blank=True)
    chek_date = models.DateField(verbose_name='Дата документа', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    sn = models.CharField(max_length=100, verbose_name='s/n', blank=True)
    count = models.PositiveSmallIntegerField(default=1, verbose_name='Кол-во', blank=True)
    owner_executor = models.ForeignKey(Executor, on_delete=models.PROTECT, related_name='equipment_executor',
                                       verbose_name='Владелец', null=True, blank=True)
    owner_arenda = models.BooleanField(verbose_name='Аренда')
    owner_office = models.BooleanField(verbose_name='2You Studio')
    roma = models.BooleanField(verbose_name='Украл Рома')
    equipment_cost = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Себестоимость/час,₽',
                                         blank=True)
    equipment_price = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Стоимость/час,₽',
                                          blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Стоимость покупки', blank=True)
    link = models.URLField(verbose_name='Ссылка на аренду', blank=True)
    equipment_photo = models.ImageField(upload_to='equipment_photo/', verbose_name='Фото', null=True, blank=True)

    def __str__(self):
        return self.model

    class Meta:
        ordering = ['id']
        verbose_name = "Оборудование"
        verbose_name_plural = "006_Оборудование"


class IncomingType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип оплаты')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Тип оплаты"
        verbose_name_plural = "Типы оплаты"


class Incoming(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    incoming_value = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Сумма,₽',
                                         blank=True)
    incoming_type = models.ForeignKey(IncomingType, on_delete=models.PROTECT, related_name='incoming_type',
                                      verbose_name='Тип оплаты', null=True, blank=True)
    custumer = models.ForeignKey(Custumer, on_delete=models.PROTECT, related_name='incoming_custumer',
                                 verbose_name='Заказчик', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='incoming_company',
                                verbose_name='Компания', null=True, blank=True)
    schet = models.ForeignKey(Schet, on_delete=models.PROTECT, related_name='incoming_schet',
                              verbose_name='Счет на оплату', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='incoming_projects',
                                verbose_name='Проект', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Приход"
        verbose_name_plural = "013_Приход"


class OutComingTarget(models.Model):
    title = models.CharField(max_length=100, verbose_name='Цель оплаты')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Цель оплаты"
        verbose_name_plural = "Цели оплаты"


class OutComing(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    outcoming_value = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Сумма,₽',
                                          blank=True)
    outcoming_target = models.ForeignKey(OutComingTarget, on_delete=models.PROTECT, related_name='outcoming_type',
                                         verbose_name='Цель оплаты', null=True, blank=True)
    outcoming_type = models.ForeignKey(IncomingType, on_delete=models.PROTECT, related_name='outcoming_type',
                                       verbose_name='Тип оплаты', null=True, blank=True)
    executor = models.ForeignKey(Executor, on_delete=models.PROTECT, related_name='outcoming_executor',
                                 verbose_name='Заказчик', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='outcoming_company',
                                verbose_name='Компания', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='outcoming_projects',
                                verbose_name='Проект', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Траты"
        verbose_name_plural = "014_Траты"
