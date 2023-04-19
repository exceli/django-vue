from django.urls import path, include

from .views import PersonAPIView

urlpatterns = [
    path('form/', PersonAPIView.as_view(), name='form'),
]