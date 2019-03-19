from rest_framework.serializers import ModelSerializer
from ambientes.models import AmbientesUnidadesEdu


class AmbientesSerializer(ModelSerializer):
    class Meta:
        model = AmbientesUnidadesEdu
        fields = (
            '__all__'
        )
        filter_fields = ('codesc')
