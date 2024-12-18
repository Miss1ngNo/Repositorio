from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestionar_variables, name='gestionar_variables'),
    path('agregar/', views.agregar_variables, name='agregar_variables'),
    path('modificar/<int:variable_id>/', views.modificar_variable, name='modificar_variable'),
    path('eliminar/<int:variable_id>/', views.eliminar_variable, name='eliminar_variable'),
]
