from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.inicio, name='inicio'),
    path('juego/<int:juego_id>/', views.detalle, name='detalle'),
]
 