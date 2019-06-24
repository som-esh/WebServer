from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Todo/', include('lists.urls')),
]
