from rest_framework.serializers import ModelSerializer
from servidores.models import Servidores


class ServidoresSerializer(ModelSerializer):
    class Meta:
        model = Servidores
        fields = (
            '__all__'
        )
        filter_fields = ('cd_unidade_educacao_atual')
