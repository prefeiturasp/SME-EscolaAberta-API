from rest_framework.viewsets import ModelViewSet
from debitos.models import Debts
from .serializers import DebitosSerializer

class DebitosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Debts.objects.all()
    serializer_class = DebitosSerializer