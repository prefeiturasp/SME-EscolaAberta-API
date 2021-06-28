from django.db import connection
from escolas.services import consulta_email_escola
from rest_framework.response import Response
from rest_framework.views import APIView


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


class LocalizadorEscola(APIView):

    def get(self, request, format=None):
        """
        Endpoint que realiza o calculo das distancias das escolas baseado na latitude e longitude
        retorna as top n escolas mais proximas dentro de um determinano raio
        :param lat: latitude do endereço
        :param lon: longitude do endereço
        :param radius: raio de delimitação
        :param top: numero de escolas para retornar
        """

        lat = request.GET.get('lat', None)
        lon = request.GET.get('lon', None)
        radius = request.GET.get('radius', None)
        top = request.GET.get('top', 10)

        # Filtros
        extra_filters = ''

        nomesc = request.GET.get('nomesc')
        if nomesc:
            extra_filters = extra_filters + f" and nomesc like '%{nomesc}%'"

        tipoesc = request.GET.get('tipoesc')
        if tipoesc:
            extra_filters = extra_filters + f" and tipoesc like '%{tipoesc}%'"

        dre = request.GET.get('dre')
        if dre:
            extra_filters = extra_filters + f" and dre like '%{dre}%'"

        bairro = request.GET.get('bairro')
        if bairro:
            extra_filters = extra_filters + f" and bairro like '%{bairro}%'"

        distrito = request.GET.get('distrito')
        if distrito:
            extra_filters = extra_filters + f" and distrito like '%{distrito}%'"

        if is_number(lat) and is_number(lon) and is_number(radius) and is_number(top):
            pass
        else:
            return Response('parametros errados')

        # https://pt.wikipedia.org/wiki/F%C3%B3rmula_de_Haversine
        # https://www.plumislandmedia.net/mysql/haversine-mysql-nearest-loc/
        query = f"""SELECT *
FROM (
         SELECT dre,
                codesc,
                tipoesc,
                nomesc,
                ceu,
                diretoria,
                subpref,
                endereco,
                numero,
                bairro,
                cep,
                tel1,
                tel2,
                fax,
                situacao,
                coddist,
                distrito,
                setor,
                codinep,
                cd_cie,
                eh,
                fx_etaria,
                rede,
                latitude,
                longitude,
                111.045 * DEGREES(ACOS(COS(RADIANS({lat}))--lat
                                           * COS(RADIANS(latitude))
                                           * COS(RADIANS(longitude) - RADIANS({lon}))--lon
                    + SIN(RADIANS({lat}))--lat
                                           * SIN(RADIANS(latitude))))
                    AS distance_in_km
         FROM escolas_escolas
         ORDER BY distance_in_km
         LIMIT {top}) as distancias
where distancias.distance_in_km <= {radius}
""" + extra_filters + """
  and distancias.tipoesc != 'ESC.PART.';
                    """

        cursor = connection.cursor()
        cursor.execute(query)

        results = []
        for row in cursor.fetchall():
            escola = dict(zip([column[0] for column in cursor.description], row))
            escola['email'] = consulta_email_escola(escola['codesc'])
            results.append(escola)

        modalidades = {'results': results}

        return Response(modalidades)
