# Generated by Django 2.2.3 on 2022-03-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_createcourse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '2. Kurslar bazasi'},
        ),
        migrations.AlterModelOptions(
            name='createcourse',
            options={'verbose_name': '3. Oqtuvchiga kurs biriktrish'},
        ),
        migrations.AddField(
            model_name='userstaff',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name="O'quv joyi manzili"),
        ),
    ]
