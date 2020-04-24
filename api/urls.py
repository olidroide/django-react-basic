from django.urls import path

from . import views

urlpatterns = [
    path('lead/', views.connect),
]
