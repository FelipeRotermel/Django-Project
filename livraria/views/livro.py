# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import (
    LivroSerializer,
    LivroDetailSerializer,
    LivroListSerializer,
)

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        else:
            return LivroSerializer