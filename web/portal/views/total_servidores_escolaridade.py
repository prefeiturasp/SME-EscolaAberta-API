from django.shortcuts import render
from escolas.models import Escolas
from turmas.models import Turmas
from rest_framework.views import APIView
from django.db import connection
from rest_framework.response import Response


# Create your views here.


class ServidoresEscolarizacao(APIView):

    def get(self, request, codesc, format=None):
        """

        :param request:
        :param codesc:
        :param format:
        :return:
        """
        query = """
                   select trim(dc_cargo_atual) titulo , trim(nivel_form) formacao, count(*) total
                    from servidores_servidores
                    where cd_unidade_educacao_atual = '{}'
                      and nivel_form notnull
                    group by nivel_form, dc_cargo_atual;""".format(codesc)

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
