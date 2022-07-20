# Generated by Django 4.0.5 on 2022-07-20 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0054_costvalue_alter_equipment_brand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тип оплаты')),
            ],
            options={
                'verbose_name': 'Тип оплаты',
                'verbose_name_plural': 'Типы оплаты',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='costvalue',
            options={'ordering': ['id'], 'verbose_name': 'Единицу измерения',
                     'verbose_name_plural': 'Единицы измерения'},
        ),
        migrations.AlterField(
            model_name='executor',
            name='driving_license',
            field=models.BooleanField(verbose_name='в/у'),
        ),
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Наименование')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('incoming_value',
                 models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, verbose_name='Сумма,₽')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                              related_name='incoming_company', to='crm.company',
                                              verbose_name='Компания')),
                ('custumer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                               related_name='incoming_custumer', to='crm.custumer',
                                               verbose_name='Заказчик')),
                ('incoming_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                                    related_name='incoming_type', to='crm.incomingtype',
                                                    verbose_name='Тип оплаты')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                              related_name='incoming_projects', to='crm.project',
                                              verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Приход',
                'verbose_name_plural': '013_Приход',
                'ordering': ['-created_at'],
            },
        ),
    ]
