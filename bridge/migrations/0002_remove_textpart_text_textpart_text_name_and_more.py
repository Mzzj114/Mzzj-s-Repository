# Generated by Django 4.2.6 on 2023-10-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textpart',
            name='text',
        ),
        migrations.AddField(
            model_name='textpart',
            name='text_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='textpart',
            name='texts',
            field=models.CharField(default='', max_length=500),
        ),
    ]
