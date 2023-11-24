from django.urls import path
from app_interface_grafica.views import exibir_pagina_inicial, obter_video, receber_teclas

urlpatterns = [
    path('', exibir_pagina_inicial, name='pagina_inicial'),
    path('obter_video/', obter_video, name='obter_video'),
    path('registrar-tecla/', receber_teclas, name='registrar_tecla'),
]
