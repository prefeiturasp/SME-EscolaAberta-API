from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class SmeVagasMatriculas(APIView):

    def get(self, request, cod_dre=None, format=None):
        """
        Endpoint que retorna os dados de vagas e matriculas da REDE ou por DRE
        """
        if cod_dre:
            query = """

select *
from (select turma.descserie            as decserie,
             turma.modal                as modalidade,
             count(*)                   as total_turmas,
             sum(vagofer)               as vagas_oferecidas,
             sum(matric)                as atendimentos,
             sum(vagofer) - sum(matric) as vagas_remanecentes,
             round(avg(matric))         as media_atendimento
      from turmas_turmas as turma
      where cdserie notnull
        and modal notnull
        and trim(dre) = '{}'
      group by turma.modal, turma.descserie
      union all
      select ''                         as decserie,
             turma.modal                as modalidade,
             count(*)                   as total_turmas,
             sum(vagofer)               as vagas_oferecidas,
             sum(matric)                as atendimentos,
             sum(vagofer) - sum(matric) as vagas_remanecentes,
             round(avg(matric))         as media_atendimento
      from turmas_turmas as turma
      where cdserie notnull
        and cdserie notnull
        and modal notnull
        and trim(dre) = '{}'
      group by turma.modal) as juntado
order by modalidade, decserie;

            """.format(cod_dre, cod_dre)

        else:
            query = """
select *
from (select turma.descserie            as decserie,
             turma.modal                as modalidade,
             count(*)                   as total_turmas,
             sum(vagofer)               as vagas_oferecidas,
             sum(matric)                as atendimentos,
             sum(vagofer) - sum(matric) as vagas_remanecentes,
             round(avg(matric))         as media_atendimento
      from turmas_turmas as turma
      where cdserie notnull
        and modal notnull
      group by turma.modal, turma.descserie
      union all
      select ''                         as decserie,
             turma.modal                as modalidade,
             count(*)                   as total_turmas,
             sum(vagofer)               as vagas_oferecidas,
             sum(matric)                as atendimentos,
             sum(vagofer) - sum(matric) as vagas_remanecentes,
             round(avg(matric))         as media_atendimento
      from turmas_turmas as turma
      where cdserie notnull
        and cdserie notnull
        and modal notnull
      group by turma.modal) as juntado
order by modalidade, decserie;
            """

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
