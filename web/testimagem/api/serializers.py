from rest_framework.serializers import ModelSerializer
from testimagem.models import MinhasImagens


class MinhasImagensSerializer(ModelSerializer):
      class Meta:
        model = MinhasImagens
        fields = (
            'id', 'name' ,'foto', 'descricao'
        )


