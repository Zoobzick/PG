from django.forms import ClearableFileInput
from django.utils.html import format_html

class AdminImagePreviewWidget(ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        if value and hasattr(value, 'url'):
            output = format_html(
                '<a href="{0}" target="_blank"><img src="{0}" alt="{1}" style="max-height: 200px;"/></a>',
                value.url, value
            ) + output
        return output