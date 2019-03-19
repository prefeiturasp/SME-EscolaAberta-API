from django.db import models
from escolas.models import Escolas


# Create your models here.
class AmbientesUnidadesEdu(models.Model):
    tpamb = models.IntegerField(primary_key=True)
    codesc = models.CharField(max_length=6, blank=True, null=True)
    numsala = models.CharField(max_length=6, blank=True, null=True)
    descamb = models.CharField(max_length=70, blank=True, null=True)
    capfis = models.IntegerField(blank=True, null=True)
    capreal = models.IntegerField(blank=True, null=True)
    metragem = models.IntegerField(blank=True, null=True)
    localizacao = models.CharField(max_length=6, blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    dt_status = models.DateTimeField(blank=True, null=True)
    padrao = models.CharField(max_length=40, blank=True, null=True)
    flag_ut = models.CharField(max_length=1, blank=True, null=True)
    dt_atualizacao_tabela = models.DateTimeField(blank=True, null=True)
    dt_inicio = models.DateTimeField(blank=True, null=True)
    dt_fim = models.DateTimeField(blank=True, null=True)
    dre = models.CharField(max_length=60, blank=True, null=True)
    tipoesc = models.CharField(max_length=12, blank=True, null=True)
    nomesc = models.CharField(max_length=60, blank=True, null=True)
    database = models.DateField(blank=True, null=True)
