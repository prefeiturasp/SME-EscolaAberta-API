from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from portal.views.alunos_por_serie_turno import AlunosSerieTurno
from portal.views.ambientes import Ambientes
from portal.views.modalidades import ModalidadesPraticadas
from portal.views.servidores_atuacao import ServidoresAtuacaoEscola
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

from escolas.api.viewsets import EscolasViewSet
from turmas.api.viewsets import TurmasViewSet
from servidores.api.viewsets import ServidoresViewSet
from ambientes.api.viewsets import AmbientesViewSet

schema_view = get_swagger_view(title='Escola Aberta API')

router = routers.DefaultRouter()
router.register(r'api/escolas', EscolasViewSet)
router.register(r'api/turmas', TurmasViewSet)
router.register(r'api/servidores', ServidoresViewSet)
router.register(r'api/ambientes', AmbientesViewSet)
# router.register('api/modalidades/<int:codesc>', ModalidadesPraticadas.as_view(), base_name='ModalidadeEnsino')

urlpatterns = [
                  path('', include(router.urls)),
                  path('api/docs', schema_view),
                  path('api/doc', schema_view),
                  path('admin/', admin.site.urls),
                  path('api/modalidades/<slug:codesc>', ModalidadesPraticadas.as_view()),
                  path('api/totvagmatbyserie/<slug:codesc>', VagasMatriculasBySerie.as_view()),
                  path('api/ambientesbyescola/<slug:codesc>', Ambientes.as_view()),
                  path('api/servatuacao/<slug:codesc>', ServidoresAtuacaoEscola.as_view()),
                  path('api/totservatuacao/<slug:codesc>', TotalServidoresAtuacaoEscola.as_view()),
                  path('api/totservescolarizacao/<slug:codesc>', ServidoresEscolarizacao.as_view()),
                  path('api/alunosserieturno/<slug:codesc>', AlunosSerieTurno.as_view()),
                  path('api/turmaserieturno/<slug:codesc>', TurmasSerieTurno.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
