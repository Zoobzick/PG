# Generated by Django 4.2.4 on 2024-10-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_rename_hero_carusel_projectimage_hero_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Заказчик'),
        ),
    ]
