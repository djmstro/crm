# Generated by Django 4.0.5 on 2022-07-09 22:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0015_alter_dogovor_options_alter_akt_akt_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='dogovor',
        ),
        migrations.AddField(
            model_name='project',
            name='dogovor',
            field=models.ManyToManyField(blank=True, null=True, related_name='dogovors', to='crm.dogovor',
                                         verbose_name='Договор'),
        ),
    ]
