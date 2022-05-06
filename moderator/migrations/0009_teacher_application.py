# Generated by Django 2.2.3 on 2022-04-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0008_auto_20220319_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200, verbose_name='Familya')),
                ('first_name', models.CharField(max_length=200, verbose_name='Ism')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Tel nomber')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('about', models.TextField(verbose_name='Kurs haqida qisqacha malumot')),
            ],
        ),
    ]
