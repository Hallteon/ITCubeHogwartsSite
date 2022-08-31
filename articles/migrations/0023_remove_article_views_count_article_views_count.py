# Generated by Django 4.0.6 on 2022-08-31 07:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0022_alter_tag_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='views_count',
        ),
        migrations.AddField(
            model_name='article',
            name='views_count',
            field=models.ManyToManyField(blank=True, default=0, related_name='views', to=settings.AUTH_USER_MODEL, verbose_name='Количество просмотров'),
        ),
    ]
