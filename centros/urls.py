from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_bonos, name='lista_bonos'),
    path('bono/<str:pk>/', views.detalle_bono, name='detalle_bono'),
    path('bono/<str:pk>/edit/', views.edita_bono, name='edita_bono'),
    path('nuevo_bono/', views.nuevo_bono, name='nuevo_bono'),
]
