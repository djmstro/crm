# Generated by Django 4.0.5 on 2022-07-18 02:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0028_equipmentbrand_equipmenttype_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
    ]
