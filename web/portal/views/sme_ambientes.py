from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class SmeAmbientes(APIView):

    def get(self, request, cod_dre=None, format=None):
        """
        Endpoint que retorna os dados dos ambientes da REDE ou por DRE
        """
        if cod_dre:
            query = """
select trim(descamb) as ambiente, count(*) as total
from ambientes_ambientesunidadesedu
where flag_ut = 'S'
  and descamb notnull
and dre like 'DRE - {}'
group by descamb;
            """.format(cod_dre)

        else:
            query = """
           select trim(descamb) as ambiente, count(*) as total
from ambientes_ambientesunidadesedu
where flag_ut = 'S'
  and descamb notnull
group by descamb;
            """

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
