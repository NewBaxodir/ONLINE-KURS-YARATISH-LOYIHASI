# Generated by Django 2.2.3 on 2022-03-12 10:23

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_userstaff_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Createlesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Qisqacha malumot')),
                ('text', ckeditor.fields.RichTextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Createcourse')),
            ],
            options={
                'verbose_name': '4. Darsliklarni ishlab chiqish',
            },
        ),
    ]