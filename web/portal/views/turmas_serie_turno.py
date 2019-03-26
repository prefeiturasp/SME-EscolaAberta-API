from rest_framework.views import APIView
from django.db import connection
from rest_framework.response import Response


# Create your views here.


class TurmasSerieTurno(APIView):

    def get(self, request, codesc, format=None):
        """
        Endpoint que disponibiliza um totalizador de turmas por serie e turno por escola, conforme o Encontre uma escola do portalSME
        :param codesc: Codigo da escola
        """
        query = """select turma,
                   descserie,
                   case
                     when turno = 1 then 'Manhã'
                     when turno = 2 then 'Intermediário'
                     when turno = 3 then 'Tarde'
                     when turno = 4 then 'Vespertino'
                     when turno = 5 then 'Noite'
                     when turno = 6 then 'Integral'
                     else 'Não Informado' end as turno
            from turmas_turmas
            where codesc = '{}'
            group by descserie, turno;""".format(codesc)

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
