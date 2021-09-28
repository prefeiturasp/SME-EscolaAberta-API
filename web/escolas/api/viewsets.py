import django_filters
from escolas.filters import CeuFilter
from rest_framework.viewsets import ReadOnlyModelViewSet
from escolas.models import Escolas, Ceus
from .serializers import EscolasSerializer, BairroSerializer, DistritoSerializer, SubprefSerializer, CeuSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response

class EscolasViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsável por retornar todas as escolas,
    filtrar pro Codigo da escola ou realizar pesquisa por nome da escola
    """
    queryset = Escolas.objects.exclude(tipoesc='ESC.PART.').order_by('codesc')
    serializer_class = EscolasSerializer
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,)
    search_fields = ('nomesc', 'nomescofi')
    filterset_fields = ('dre', 'tipoesc', 'distrito', 'bairro', 'subpref')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if 'page' in request.query_params:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


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


class CeuViewSet(ReadOnlyModelViewSet):
    queryset = Ceus.objects.all()
    serializer_class = CeuSerializer
    filterset_class = CeuFilter
