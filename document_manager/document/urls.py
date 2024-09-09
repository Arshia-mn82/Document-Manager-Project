from django.urls import path
from .views import *

urlpatterns = [
    path("list/", FileListCreateView.as_view()),
    path("upload/", FileListCreateView.as_view()),
    path("token/", Login.as_view()),
    path("token/refresh/", Refresh.as_view()),
]
