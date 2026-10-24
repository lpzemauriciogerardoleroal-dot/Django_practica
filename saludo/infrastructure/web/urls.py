from django.urls import path
from saludo.infrastructure.web.views import saludar_view

urlpatterns = [
    path('saludar/', saludar_view, name='saludar'),
]