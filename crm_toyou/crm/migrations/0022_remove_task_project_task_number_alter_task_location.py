# Generated by Django 4.0.5 on 2022-07-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0021_parking_projecttaskstatus_servicecategory_services_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project_task_number',
        ),
        migrations.AlterField(
            model_name='task',
            name='location',
            field=models.CharField(blank=True, max_length=150, verbose_name='Локация'),
        ),
    ]
