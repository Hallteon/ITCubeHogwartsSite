# Generated by Django 4.0.6 on 2022-09-11 06:52

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Текст'),
        ),
    ]
