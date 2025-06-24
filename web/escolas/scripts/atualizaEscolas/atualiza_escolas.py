import json
from datetime import datetime
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
                if campo_modelo == "setor":
                    coddist = entrada.get("CDIST")
                    setor = entrada.get("SETOR")
                    if coddist is not None and setor is not None:
                        valor_json = int(f"{int(coddist):02d}{int(setor):02d}")
                    else:
                        continue
                elif campo_modelo in ["cep", "codinep"]:
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

if __name__ == "__main__":
    for entrada in dados_json:
        resultado = processar_entrada(entrada)
        print(resultado)
