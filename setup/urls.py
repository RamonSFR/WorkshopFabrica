from django.contrib import admin
from django.urls import path, include
from videogame_store.views import jogo,jogoViewSet,LojaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("jogos",jogoViewSet,basename="Jogos")
router.register("lojas",LojaViewSet,basename="Lojas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls))
]

