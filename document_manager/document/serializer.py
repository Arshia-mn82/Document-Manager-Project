from rest_framework.serializers import ModelSerializer
from .models import *

class TextFileSerializer(ModelSerializer):
    class Meta:
        model = TextFile
        fields = ['id', 'file', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        
