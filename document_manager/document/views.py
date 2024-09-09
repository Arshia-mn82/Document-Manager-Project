from .serializer import TextFileSerializer
from .models import TextFile
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import io
from rest_framework import status
from django.core.files.base import ContentFile


class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass


class FileCreateView(CreateAPIView):
    serializer_class = TextFileSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        file_title = request.data.get("file_title")
        file_description = request.data.get("file_description")
        file_content = request.data.get("file_content")

        if not file_title or not file_description or not file_content:
            return Response(
                {
                    "detail": "file_title, file_description, and file_content are required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        file_content = ContentFile(file_content, "new_file.txt")

        text_file = TextFile(
            user=self.request.user,
            file_title=file_title,
            file_description=file_description,
            file=file_content,
        )
        text_file.save()

        serializer = self.get_serializer(text_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# List and Create View for File Management
class FileListCreateView(ListCreateAPIView):
    serializer_class = TextFileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TextFile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = TextFileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TextFile.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        file = instance.file

        response = FileResponse(file.open("rb"), content_type="text/plain")
        response["Content-Disposition"] = f'attachment; filename="{file.name}"'
        return response
