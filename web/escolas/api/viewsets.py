from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from escolas.models import Escolas
from .serializers import EscolasSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class EscolasViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsável por retornar todas as escolas,
    filtrar pro Codigo da escola ou realizar pesquisa por nome da escola
    """
    queryset = Escolas.objects.all()
    serializer_class = EscolasSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nomesc',)
