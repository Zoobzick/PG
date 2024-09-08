from django.contrib import admin

from mainapp.models import Project, ProjectImage


# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image']
    can_delete = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ProjectImageInline]
