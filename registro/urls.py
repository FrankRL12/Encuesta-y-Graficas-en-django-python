from django.urls import path
from django.conf import settings
from .import views


urlpatterns = [
    path('', views.registro, name='registro'),
    path('tabla/', views.tabla, name='tabla'),
    path('graficas/', views.graficas, name='graficas'),
]
