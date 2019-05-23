from django.db import connection
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

        if is_number(lat) and is_number(lon) and is_number(radius) and is_number(top):
            pass
        else:
            return Response('parametros errados')

        # https://pt.wikipedia.org/wiki/F%C3%B3rmula_de_Haversine
        # https://www.plumislandmedia.net/mysql/haversine-mysql-nearest-loc/
        query = f"""SELECT * FROM (
SELECT codesc,
       tipoesc,
       nomesc,
       endereco,
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
LIMIT {top}) as distancias where distancias.distance_in_km <= {radius} and distancias.tipoesc!='ESC.PART.';
                    """

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
