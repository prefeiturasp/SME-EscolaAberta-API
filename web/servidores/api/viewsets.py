from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from servidores.models import Servidores
from .serializers import ServidoresSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response


class ServidoresViewSet(ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Servidores.objects.all()
    serializer_class = ServidoresSerializer

    def retrieve(self, request, *args, **kwargs):
        cd_esc = str(kwargs.get('pk', None))
        queryset = Servidores.objects.filter(cd_unidade_educacao_atual=cd_esc)
        serializer = ServidoresSerializer(queryset, many=True)
        return Response(serializer.data)
