# Generated by Django 4.0.5 on 2022-08-01 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0077_archives_archives_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='archives',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='archives_brand', to='crm.equipmentbrand', verbose_name='Бренд'),
        ),
    ]
