# Generated by Django 5.1.7 on 2025-04-03 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postfile_file'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='Posts',
        ),
        migrations.AlterModelTable(
            name='postfile',
            table='Post Files',
        ),
    ]
