# Generated by Django 2.2.3 on 2022-03-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0007_auto_20220319_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='write',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='articles',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='write',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
