from .serializer import TextFileSerializer
from .models import TextFile
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass

# List and Create View for File Management
class FileListCreateView(ListCreateAPIView):
    serializer_class = TextFileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [FileUploadParser]

    def get_queryset(self):
        # Filter files by the authenticated user
        return TextFile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save file with the user who is authenticated
        serializer.save(user=self.request.user)

# Retrieve, Update, and Delete View for Single File Operations
class FileRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = TextFileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Filter by authenticated user to ensure security
        return TextFile.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        # Custom retrieve logic for downloading the file
        file = self.get_object()
        return FileResponse(file.file.open("rb"))

