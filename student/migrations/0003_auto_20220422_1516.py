# Generated by Django 2.2.3 on 2022-04-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20220318_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstudent',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='telefon nomer'),
        ),
    ]
