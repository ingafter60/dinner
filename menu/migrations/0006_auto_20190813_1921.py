# Generated by Django 2.1 on 2019-08-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20190813_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(null=True, upload_to='menus/'),
        ),
    ]
