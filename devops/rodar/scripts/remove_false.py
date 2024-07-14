import os
import yaml

def remover_campos_desabilitados(dados):
    if isinstance(dados, dict):
        if 'enabled' in dados and dados['enabled'] is False:
            return {'enabled': False}
        return {k: remover_campos_desabilitados(v) for k, v in dados.items()}
    elif isinstance(dados, list):
        return [remover_campos_desabilitados(item) for item in dados]
    else:
        return dados

def processar_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            dados = yaml.safe_load(file)

        if dados is None:
            return

        dados_limpos = remover_campos_desabilitados(dados)

        with open(caminho_arquivo, 'w', encoding='utf-8') as file:
            yaml.dump(dados_limpos, file, default_flow_style=False, sort_keys=False)

        print(f"Processed file: {caminho_arquivo}")
    except Exception as e:
        print(f"Error processing {caminho_arquivo}: {e}")

def percorrer_diretorio(diretorio):
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.yaml'):
                caminho_arquivo = os.path.join(root, file)
                processar_arquivo(caminho_arquivo)

if __name__ == "__main__":
    diretorio_alvo = '../applications'  
    percorrer_diretorio(diretorio_alvo)
