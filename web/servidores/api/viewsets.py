from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from servidores.models import Servidores

from .serializers import ServidoresSerializer


class ServidoresViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsavel por retornar todos os servidores, ou retornar servidores de uma determinada escola
    """
    queryset = Servidores.objects.all()
    serializer_class = ServidoresSerializer
    lookup_url_kwarg = 'codesc'

    def retrieve(self, request, *args, **kwargs):
        cd_esc = str(kwargs.get('codesc', None))
        queryset = Servidores.objects.filter(cd_unidade_educacao_atual=cd_esc)
        serializer = ServidoresSerializer(queryset, many=True)
        return Response(serializer.data)
