# Generated by Django 4.0.6 on 2022-08-31 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0021_alter_article_author_alter_comment_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]
