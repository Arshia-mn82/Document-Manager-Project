from django.db import models
from django.contrib.auth.models import User

class TextFile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    file_title = models.CharField(max_length=100)
    file_description = models.TextField()
    file = models.FileField(upload_to='text_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.file.name
    
