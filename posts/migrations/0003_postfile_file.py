# Generated by Django 5.1.7 on 2025-04-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_postfile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='postfile',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
