from rest_framework.serializers import ModelSerializer
from turmas.models import Turmas


class TurmasSerializer(ModelSerializer):
    class Meta:
        model = Turmas
        fields = (
            '__all__'
        )
        filter_fields = ('codesc')
