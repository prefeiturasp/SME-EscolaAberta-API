from rest_framework.viewsets import ModelViewSet
from creditos.models import Credits
from .serializers import CreditosSerializer

class CreditosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Credits.objects.all()
    serializer_class = CreditosSerializer
