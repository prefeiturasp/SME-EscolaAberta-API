from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from ambientes.models import AmbientesUnidadesEdu
from .serializers import AmbientesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response


class AmbientesViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsavel por retornar todos os ambientes, ou retornar ambientes de uma determinada escola
    """
    queryset = AmbientesUnidadesEdu.objects.all()
    serializer_class = AmbientesSerializer
    lookup_url_kwarg = 'codesc'

    def retrieve(self, request, *args, **kwargs):
        cd_esc = str(kwargs.get('codesc', None))
        queryset = AmbientesUnidadesEdu.objects.filter(codesc=cd_esc)
        serializer = AmbientesSerializer(queryset, many=True)
        return Response(serializer.data)
