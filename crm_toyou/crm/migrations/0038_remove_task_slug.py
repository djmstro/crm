# Generated by Django 4.0.5 on 2022-07-18 04:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0037_remove_car_executor_executor_car_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='slug',
        ),
    ]
