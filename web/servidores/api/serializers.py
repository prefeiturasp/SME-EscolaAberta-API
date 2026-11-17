from rest_framework.serializers import ModelSerializer
from servidores.models import Servidores


class ServidoresSerializer(ModelSerializer):
    class Meta:
        model = Servidores
        exclude = ('rf', 'possui_sigilo')

        filter_fields = ('cd_unidade_educacao_atual')
