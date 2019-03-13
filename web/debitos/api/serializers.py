from rest_framework.serializers import ModelSerializer
from debitos.models import Debts


class DebitosSerializer(ModelSerializer):
      class Meta:
        model = Debts
        fields = (
            'id', 'name', 'value', 'status'
        )
