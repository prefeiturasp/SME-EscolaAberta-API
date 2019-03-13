from django.db import models

# Create your models here.



from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# validador personalizados

def validate_floatPositivos(value):
    if value < 0 :
        raise ValidationError(
            _('%(value)s somente maiores ou igual azero '),
            params={'value': value},
        )



class Debts(models.Model):
    PAGO = 'PAGO'
    PENDENTE = 'PENDENTE'
    AGENDADO = 'AGENDADO'

    STATUS_PAGAMENTO = (
        (PAGO, 'PAGO'),
        (PENDENTE, 'PENDENTE'),
        (AGENDADO, 'AGENDADO'),
    )



    name = models.CharField(max_length=150)
    value = models.FloatField(default=0,validators=[validate_floatPositivos] )
    status = models.CharField(max_length=10,choices=STATUS_PAGAMENTO,default=PENDENTE)

    def __str__(self):
        return self.name

