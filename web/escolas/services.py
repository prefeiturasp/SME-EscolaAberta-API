import os

import requests
from rest_framework import status


def consulta_email_escola(codigo_escola):
    """ Consulta dados de uma unidade no EOL e retorna o email da escola
        (get) /api/escolas/dados/{codigo_eol}
        Result =
            {
              "nomeDRE": "DIRETORIA REGIONAL DE EDUCACAO CAPELA DO SOCORRO",
              "siglaDRE": "DRE - CS",
              "codigoDRE": "108300",
              "siglaTipoEscola": null,
              "nome": "TRES LAGOS - JOSE ARISTODEMO PINOTTI, PROFESSOR",
              "tipoUnidade": "UNIDADE ADMINISTRATIVA",
              "email": null,
              "telefone": "59765642",
              "tipoLogradouro": "Rua",
              "logradouro": "MARIA MOURA DA CONCEICAO",
              "numero": "S/N",
              "bairro": "JARDIM BELCITO",
              "cep": 4855257
            }

        Return: email
    """

    headers = {
        'accept': 'application/json',
        'x-api-eol-key': os.environ.get('SME_INTEGRACAO_TOKEN')
    }
    timeout = 20
    print(f'Consultando no eol dados da unidade {codigo_escola}.')
    try:
        url = f'{os.environ.get("SME_INTEGRACAO_URL")}/api/escolas/dados/{codigo_escola}'
        response = requests.get(url, headers=headers)
        if response.status_code == status.HTTP_200_OK:
            return response.json()['email']
        else:
            print("Falha ao tentar consultar dados da unidade no eol: %s", response)
    except Exception as err:
        print("Erro ao tentar ao consulta dados da unidade do eol: %s", str(err))
    
    return ''

    