from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class SmeEscolasPorTipo(APIView):

    def get(self, request, cod_dre=None, format=None):
        """
        Endpoint que retorna os dados de matricula por escola da REDE ou por DRE
        """
        if cod_dre:
            query = """
            select bucket_table.dre, bucket_table.tipoesc, bucket_table.faixa, count( bucket_table.faixa)
from (
         select table_mat.*,
                case
                    when mat isnull then 'Sem estudantes cadastrados'
                    when (mat >= 1) and (mat <= 250) then '1 a 250 estudantes'
                    when (mat >= 251) and (mat <= 500) then '251 a 500 estudantes'
                    when (mat >= 501) and (mat <= 1000) then '501 a 1000 estudantes'
                    when (mat >= 1001) and (mat <= 1500) then '1001 a 1500 estudantes'
                    when (mat >= 1501) and (mat <= 2000) then '1501 a 2000 estudantes'
                    when (mat >= 2001) and (mat <= 2500) then '2001 a 2500 estudantes'
                    END as faixa
         from (select dre,
                      codesc,
                      tipoesc,
                      sum(matric) mat
               from turmas_turmas
               where dre='{}'
               group by dre, codesc
                      , tipoesc) table_mat
     ) as bucket_table
group by bucket_table.dre, bucket_table.tipoesc, bucket_table.faixa;--
            """.format(cod_dre)

        else:
            query = """
            select  bucket_table.tipoesc, bucket_table.faixa, count( bucket_table.faixa)
from (
         select table_mat.*,
                case
                    when mat isnull then 'Sem estudantes cadastrados'
                    when (mat >= 1) and (mat <= 250) then '1 a 250 estudantes'
                    when (mat >= 251) and (mat <= 500) then '251 a 500 estudantes'
                    when (mat >= 501) and (mat <= 1000) then '501 a 1000 estudantes'
                    when (mat >= 1001) and (mat <= 1500) then '1001 a 1500 estudantes'
                    when (mat >= 1501) and (mat <= 2000) then '1501 a 2000 estudantes'
                    when (mat >= 2001) and (mat <= 2500) then '2001 a 2500 estudantes'
                    END as faixa
         from (select
                      codesc,
                      tipoesc,
                      sum(matric) mat
               from turmas_turmas
               group by  codesc
                      , tipoesc) table_mat
     ) as bucket_table
group by  bucket_table.tipoesc, bucket_table.faixa; --
            """

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
