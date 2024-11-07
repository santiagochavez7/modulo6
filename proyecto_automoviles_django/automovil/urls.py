from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('agregar/', views.nuevo_automovil, name='nuevo_automovil'),
    path('<int:id>/', views.detalle_automovil, name='detalle_automovil'),
    path('catalogo/', views.catalogo_automoviles, name='catalogo_automoviles'),
]
