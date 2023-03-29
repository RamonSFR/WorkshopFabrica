from rest_framework import viewsets
from .models import jogo , loja
from .serializer import JogoSerializer , LojaSerializer

class jogoViewSet(viewsets.ModelViewSet):
    queryset = jogo.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = loja.objects.all()
    serializer_class = LojaSerializer


