from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personas, name='lista_personas'),
    path('agregar/', views.agregar_persona, name='agregar_persona'),
    path('eliminar/<int:persona_id>/', views.eliminar_persona, name='eliminar_persona'),
    path('modificar/<int:persona_id>/', views.modificar_persona, name='modificar_persona'),
]