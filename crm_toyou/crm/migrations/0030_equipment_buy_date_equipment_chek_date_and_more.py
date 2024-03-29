# Generated by Django 4.0.5 on 2022-07-18 02:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0029_equipment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='buy_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата покупки по чеку'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='chek_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата документа'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='chek_number',
            field=models.CharField(blank=True, max_length=150, verbose_name='Номер документа'),
        ),
    ]
