# Generated by Django 2.2.3 on 2022-04-21 12:17

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0011_auto_20220420_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_application',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Tel nomer', max_length=31),
        ),
    ]