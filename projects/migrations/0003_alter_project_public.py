# Generated by Django 4.0.6 on 2022-09-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='public',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='Публичный проект'),
        ),
    ]
