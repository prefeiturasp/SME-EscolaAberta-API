from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from turmas.models import Turmas
from .serializers import TurmasSerializer


class TurmasViewSet(ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer

    def retrieve(self, request, *args, **kwargs):
        cd_esc = str(kwargs.get('pk', None))
        queryset = Turmas.objects.filter(codesc=cd_esc)
        serializer = TurmasSerializer(queryset, many=True)
        return Response(serializer.data)
