# Generated by Django 4.0.5 on 2022-08-01 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0070_alter_location_options_remove_task_parking'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Место хранения оборудования')),
            ],
            options={
                'verbose_name': 'Место хранения оборудования',
                'verbose_name_plural': 'Места хранения оборудованияя',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='equipment_location', to='crm.equipmentlocation',
                                    verbose_name='Место хранения'),
        ),
    ]