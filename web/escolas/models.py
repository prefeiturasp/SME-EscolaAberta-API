from django.db import models


# Create your models here.

class Escolas(models.Model):
    dre = models.TextField(blank=True, null=True)
    codesc = models.CharField(max_length=6, primary_key=True)
    tipoesc = models.CharField(max_length=12, blank=True, null=True)
    nomesc = models.CharField(max_length=60, blank=True, null=True)
    ceu = models.TextField(blank=True, null=True)
    diretoria = models.CharField(max_length=60, blank=True, null=True)
    subpref = models.CharField(max_length=35, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    numero = models.CharField(max_length=6, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cep = models.IntegerField(blank=True, null=True)
    tel1 = models.CharField(max_length=40, blank=True, null=True)
    tel2 = models.CharField(max_length=40, blank=True, null=True)
    fax = models.CharField(max_length=40, blank=True, null=True)
    situacao = models.CharField(max_length=10, blank=True, null=True)
    coddist = models.TextField(blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    setor = models.SmallIntegerField(blank=True, null=True)
    codinep = models.IntegerField(blank=True, null=True)
    cd_cie = models.TextField(blank=True, null=True)
    eh = models.CharField(max_length=15, blank=True, null=True)
    fx_etaria = models.CharField(max_length=100, blank=True, null=True)
    dt_criacao = models.DateTimeField(blank=True, null=True)
    ato_criacao = models.CharField(max_length=20, blank=True, null=True)
    dom_criacao = models.DateTimeField(blank=True, null=True)
    dt_ini_conv = models.DateTimeField(blank=True, null=True)
    dt_ini_func = models.DateTimeField(blank=True, null=True)
    dt_autoriza = models.DateTimeField(blank=True, null=True)
    dt_extintao = models.DateTimeField(blank=True, null=True)
    nome_ant = models.CharField(max_length=100, blank=True, null=True)
    rede = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    database = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.codesc) + '-' + str(self.nomesc)
