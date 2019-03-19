from django.db import models


# Create your models here.
class Alunos(models.Model):
    dre = models.TextField(blank=True, null=True)
    codes = models.CharField(max_length=6, blank=True, null=True)
    tipoesc = models.CharField(max_length=12, blank=True, null=True)
    nomesc = models.CharField(max_length=60, blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    setor = models.SmallIntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    rede = models.TextField(blank=True, null=True)
    modal = models.CharField(max_length=100, blank=True, null=True)
    descserie = models.CharField(max_length=100, blank=True, null=True)
    periodo = models.TextField(blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)
    descturno = models.CharField(max_length=20, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    idade = models.FloatField(blank=True, null=True)
    nee = models.CharField(max_length=100, blank=True, null=True)
    raca = models.CharField(max_length=20, blank=True, null=True)
    qtd = models.BigIntegerField(blank=True, null=True)
    database = models.DateField(blank=True, null=True)
