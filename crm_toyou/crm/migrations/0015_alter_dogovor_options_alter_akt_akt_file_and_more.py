# Generated by Django 4.0.5 on 2022-07-09 22:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0014_akt_document_status_dogovortask_document_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dogovor',
            options={'ordering': ['id'], 'verbose_name': 'Договор', 'verbose_name_plural': 'Договоры'},
        ),
        migrations.AlterField(
            model_name='akt',
            name='akt_file',
            field=models.FileField(blank=True, null=True, upload_to='docs/acts/', verbose_name='Файл акта'),
        ),
        migrations.AlterField(
            model_name='akt',
            name='akt_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='dogovor_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='dogovor_title',
            field=models.CharField(blank=True, max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='dogovortask',
            name='task_file',
            field=models.FileField(blank=True, null=True, upload_to='docs/tasks/', verbose_name='Файл Задания'),
        ),
        migrations.AlterField(
            model_name='dogovortask',
            name='task_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='schet',
            name='schet_file',
            field=models.FileField(blank=True, null=True, upload_to='docs/schets/', verbose_name='Файл счета'),
        ),
        migrations.AlterField(
            model_name='schet',
            name='schet_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, verbose_name='Сумма'),
        ),
    ]
