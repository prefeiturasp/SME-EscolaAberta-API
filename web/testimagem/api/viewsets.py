from rest_framework.viewsets import ModelViewSet
from testimagem.models import MinhasImagens
from .serializers import MinhasImagensSerializer

class MinhasImagensViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = MinhasImagens.objects.all()
    serializer_class = MinhasImagensSerializer