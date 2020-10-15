from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class LivroAbertoEscolas(APIView):

    def get(self, request, format=None):
        """
        Endpoint utilizado pelo livro aberto que retorna todas informações
        das escolas com quantidade de vagas oferecidas
        """
        query = """
                select escolas.*,
                    turmas.total_vagas,
                    coalesce(servidores.total_servidores, 0) as total_servidores,
                    coalesce(turmas.total_matriculados, 0) as total_matriculados
                from escolas_escolas as escolas
                    inner join (select codesc,
                                        sum(vagofer) total_vagas,
                                        sum(matric) as total_matriculados
                                from turmas_turmas as turmas
                                where cdserie notnull
                                    and escolarizacao = 'S'
                                    and matric notnull
                                group by codesc) turmas
                                on turmas.codesc = escolas.codesc
                    left join (select   count(cd_serv_sme) as total_servidores,
                                        cd_unidade_educacao_atual
                                from servidores_servidores ss
                                group by cd_unidade_educacao_atual) servidores
                                on escolas.codesc = servidores.cd_unidade_educacao_atual
                where tipoesc != 'ESC.PART.';
                """

        cursor = connection.cursor()
        cursor.execute(query)
        escolas = {'results':
                       [dict(zip([column[0] for column in cursor.description], row))
                        for row in cursor.fetchall()]}
        return Response(escolas)
