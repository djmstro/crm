# Generated by Django 4.0.5 on 2022-07-20 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0055_incomingtype_alter_costvalue_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutComingTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Цель оплаты')),
            ],
            options={
                'verbose_name': 'Цель оплаты',
                'verbose_name_plural': 'Цели оплаты',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='incoming',
            name='schet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='incoming_schet', to='crm.schet', verbose_name='Счет на оплату'),
        ),
        migrations.CreateModel(
            name='OutComing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Наименование')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('outcoming_value',
                 models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, verbose_name='Сумма,₽')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                              related_name='outcoming_company', to='crm.company',
                                              verbose_name='Компания')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                               related_name='outcoming_executor', to='crm.executor',
                                               verbose_name='Заказчик')),
                ('outcoming_target',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                   related_name='outcoming_type', to='crm.outcomingtarget',
                                   verbose_name='Цель оплаты')),
                ('outcoming_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                                     related_name='outcoming_type', to='crm.incomingtype',
                                                     verbose_name='Тип оплаты')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                              related_name='outcoming_projects', to='crm.project',
                                              verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Траты',
                'verbose_name_plural': '014_Траты',
                'ordering': ['-created_at'],
            },
        ),
    ]