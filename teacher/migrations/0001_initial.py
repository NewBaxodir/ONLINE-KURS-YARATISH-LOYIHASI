# Generated by Django 2.2.3 on 2022-03-03 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('moderator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Kursning nomi')),
            ],
            options={
                'verbose_name': '1. Hodimlarning kurslar bazasi',
            },
        ),
        migrations.CreateModel(
            name='Userstaff',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sex', models.CharField(blank=True, choices=[('ERKAK', 'ERKAK'), ('AYOL', 'AYOL')], max_length=100, null=True, verbose_name='Jinsi')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, verbose_name='telefon nomer')),
                ('staff_image', models.ImageField(blank=True, null=True, upload_to='staff_images')),
                ('coursen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Course')),
            ],
            options={
                'verbose_name': '1. Hodimlar bazasi',
            },
        ),
    ]
