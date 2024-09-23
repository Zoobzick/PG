from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models


# Create your models here.


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('industry', 'Промышленность'),
        ('logistics', 'Логистика'),
        ('warehouses', 'Склады'),
        ('public-objects', 'Общественные объекты'),
        ('other', 'Другие')]

    name = models.CharField(max_length=256,
                            verbose_name="Наименование проекта")

    title = models.CharField(max_length=256,
                             null=False,
                             blank=False,
                             verbose_name="Заголовок")

    client = models.CharField(max_length=256,
                              null=True,
                              blank=False,
                              verbose_name='Заказчик')

    category = models.CharField(max_length=50,
                                choices=CATEGORY_CHOICES,
                                default='industry',
                                verbose_name='Категория')

    date = models.DateField(
        verbose_name="Дата проекта")

    area = models.IntegerField(
        verbose_name='Площадь', null=True
    )

    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='images')

    image = models.ImageField(upload_to='projects/images/')

    hero_carusel = models.BooleanField(default=False,
                                       verbose_name="Карусель главной страницы")

    def convert_to_webp(self, uploaded_image):
        image = Image.open(uploaded_image)
        image_io = BytesIO()
        image.save(image_io, format='WEBP', quality=80)
        webp_image = ContentFile(image_io.getvalue(), name=uploaded_image.name.split('.')[0] + '.webp')
        return webp_image

    def save(self, *args, **kwargs):
        if self.image:
            self.image = self.convert_to_webp(self.image)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'Image for {self.project.title}'
