# Generated by Django 4.0.6 on 2022-09-10 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_alter_article_views_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-create_time'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]