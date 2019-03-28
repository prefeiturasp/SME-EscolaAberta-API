from django.shortcuts import render
from escolas.models import Escolas
from turmas.models import Turmas
from rest_framework.views import APIView
from django.db import connection
from rest_framework.response import Response


# Create your views here.


class ServidoresAtuacaoEscola(APIView):

    def get(self, request, codesc, format=None):
        """
        Endpoint que disponibiliza os servidores e sua atuação por escola, conforme o Encontre uma escola do portalSME
        :param codesc: Codigo da escola
        """
        query = """
                    select trim(dc_cargo_atual) as dc_cargo_atual,trim(nm_nome) as nm_nome
                    from servidores_servidores
                    where cd_unidade_educacao_atual='{}'
                    group by dc_cargo_atual,nm_nome;""".format(codesc)

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
