# Generated by Django 4.0.5 on 2022-07-09 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0012_project_dogovor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('akt_title', models.CharField(blank=True, max_length=150, verbose_name='Название акта')),
                ('akt_number', models.CharField(blank=True, max_length=150, verbose_name='Номер акта')),
                ('akt_date', models.DateField(blank=True, null=True, verbose_name='Дата акта')),
                ('akt_file', models.FileField(blank=True, upload_to='docs/acts/', verbose_name='Файл акта')),
                ('akt_price', models.DecimalField(decimal_places=0, default=0, max_digits=8, verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Акт',
                'verbose_name_plural': 'Акты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DocumentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Статус документа')),
            ],
            options={
                'verbose_name': 'Статус документа',
                'verbose_name_plural': 'Статусы документов',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DogovorTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dogovor_task_title', models.CharField(blank=True, max_length=150, verbose_name='Название Задания')),
                ('task_number', models.CharField(blank=True, max_length=150, verbose_name='Номер Задания')),
                ('task_date', models.DateField(blank=True, null=True, verbose_name='Дата Задания')),
                ('task_file', models.FileField(blank=True, upload_to='docs/tasks/', verbose_name='Файл Задания')),
                ('task_price', models.DecimalField(decimal_places=0, default=0, max_digits=8, verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Schet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schet_title', models.CharField(blank=True, max_length=150, verbose_name='Название счета')),
                ('schet_number', models.CharField(blank=True, max_length=150, verbose_name='Номер счета')),
                ('schet_date', models.DateField(blank=True, null=True, verbose_name='Дата счета')),
                ('schet_file', models.FileField(blank=True, upload_to='docs/schets/', verbose_name='Файл счета')),
                ('schet_price', models.DecimalField(decimal_places=0, default=0, max_digits=8, verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='dogovor',
            name='akt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='projects', to='crm.akt', verbose_name='Акт'),
        ),
        migrations.AddField(
            model_name='dogovor',
            name='document_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='projects', to='crm.documentstatus', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='dogovor',
            name='dogovor_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='projects', to='crm.dogovortask', verbose_name='Задание'),
        ),
        migrations.AddField(
            model_name='dogovor',
            name='schet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='projects', to='crm.schet', verbose_name='Счет'),
        ),
    ]
