# Generated by Django 4.2.4 on 2024-09-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='hero_carusel',
            field=models.BooleanField(default=False, verbose_name='Карусель главной страницы'),
        ),
    ]