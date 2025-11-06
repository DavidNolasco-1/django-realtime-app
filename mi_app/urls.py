# mi_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Esta ruta asocia la raíz de la app ('/') con la función views.items_page
    path('', views.items_page, name='items_page'),
]