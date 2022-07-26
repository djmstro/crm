# Generated by Django 4.0.5 on 2022-07-20 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0066_project_kp'),
    ]

    operations = [
        migrations.CreateModel(
            name='IsPaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Статус оплаты')),
            ],
            options={
                'verbose_name': 'Статус оплаты',
                'verbose_name_plural': 'Статусы оплаты',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_cost',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='Себестоимость'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='outcoming',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='outcoming_executor', to='crm.executor', verbose_name='Исполнитель'),
        ),
        migrations.AddField(
            model_name='project',
            name='is_paid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects_is_paid', to='crm.ispaid', verbose_name='Статус оплаты'),
        ),
    ]