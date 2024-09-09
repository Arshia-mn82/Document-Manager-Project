from .serializer import *
from .models import *
from rest_framework.views import APIView
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass


class FileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        files = TextFile.objects.filter(user=request.user)
        serializer = TextFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [FileUploadParser]

    def post(self, request):
        file_serializer = TextFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save(user=request.user)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        file = get_object_or_404(TextFile, pk=pk, user=request.user)
        response = FileResponse(file.file.open("rb"))
        return response


class FileDownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        file = get_object_or_404(TextFile, pk=pk, user=request.user)
        response = FileResponse(file.file.open("rb"))
        return response


class FileEditView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        file = get_object_or_404(TextFile, pk=pk, user=request.user)
        file_serializer = TextFileSerializer(file, data=request.data, partial=True)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_200_OK)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        file = get_object_or_404(TextFile, pk=pk, user=request.user)
        file.file.delete()
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
