from django.db import models

# Create your models here.
from debitos.models import Debts
from creditos.models import Credits


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# validador personalizados
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
def validate_mes(value):
    if value < 1 or   value >12:
        raise ValidationError(
            _('%(value)s nao e um mes valido Faixa 1 a 12'),
            params={'value': value},
        )
def validate_ano(value):
    if value < 1970 or   value > 3000:
        raise ValidationError(
            _('%(value)s nao e um ano valido Faixa 1970 a 2999 '),
            params={'value': value},
        )





class Nucleo(models.Model):
    name = models.CharField(max_length=150)
    month = models.IntegerField(default=1,validators=[validate_mes] )
    year = models.IntegerField(default=2019,validators=[validate_ano])
    debts = models.ManyToManyField(Debts)
    credits = models.ManyToManyField(Credits)
    #debts = models.ForeignKey(Debts,on_delete=models.CASCADE,null=True,blank=True)
    #credits = models.ForeignKey(Credits,on_delete=models.CASCADE,null=True,blank=True)





    @property
    def campoextra2(self):
       return 'campo extra via property - %s' % self.name


    def __str__(self):
        return self.name
