# Generated by Django 2.2.3 on 2022-03-10 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20220304_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstaff',
            name='coursen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.Course'),
        ),
    ]
