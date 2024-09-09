from django.contrib.admin import register,ModelAdmin
from .models import *

@register(TextFile)
class TextFileAdmin(ModelAdmin):
    pass