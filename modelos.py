# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlunosAlunos(models.Model):
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

    class Meta:
        managed = False
        db_table = 'alunos_alunos'


class AmbientesAmbientesunidadesedu(models.Model):
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

    class Meta:
        managed = False
        db_table = 'ambientes_ambientesunidadesedu'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EscolasCeus(models.Model):
    cd_unidade = models.TextField(blank=True, null=True)
    nm_unidade = models.TextField(blank=True, null=True)
    nm_exibicao_unidade = models.TextField(blank=True, null=True)
    tp_unidade_administrativa = models.IntegerField(blank=True, null=True)
    dc_tipo_unidade_administrativa = models.TextField(blank=True, null=True)
    sg_unidade_administrativa = models.TextField(blank=True, null=True)
    cd_unidade_administrativa = models.TextField(blank=True, null=True)
    nm_unidade_administrativa = models.TextField(blank=True, null=True)
    database = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escolas_ceus'


class EscolasEscolas(models.Model):
    dre = models.TextField(blank=True, null=True)
    codesc = models.CharField(primary_key=True, max_length=6)
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

    class Meta:
        managed = False
        db_table = 'escolas_escolas'


class ServidoresServidores(models.Model):
    rf = models.TextField(blank=True, null=True)
    nm_nome = models.TextField(blank=True, null=True)
    cd_serv_sme = models.TextField(blank=True, null=True)
    mes_nasc = models.FloatField(blank=True, null=True)
    ano_nasc = models.FloatField(blank=True, null=True)
    idade = models.FloatField(blank=True, null=True)
    cd_sexo = models.TextField(blank=True, null=True)
    cd_municipio_nasc = models.IntegerField(blank=True, null=True)
    dc_municipio_nasc = models.CharField(max_length=100, blank=True, null=True)
    uf_municipio_nasc = models.CharField(max_length=2, blank=True, null=True)
    cd_pais_nasc = models.IntegerField(blank=True, null=True)
    dc_pais_nasc = models.CharField(max_length=50, blank=True, null=True)
    cd_municipio_res = models.IntegerField(blank=True, null=True)
    dc_municipio_res = models.CharField(max_length=100, blank=True, null=True)
    uf_municipio_res = models.CharField(max_length=2, blank=True, null=True)
    cd_raca_cor = models.IntegerField(blank=True, null=True)
    dc_raca_cor = models.CharField(max_length=20, blank=True, null=True)
    cd_def = models.IntegerField(blank=True, null=True)
    dc_def = models.CharField(max_length=70, blank=True, null=True)
    nivel_form = models.TextField(blank=True, null=True)
    dc_sit_func = models.CharField(max_length=40, blank=True, null=True)
    cd_cargo_base = models.IntegerField(blank=True, null=True)
    dc_cargo_base = models.CharField(max_length=70, blank=True, null=True)
    cd_area_atuacao_base = models.IntegerField(blank=True, null=True)
    dc_area_atuacao_base = models.CharField(max_length=70, blank=True, null=True)
    dt_inicio_cargo_base = models.TextField(blank=True, null=True)
    cd_unidade_base = models.CharField(max_length=6, blank=True, null=True)
    tp_unidade_base = models.CharField(max_length=12, blank=True, null=True)
    dc_unidade_base = models.CharField(max_length=60, blank=True, null=True)
    sigla_lotacao = models.TextField(blank=True, null=True)
    tp_lotacao = models.CharField(max_length=1, blank=True, null=True)
    cd_cargo_atual = models.IntegerField(blank=True, null=True)
    dc_cargo_atual = models.CharField(max_length=70, blank=True, null=True)
    cd_area_atuacao_cargo_atual = models.IntegerField(blank=True, null=True)
    dc_area_atuacao_cargo_atual = models.CharField(max_length=70, blank=True, null=True)
    cd_unidade_educacao_atual = models.CharField(max_length=6, blank=True, null=True)
    tp_unidade_educacao_atual = models.CharField(max_length=50, blank=True, null=True)
    dc_unidade_educacao_atual = models.CharField(max_length=60, blank=True, null=True)
    sigla_atual = models.TextField(blank=True, null=True)
    cd_unidade_funcao = models.CharField(max_length=20, blank=True, null=True)
    cd_funcao = models.IntegerField(blank=True, null=True)
    dc_funcao = models.CharField(max_length=100, blank=True, null=True)
    dt_inicio_funcao = models.TextField(blank=True, null=True)
    cd_unidade_sobreposto = models.CharField(max_length=20, blank=True, null=True)
    cd_sobreposto = models.IntegerField(blank=True, null=True)
    dc_sobreposto = models.CharField(max_length=100, blank=True, null=True)
    dt_inicio_sobreposto = models.TextField(blank=True, null=True)
    database = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidores_servidores'


class TurmasTurmas(models.Model):
    dre = models.TextField(blank=True, null=True)
    codesc = models.CharField(max_length=6, blank=True, null=True)
    codinep = models.IntegerField(blank=True, null=True)
    tipoesc = models.CharField(max_length=12, blank=True, null=True)
    nomesc = models.CharField(max_length=60, blank=True, null=True)
    subpref = models.CharField(max_length=35, blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    setor = models.SmallIntegerField(blank=True, null=True)
    dturnos = models.TextField(blank=True, null=True)
    t2d3d = models.TextField(blank=True, null=True)
    numsala = models.CharField(max_length=6, blank=True, null=True)
    codamb = models.IntegerField(blank=True, null=True)
    descamb = models.CharField(max_length=70, blank=True, null=True)
    capreal = models.IntegerField(blank=True, null=True)
    metragem = models.IntegerField(blank=True, null=True)
    codturm = models.IntegerField(primary_key=True)
    ano = models.IntegerField(blank=True, null=True)
    modal = models.CharField(max_length=60, blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)
    rede = models.TextField(blank=True, null=True)
    cdserie = models.IntegerField(blank=True, null=True)
    descserie = models.CharField(max_length=40, blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)
    turma = models.CharField(max_length=15, blank=True, null=True)
    vagofer = models.IntegerField(blank=True, null=True)
    matric = models.BigIntegerField(blank=True, null=True)
    alu_teg = models.BigIntegerField(blank=True, null=True)
    alu_teg_def = models.BigIntegerField(blank=True, null=True)
    hora_inicio = models.CharField(max_length=4, blank=True, null=True)
    hora_final = models.CharField(max_length=4, blank=True, null=True)
    dt_inclusao = models.DateTimeField(blank=True, null=True)
    localizacao = models.CharField(max_length=6, blank=True, null=True)
    classes = models.IntegerField(blank=True, null=True)
    x_semana = models.BigIntegerField(blank=True, null=True)
    durac_dia = models.IntegerField(blank=True, null=True)
    durac_semana = models.FloatField(blank=True, null=True)
    escolarizacao = models.TextField(blank=True, null=True)
    dias = models.TextField(blank=True, null=True)
    al_reprov = models.FloatField(blank=True, null=True)
    al_evad = models.FloatField(blank=True, null=True)
    al_aprov = models.FloatField(blank=True, null=True)
    al_fale = models.FloatField(blank=True, null=True)
    al_excl = models.FloatField(blank=True, null=True)
    al_ncom = models.FloatField(blank=True, null=True)
    al_nrem = models.FloatField(blank=True, null=True)
    pnee_ah = models.BigIntegerField(blank=True, null=True)
    pnee_da = models.BigIntegerField(blank=True, null=True)
    pnee_df = models.BigIntegerField(blank=True, null=True)
    pnee_dv = models.BigIntegerField(blank=True, null=True)
    pnee_di = models.BigIntegerField(blank=True, null=True)
    pnee_tgd = models.BigIntegerField(blank=True, null=True)
    pnee_bv = models.BigIntegerField(blank=True, null=True)
    pnee_ba = models.BigIntegerField(blank=True, null=True)
    pnee_tdi = models.BigIntegerField(blank=True, null=True)
    pnee_mul = models.BigIntegerField(blank=True, null=True)
    pnee_suce = models.BigIntegerField(blank=True, null=True)
    cadeir = models.BigIntegerField(blank=True, null=True)
    pnee_tot = models.BigIntegerField(blank=True, null=True)
    database = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turmas_turmas'
