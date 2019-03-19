from django.shortcuts import render
from escolas.models import Escolas
from turmas.models import Turmas
from rest_framework.views import APIView
from django.db import connection
from rest_framework.response import Response


# Create your views here.


class Ambientes(APIView):

    def get(self, request, codesc, format=None):
        """

        :param request:
        :param codesc:
        :param format:
        :return:
        """
        query = """
                    select trim(descamb) as ambiente, count(*) as total
                    from ambientes_ambientesunidadesedu
                    where codesc = '{}'
                      and flag_ut = 'S'
                      and descamb not null
                    group by descamb;""".format(codesc)

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
