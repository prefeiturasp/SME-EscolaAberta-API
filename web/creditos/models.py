from django.db import models



from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# validador personalizados

def validate_floatPositivos(value):
    if value < 0 :
        raise ValidationError(
            _('%(value)s somente maiores ou igual azero '),
            params={'value': value},
        )

class Credits(models.Model):
    name = models.CharField(max_length=150)
    value = models.FloatField(default=0,validators=[validate_floatPositivos] )

    def __str__(self):
        return self.name
