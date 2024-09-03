from django.contrib import admin
from mainapp.models import Project
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
