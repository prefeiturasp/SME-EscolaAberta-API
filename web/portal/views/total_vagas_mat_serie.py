from django.shortcuts import render
from escolas.models import Escolas
from turmas.models import Turmas
from rest_framework.views import APIView
from django.db import connection
from rest_framework.response import Response


# Create your views here.


class VagasMatriculasBySerie(APIView):

    def get(self, request, codesc, format=None):
        """
        Endpoint que disponibiliza um totalizador de vagas e matriculas por serie e escola, conforme o Encontre uma escola do portalSME
        :param codesc: Codigo da escola
        """
        query = """
select turma.descserie as serie,
       count(*)                   as total_turmas,
       sum(vagofer)               as vagas_oferecidas,
       sum(matric)                as atendimentos,
       sum(vagofer) - sum(matric) as vagas_remanecentes,
       round(avg(matric))         as media_atendimento
from turmas_turmas as turma
group by turma.modal, turma.codesc, turma.descserie
having turma.codesc = '{}'
union all
select turma.modal as serie,
       count(*)                   as total_turmas,
       sum(vagofer)               as vagas_oferecidas,
       sum(matric)                as atendimentos,
       sum(vagofer) - sum(matric) as vagas_remanecentes,
       round(avg(matric))         as media_atendimento
from turmas_turmas as turma
group by turma.modal, turma.codesc
having turma.codesc = '{}';""".format(codesc, codesc)

        cursor = connection.cursor()
        cursor.execute(query)
        # row = cursor.fetchall()
        # modalidades = {'modalidade': [mod[0] for mod in row]}
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
