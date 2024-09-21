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

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
    def __str__(self):
        return f'Image for {self.project.title}'

