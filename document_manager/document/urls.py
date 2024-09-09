from django.urls import path
from .views import *

urlpatterns = [
    path("list/", FileListView.as_view()),
    path("upload/", FileUploadView.as_view()),
    path("token/", Login.as_view()),
    path("token/refresh/", Refresh.as_view()),
]
