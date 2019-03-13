from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import Nucleo
from .serializers import NucleoSerializer



class NucleoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    ##queryset = Nucleo.objects.all()
    serializer_class = NucleoSerializer

    # ------------- sistema de busca automatica do dajngo-restful
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'month', 'year')
    lookup_field = 'id' # campo de buscoa como recurso
    #-------------------------------------------------------------

## sobre escrita dos methods  para filtrar modelo de dados
    def get_queryset(self):

        # ---- filter/query text ----------------------
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)
        #---------------------------------------------------

        #--------------- cadeias de filtragem lazy ----------------
        queryset =  Nucleo.objects.filter()
        if id:
            queryset = Nucleo.objects.filter(pk=id)

        if name:
            queryset = queryset.filter(name__iexact=name)

        if month:
            queryset = queryset.filter(month__iexact=month)

        if year:
            queryset = queryset.filter(year__iexact=year)

        return queryset
        #----------------------------------------------------------

    ## sobre escrita dos verbos restful
    def list(self, request, *args, **kwargs):
        #return Response({'teste':123456})
        return super(NucleoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):





        return super(NucleoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(NucleoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(NucleoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(NucleoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(NucleoViewSet, self).partial_update(request, *args, **kwargs)


    @action(methods=['post', 'get'], detail=True)
    def tecnica_criar_action(self, request, pk=None):
        return Response({'nodetalhe': 123456})

    @action(methods=['get'], detail=False)
    def tecnica_criar_action_geral(self, request):
        return Response({'geral': 55555})

    @action(methods=['get'], detail=False)
    def summary(self, request, *args, **kwargs):
        recb = super(NucleoViewSet, self).list(request, *args, **kwargs)
        dados = recb.data
        soma_debitos = 0
        soma_creditos = 0
        for linha in dados:
            if 'debts' in linha.keys():
                if linha['debts']:
                    for Dvalor in linha['debts']:
                        soma_debitos += Dvalor['value']

            if 'credits' in linha.keys():
                if linha['credits']:
                    for Cvalor in linha['credits']:
                        soma_creditos += Cvalor['value']

        soma_debitos = "{0: .2f}".format(soma_debitos)
        soma_creditos = "{0: .2f}".format(soma_creditos)
        return Response({"credit":soma_creditos,"debt":soma_debitos})

