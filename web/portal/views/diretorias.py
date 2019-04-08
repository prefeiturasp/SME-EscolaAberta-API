from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class DiretoriasView(APIView):

    def get(self, request, format=None):
        """
        Endpoint que retorna as diretorias
        """
        query = """
        select dre,diretoria from escolas_escolas group by dre,diretoria;"""

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
