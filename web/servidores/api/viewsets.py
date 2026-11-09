from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from servidores.models import Servidores

from .serializers import ServidoresSerializer


class ServidoresViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsavel por retornar todos os servidores, ou retornar servidores de uma determinada escola
    """
    queryset = Servidores.objects.filter(possui_sigilo=False)
    serializer_class = ServidoresSerializer
    lookup_url_kwarg = 'codesc'

    def retrieve(self, request, *args, **kwargs):
        cd_esc = str(kwargs.get('codesc', None))
        queryset = self.get_queryset().filter(
            cd_unidade_educacao_atual=cd_esc
        ).distinct('nm_nome')
        serializer = ServidoresSerializer(queryset, many=True)
        return Response(serializer.data)
