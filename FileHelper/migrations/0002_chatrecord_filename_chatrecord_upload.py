# Generated by Django 4.2.6 on 2023-12-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileHelper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatrecord',
            name='filename',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='chatrecord',
            name='upload',
            field=models.FileField(default='', upload_to='upload/'),
        ),
    ]
