# Generated by Django 4.0.5 on 2022-08-01 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0074_rename_status_project_statusproject_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type_call',
            new_name='TypeCall',
        ),
    ]