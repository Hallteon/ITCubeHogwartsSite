# Generated by Django 4.0.6 on 2022-08-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_delete_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя профиля'),
        ),
    ]