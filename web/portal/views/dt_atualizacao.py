from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class DtAtualizacaoView(APIView):

    def get(self, request, format=None):
        """
        Endpoint que retorna a data de atualização das informações
        """
        query = """
       select max(dt) dt_atualizacao
from (
     select max(database) dt
from turmas_turmas
union all
select max(database) dt
from escolas_escolas
         ) juntado;
       """

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
