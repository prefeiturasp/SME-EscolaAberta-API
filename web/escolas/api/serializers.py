from rest_framework.serializers import ModelSerializer
from escolas.models import Escolas


class EscolasSerializer(ModelSerializer):
    class Meta:
        model = Escolas
        fields = (
            '__all__'
        )
        filter_fields = ('cdesc')
