# Generated by Django 4.2.4 on 2024-09-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_project_client_alter_project_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='area',
            field=models.IntegerField(null=True, verbose_name='Площадь'),
        ),
    ]
