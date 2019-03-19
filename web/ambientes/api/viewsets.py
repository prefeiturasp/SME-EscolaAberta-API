from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from ambientes.models import AmbientesUnidadesEdu
from .serializers import AmbientesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response


class AmbientesViewSet(ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = AmbientesUnidadesEdu.objects.all()
    serializer_class = AmbientesSerializer

    def retrieve(self, request, *args, **kwargs):
        cd_esc = str(kwargs.get('pk', None))
        queryset = AmbientesUnidadesEdu.objects.filter(codesc=cd_esc)
        serializer = AmbientesSerializer(queryset, many=True)
        return Response(serializer.data)
