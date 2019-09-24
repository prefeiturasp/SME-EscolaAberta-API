import django_filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from escolas.models import Escolas
from .serializers import EscolasSerializer, BairroSerializer, DistritoSerializer, SubprefSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class EscolasViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsável por retornar todas as escolas,
    filtrar pro Codigo da escola ou realizar pesquisa por nome da escola
    """
    queryset = Escolas.objects.exclude(tipoesc='ESC.PART.')
    serializer_class = EscolasSerializer
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,)
    search_fields = ('nomesc',)
    filterset_fields = ('dre', 'tipoesc', 'distrito', 'bairro')


class BairrosViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsável por retornar todas os bairros,
    filtrar pelo nome do bairros
    """
    queryset = Escolas.objects.distinct('bairro')
    serializer_class = BairroSerializer
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,)
    search_fields = ('bairro',)
    filterset_fields = ('bairro',)


class DistritoViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsável por retornar todas os distritos,
    filtrar pelo nome do distritos
    """
    queryset = Escolas.objects.distinct('distrito')
    serializer_class = DistritoSerializer
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,)
    search_fields = ('distrito',)
    filterset_fields = ('distrito',)


class SubprefViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsável por retornar todas os subprefeituras,
    filtrar pelo nome do subprefeituras
    """
    queryset = Escolas.objects.distinct('subpref')
    serializer_class = SubprefSerializer
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,)
    search_fields = ('subpref',)
    filterset_fields = ('subpref',)
