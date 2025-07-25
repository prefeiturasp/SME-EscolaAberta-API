import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from escolas.models import Escolas

with open("escolas/scripts/atualizaEscolas/dadosEscolas.json", "r", encoding="utf-8") as f:
    dados_json = json.load(f)

campo_mapeamento = {
    "dre": "DRE",
    "codesc": "CODESC",
    "tipoesc": "TIPOESC",
    "nomesc": "NOMESC",
    "ceu": "CEU",
    "diretoria": "DIRETORIA",
    "subpref": "SUBPREF",
    "endereco": "ENDERECO",
    "numero": "NUMERO",
    "bairro": "BAIRRO",
    "cep": "CEP",
    "tel1": "TEL1",
    "tel2": "TEL2",
    "fax": "FAX",
    "situacao": "SITUACAO",
    "coddist": "CDIST",
    "distrito": "DISTRITO",
    "setor": "SETOR",
    "codinep": "CODINEP",
    "eh": "EH",
    "nome_ant": "NOME_ANT",
    "rede": "REDE",
    "latitude": "LATITUDE",
    "longitude": "LONGITUDE",
    "database": "DATABASE",
}

def processar_entrada(entrada):
    codesc = entrada.get("CODESC")
    if not codesc:
        return "Registro ignorado: CODESC ausente."

    try:
        escola = Escolas.objects.get(codesc=codesc)
    except Escolas.DoesNotExist:
        return f"Escola com código {codesc} não encontrada."

    alterado = False
    for campo_modelo, campo_json in campo_mapeamento.items():
        valor_json = entrada.get(campo_json)
        if valor_json not in [None, ""]:
            try:
                if campo_modelo in ["cep", "setor", "codinep"]:
                    valor_json = int(valor_json)
                elif campo_modelo in ["latitude", "longitude"]:
                    valor_json = float(valor_json)
                elif campo_modelo == "database":
                    valor_json = datetime.strptime(valor_json, "%d/%m/%Y").date()
            except (ValueError, TypeError):
                continue

            if getattr(escola, campo_modelo) != valor_json:
                setattr(escola, campo_modelo, valor_json)
                alterado = True

    if alterado:
        escola.save()
        return f"Escola {codesc} atualizada."
    else:
        return f"Escola {codesc} sem alterações."

# Número de threads paralelas (ajuste conforme capacidade)
num_threads = 10

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futuros = [executor.submit(processar_entrada, entrada) for entrada in dados_json]

        for futuro in as_completed(futuros):
            resultado = futuro.result()
            print(resultado)
