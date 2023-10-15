from django.urls import path
from . import views

urlpatterns = [
    path('principal', views.obterMenuPrincipal, name='menu-principal'),
    path('plataforma', views.obterMenuPlataforma, name='menu-plataforma'),
    path('suporte', views.obterMenuSuporte, name='menu-suporte'),
    path('suporte', views.obterMenuSuporte, name='menu-cancelamento'),

    path('plataforma/inicio', views.obterPlataformaInicio, name='plataforma-inicio'),
    path('plataforma/exercicios', views.obterPlataformaExercicios, name='plataforma-exercicios'),
    path('plataforma/videos', views.obterPlataformaVideos, name='plataforma-videos'),
    path('plataforma/tempo', views.obterPlataformaTempo, name='plataforma-tempo'),
]
