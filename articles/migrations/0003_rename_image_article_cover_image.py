# Generated by Django 4.0.6 on 2022-08-12 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_author_article_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='cover_image',
        ),
    ]