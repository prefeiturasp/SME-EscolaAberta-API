from django.test import TestCase

from .models import Servidores


class ServidoresSigiloTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        dados = {
            'cd_unidade_educacao_atual': '094145',
            'dc_cargo_atual': 'DIRETOR DE ESCOLA',
            'nivel_form': 'SUPERIOR COMPLETO',
            'sigla_atual': 'IP',
        }
        cls.publico = Servidores.objects.create(
            rf='RF-PUBLICO', nm_nome='PESSOA PUBLICA', **dados
        )
        cls.sigiloso = Servidores.objects.create(
            rf='RF-SIGILOSO', nm_nome='PESSOA SIGILOSA', possui_sigilo=True,
            **dados
        )
        Servidores.objects.create(
            nm_nome='PESSOA DE OUTRA ESCOLA',
            cd_unidade_educacao_atual='123456',
            dc_cargo_atual='DIRETOR DE ESCOLA',
            nivel_form='SUPERIOR COMPLETO',
            sigla_atual='JA',
        )

    def assert_campos_restritos_ausentes(self, registros):
        for registro in registros:
            self.assertNotIn('rf', registro)
            self.assertNotIn('possui_sigilo', registro)

    def test_listagem_geral_exclui_sigilosos_e_campos_restritos(self):
        resposta = self.client.get('/servidores/')

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.data['count'], 2)
        self.assertCountEqual(
            [item['nm_nome'] for item in resposta.data['results']],
            ['PESSOA PUBLICA', 'PESSOA DE OUTRA ESCOLA'],
        )
        self.assert_campos_restritos_ausentes(resposta.data['results'])

    def test_consulta_por_escola_exclui_sigilosos_e_campos_restritos(self):
        resposta = self.client.get('/servidores/094145/')

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(
            [item['nm_nome'] for item in resposta.data], ['PESSOA PUBLICA']
        )
        self.assert_campos_restritos_ausentes(resposta.data)

    def test_consulta_de_atuacao_exclui_sigilosos(self):
        resposta = self.client.get('/servatuacao/094145')

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.data['results'], [{
            'dc_cargo_atual': 'DIRETOR DE ESCOLA',
            'nm_nome': 'PESSOA PUBLICA',
        }])

    def test_consultas_por_escola_sem_nomes_quando_todos_sao_sigilosos(self):
        Servidores.objects.filter(pk=self.publico.pk).update(possui_sigilo=True)

        for url, chave in [
            ('/servidores/094145/', None),
            ('/servatuacao/094145', 'results'),
        ]:
            with self.subTest(url=url):
                resposta = self.client.get(url)
                self.assertEqual(resposta.status_code, 200)
                self.assertEqual(
                    resposta.data if chave is None else resposta.data[chave], []
                )

    def test_listagem_geral_vazia_quando_todos_sao_sigilosos(self):
        Servidores.objects.update(possui_sigilo=True)

        resposta = self.client.get('/servidores/')

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.data['count'], 0)
        self.assertEqual(resposta.data['results'], [])

    def test_totais_e_estatisticas_incluem_sigilosos(self):
        consultas = [
            ('/totservatuacao/094145', 2, 'total'),
            ('/totservescolarizacao/094145', 2, 'total'),
            ('/smeprofissionais/', 3, 'total'),
            ('/smeprofissionais/IP', 2, 'total'),
        ]
        antes = {}
        for url, total, campo in consultas:
            with self.subTest(url=url):
                resposta = self.client.get(url)
                self.assertEqual(resposta.status_code, 200)
                antes[url] = resposta.data
                if url.startswith('/totservatuacao/'):
                    registros = [
                        item for item in resposta.data['results']
                        if item['area_de_atuacao'] == 'TOTAL DE SERVIDORES'
                    ]
                else:
                    registros = resposta.data['results']
                self.assertEqual(sum(item[campo] for item in registros), total)

        Servidores.objects.update(possui_sigilo=True)

        for url, _, _ in consultas:
            with self.subTest(url=url):
                resposta = self.client.get(url)
                self.assertEqual(resposta.status_code, 200)
                self.assertEqual(resposta.data, antes[url])
