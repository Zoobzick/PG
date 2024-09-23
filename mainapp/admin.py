from django.contrib import admin
from django import forms
from mainapp.models import Project, ProjectImage
from mainapp.widgets import AdminImagePreviewWidget

class ProjectImageAdminForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = '__all__'
        widgets = {
            'image': AdminImagePreviewWidget(),
        }
# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    form = ProjectImageAdminForm
    extra = 1
    fields = ['image', 'hero_carousel']
    can_delete = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ProjectImageInline]
