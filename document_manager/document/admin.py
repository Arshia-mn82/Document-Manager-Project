from django.contrib.admin import register,ModelAdmin
from .models import *

class TextFileAdmin(ModelAdmin):
    list_display = ['title','file']
    list_filter = ['title']
    search_fields = ['title']