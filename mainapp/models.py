from django.db import models


# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=256, unique=True, null=False, blank=False,
                            verbose_name="Наименование проекта")

    title = models.CharField(max_length=256, unique=True, null=False, blank=False)

    date = models.DateField(
        verbose_name="Дата проекта"
    )

    description = models.TextField()
