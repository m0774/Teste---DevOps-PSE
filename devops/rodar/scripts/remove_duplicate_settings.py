import os
import yaml

def remover_duplicatas(data):
    if isinstance(data, list):
        lista_unica = []
        visto = set()
        for item in data:
            item_str = yaml.dump(item)
            if item_str not in visto:
                visto.add(item_str)
                lista_unica.append(item)
        return lista_unica
    elif isinstance(data, dict):
        dados_unicos = {}
        for chave, valor in data.items():
            dados_unicos[chave] = remover_duplicatas(valor)
        return dados_unicos
    else:
        return data

def processar_arquivo_yaml(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            dados = yaml.safe_load(file)

        if dados is None:
            return

        dados_unicos = remover_duplicatas(dados)

        with open(caminho_arquivo, 'w', encoding='utf-8') as file:
            yaml.dump(dados_unicos, file, default_flow_style=False, sort_keys=False)

        print(f"Arquivo processado: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")

def percorrer_diretorio(diretorio):
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.yaml'):
                caminho_arquivo = os.path.join(root, file)
                processar_arquivo_yaml(caminho_arquivo)

if __name__ == "__main__":
    diretorio_alvo = '../applications' 
    percorrer_diretorio(diretorio_alvo)
