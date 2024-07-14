import os
import yaml

def adicionar_env_aos_valores_yaml(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            dados = yaml.safe_load(file)

        if dados is None:
            return

        if os.path.basename(caminho_arquivo) == 'values.yaml':
            if 'env' in dados:
                dados['env']['ENV'] = 'dev'
            else:
                dados['env'] = {'ENV': 'dev'}

            with open(caminho_arquivo, 'w', encoding='utf-8') as file:
                yaml.dump(dados, file, default_flow_style=False, sort_keys=False)

            print(f"Adicionado ENV: dev ao arquivo: {caminho_arquivo}")
        else:
            print(f"Ignorando arquivo: {caminho_arquivo}")

    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")

def percorrer_diretorio(diretorio):
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.yaml'):
                caminho_arquivo = os.path.join(root, file)
                adicionar_env_aos_valores_yaml(caminho_arquivo)

if __name__ == "__main__":
    diretorio_alvo = '../applications' 
    percorrer_diretorio(diretorio_alvo)
