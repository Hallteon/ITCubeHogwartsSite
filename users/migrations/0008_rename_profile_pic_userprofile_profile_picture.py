# Generated by Django 4.0.6 on 2022-08-26 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
    ]