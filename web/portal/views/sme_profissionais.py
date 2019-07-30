from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class SmeProfissionais(APIView):

    def get(self, request, cod_dre=None, format=None):
        """
        Endpoint que retorna os dados dos servidores da REDE ou por DRE
        """
        if cod_dre:
            query = """
select trim(dc_cargo_atual) titulo, trim(nivel_form) formacao, count(*) total
from servidores_servidores
where nivel_form notnull
and sigla_atual = '{}'
group by nivel_form, dc_cargo_atual; --
            """.format(cod_dre)

        else:
            query = """
           select trim(dc_cargo_atual) titulo, trim(nivel_form) formacao, count(*) total
from servidores_servidores
where nivel_form notnull
group by nivel_form, dc_cargo_atual
            """

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
