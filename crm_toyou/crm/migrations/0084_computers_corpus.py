# Generated by Django 4.0.5 on 2022-08-01 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0083_computers_keyboard_computers_keyboard_sn_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='corpus',
            field=models.CharField(blank=True, max_length=150, verbose_name='Корпус'),
        ),
    ]
