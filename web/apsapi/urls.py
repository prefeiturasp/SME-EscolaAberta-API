from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from portal.views.alunos_por_serie_turno import AlunosSerieTurno
from portal.views.ambientes import Ambientes
from portal.views.diretorias import DiretoriasView
from portal.views.localizador_escola import LocalizadorEscola
from portal.views.modalidades import ModalidadesPraticadas
from portal.views.serie_estudantes import SerieEstudantes
from portal.views.servidores_atuacao import ServidoresAtuacaoEscola
from portal.views.sme_ambientes import SmeAmbientes
from portal.views.sme_escolas import SmeEscolasPorTipo
from portal.views.sme_profissionais import SmeProfissionais
from portal.views.tipo_escola import TipoEscolaView
from portal.views.total_servidores_atuacao import TotalServidoresAtuacaoEscola
from portal.views.total_servidores_escolaridade import ServidoresEscolarizacao
from portal.views.total_vagas_mat_serie import VagasMatriculasBySerie
from portal.views.turmas_serie_turno import TurmasSerieTurno
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

# -----------------arquivos staticos-------------------------------------------------
from django.conf import settings
from django.conf.urls.static import static
# -----------------------------------------------------------------------------------

from escolas.api.viewsets import EscolasViewSet, BairrosViewSet, DistritoViewSet, SubprefViewSet
from turmas.api.viewsets import TurmasViewSet
from servidores.api.viewsets import ServidoresViewSet
from ambientes.api.viewsets import AmbientesViewSet

schema_view = get_swagger_view(title='Escola Aberta API', url='/api/')

router = routers.DefaultRouter()
router.register(r'escolas', EscolasViewSet)
router.register(r'bairros', BairrosViewSet)
router.register(r'distritos', DistritoViewSet)
router.register(r'subpref', SubprefViewSet)
router.register(r'turmas', TurmasViewSet)
router.register(r'servidores', ServidoresViewSet)
router.register(r'ambientes', AmbientesViewSet)
# router.register('modalidades/<int:codesc>', ModalidadesPraticadas.as_view(), base_name='ModalidadeEnsino')

urlpatterns = [
                  path('', include(router.urls)),
                  path('docs', schema_view),
                  path('doc', schema_view),
                  path('admin/', admin.site.urls),
                  path('tipo_escola/', TipoEscolaView.as_view(), name='tipo_escola'),
                  path('diretorias/', DiretoriasView.as_view(), name='diretorias'),
                  path('modalidades/<slug:codesc>', ModalidadesPraticadas.as_view(), name='modalidades'),
                  path('totvagmatbyserie/<slug:codesc>', VagasMatriculasBySerie.as_view(), name='totvagmatbyserie'),
                  path('ambientesbyescola/<slug:codesc>', Ambientes.as_view(), name="ambientesbyescola"),
                  path('servatuacao/<slug:codesc>', ServidoresAtuacaoEscola.as_view(), name="servatuacao"),
                  path('totservatuacao/<slug:codesc>', TotalServidoresAtuacaoEscola.as_view(),
                       name="totservatuacao"),
                  path('totservescolarizacao/<slug:codesc>', ServidoresEscolarizacao.as_view(),
                       name="totservescolarizacao"),
                  path('alunosserieturno/<slug:codesc>', AlunosSerieTurno.as_view(), name="alunosserieturno"),
                  path('turmaserieturno/<slug:codesc>', TurmasSerieTurno.as_view(), name="turmaserieturno"),
                  path('seriesestudantes/<slug:codesc>', SerieEstudantes.as_view(), name="serieestudantes"),

                  path('smeescolas/<slug:cod_dre>', SmeEscolasPorTipo.as_view(), name="smeescolas_dre"),
                  path('smeescolas/', SmeEscolasPorTipo.as_view(), name="smeescolas"),

                  path('smeprofissionais/<slug:cod_dre>', SmeProfissionais.as_view(), name="smeescolas_dre"),
                  path('smeprofissionais/', SmeProfissionais.as_view(), name="smeescolas"),

                  path('smeambientes/<slug:cod_dre>', SmeAmbientes.as_view(), name="smeescolas_dre"),
                  path('smeambientes/', SmeAmbientes.as_view(), name="smeescolas"),

                  path('localizador', LocalizadorEscola.as_view(), name="localizadorescolas"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
