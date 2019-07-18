from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class SerieEstudantes(APIView):

    def get(self, request, codesc, format=None):
        """
        Endpoint que disponibiliza um totalizador de matriculados por turma, serie e turno
        :param codesc: Codigo da escola
        """
        query = """
                  select descserie,
       turma,
       case
           when turno = 1 then 'Manhã'
           when turno = 2 then 'Intermediário'
           when turno = 3 then 'Tarde'
           when turno = 4 then 'Vespertino'
           when turno = 5 then 'Noite'
           when turno = 6 then 'Integral'
           else '' end as desc_turno,
       modal,
       matric

from turmas_turmas
where cdserie notnull
  and codesc = '{}'
group by descserie, turma, turno, modal, matric;""".format(codesc)

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
