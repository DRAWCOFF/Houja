import json
import os

PATH_QUESTOES = "questoes.json"

def carregar_questoes():
    if os.path.exists(PATH_QUESTOES):
        with open(PATH_QUESTOES, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return {"STAGE1": []}
carregar_questoes()

def salvar_perguntas(data):
    with open(PATH_QUESTOES, "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo, indent=4, ensure_ascii=False)

dados = carregar_questoes()