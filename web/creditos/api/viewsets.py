from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Credits
from .serializers import CreditosSerializer

class CreditosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Credits.objects.all()
    serializer_class = CreditosSerializer

    #================ tecnica automatizada de filtragem usando djangobackend
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'value')