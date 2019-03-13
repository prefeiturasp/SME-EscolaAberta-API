from rest_framework.serializers import ModelSerializer
from creditos.models import Credits


class CreditosSerializer(ModelSerializer):
      class Meta:
        model = Credits
        fields = (
            'id', 'name', 'value'
        )


