# Generated by Django 4.0.5 on 2022-07-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0044_remove_executorprograms_executor_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executor',
            name='kod_podrazdelenia',
            field=models.IntegerField(blank=True, null=True, verbose_name='Код подразделения'),
        ),
        migrations.AlterField(
            model_name='executor',
            name='passport_n',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='executor',
            name='passport_s',
            field=models.IntegerField(blank=True, null=True, verbose_name='Серия паспорта'),
        ),
    ]
