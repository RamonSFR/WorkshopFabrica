from django.contrib import admin
from django.urls import path, include
from setup.views import ProdutoViewSet, LojaViewSet,ClienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Produto', ProdutoViewSet, basename='Produtos')
router.register('lojas', LojaViewSet, basename='Lojas')
router.register("cliente",LojaViewSet,basename="Clientes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
