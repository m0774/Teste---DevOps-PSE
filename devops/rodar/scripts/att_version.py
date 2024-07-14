import os

def atualizar_versao_no_arquivo(caminho_arquivo, versoes_antigas, nova_versao):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            linhas = file.readlines()

        with open(caminho_arquivo, 'w', encoding='utf-8') as file:
            for linha in linhas:
                for versao_antiga in versoes_antigas:
                    if f'version: {versao_antiga}' in linha:
                        linha = linha.replace(f'version: {versao_antiga}', f'version: {nova_versao}')
                file.write(linha)
        
        print(f"Versão atualizada em: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")

def percorrer_diretorio(diretorio, versoes_antigas, nova_versao):
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file == 'kustomization.yaml':
                caminho_arquivo = os.path.join(root, file)
                atualizar_versao_no_arquivo(caminho_arquivo, versoes_antigas, nova_versao)

if __name__ == "__main__":
    diretorio_alvo = '../applications'
    versoes_antigas = ['2.2.0', '2.1.0', '1.0.1']
    nova_versao = '2.2.1'
    percorrer_diretorio(diretorio_alvo, versoes_antigas, nova_versao)
