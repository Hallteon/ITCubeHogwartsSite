# Generated by Django 4.0.6 on 2022-09-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=650, verbose_name='Описание'),
        ),
    ]
