# Generated by Django 4.0.6 on 2022-08-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='ip',
            field=models.CharField(max_length=100, null=True, verbose_name='Айпи'),
        ),
    ]