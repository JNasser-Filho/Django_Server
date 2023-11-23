'''from django.urls import path
from app_interface_grafica import views

urlpatterns = [
    path('',views.home,name="home"),
]'''

from django.urls import path
from app_interface_grafica.views import exibir_pagina_inicial, obter_video

urlpatterns = [
    path('', exibir_pagina_inicial, name='pagina_inicial'),
    path('obter_video/', obter_video, name='obter_video'),
]
