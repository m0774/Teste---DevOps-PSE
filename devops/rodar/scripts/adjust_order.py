import os
import yaml

def processar_arquivo_yaml(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            dados = yaml.safe_load(file)

        if dados is None:
            return

        with open(caminho_arquivo, 'w', encoding='utf-8') as file:
            yaml.dump(dados, file, default_flow_style=False, sort_keys=False)

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
