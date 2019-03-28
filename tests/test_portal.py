from portal.views.alunos_por_serie_turno import AlunosSerieTurno
from portal.views.ambientes import Ambientes
from portal.views.servidores_atuacao import ServidoresAtuacaoEscola
from portal.views.total_servidores_atuacao import TotalServidoresAtuacaoEscola
from portal.views.total_vagas_mat_serie import VagasMatriculasBySerie
from portal.views.turmas_serie_turno import TurmasSerieTurno
from rest_framework.test import APIRequestFactory
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from portal.views.modalidades import ModalidadesPraticadas
from portal.views.total_servidores_escolaridade import ServidoresEscolarizacao


def resolve_by_name_and_escola094145(name, **kwargs):
    url = reverse(name, kwargs={'codesc': '094145'})
    return resolve(url)


class PortalUrlsTestCase(SimpleTestCase):

    def test_resolves_ModalidadesPraticadas_url(self):
        resolver = resolve_by_name_and_escola094145("modalidades")
        self.assertEqual(resolver.func.cls, ModalidadesPraticadas)

    def test_resolves_VagasMatriculasBySerie_url(self):
        resolver = resolve_by_name_and_escola094145("totvagmatbyserie")
        self.assertEqual(resolver.func.cls, VagasMatriculasBySerie)

    def test_resolves_Ambientes_url(self):
        resolver = resolve_by_name_and_escola094145("ambientesbyescola")
        self.assertEqual(resolver.func.cls, Ambientes)

    def test_resolves_ServidoresAtuacaoEscola_url(self):
        resolver = resolve_by_name_and_escola094145("servatuacao")
        self.assertEqual(resolver.func.cls, ServidoresAtuacaoEscola)

    def test_resolves_TotalServidoresAtuacaoEscola_url(self):
        resolver = resolve_by_name_and_escola094145("totservatuacao")
        self.assertEqual(resolver.func.cls, TotalServidoresAtuacaoEscola)

    def test_resolves_ServidoresEscolarizacao_url(self):
        resolver = resolve_by_name_and_escola094145("totservescolarizacao")
        self.assertEqual(resolver.func.cls, ServidoresEscolarizacao)

    def test_resolves_AlunosSerieTurno_url(self):
        resolver = resolve_by_name_and_escola094145("alunosserieturno")
        self.assertEqual(resolver.func.cls, AlunosSerieTurno)

    def test_resolves_TurmasSerieTurno_url(self):
        resolver = resolve_by_name_and_escola094145("turmaserieturno")
        self.assertEqual(resolver.func.cls, TurmasSerieTurno)

