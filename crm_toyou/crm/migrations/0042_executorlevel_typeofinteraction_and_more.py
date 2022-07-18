# Generated by Django 4.0.5 on 2022-07-18 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0041_alter_company_name_alter_executor_executor_cost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutorLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Уровень Исполнителя',
                'verbose_name_plural': 'Уровни Исполнителей',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypeOfInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип взаимодейтсвия',
                'verbose_name_plural': 'Типы взаимодействия',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='executor',
            name='office',
        ),
        migrations.AddField(
            model_name='executor',
            name='executor_comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='executor',
            name='executor_tg',
            field=models.CharField(blank=True, max_length=100, verbose_name='Телеграм'),
        ),
        migrations.AddField(
            model_name='executor',
            name='executor_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='executor_level', to='crm.executorlevel', verbose_name='Уровень'),
        ),
        migrations.AddField(
            model_name='executor',
            name='type_of_interaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='executor_interaction', to='crm.typeofinteraction',
                                    verbose_name='Тип взаимодейтсвия'),
        ),
    ]
